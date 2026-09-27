"""
CCR Analytics Engine - SA-CCR Calculator v1.2.0
================================================

Standardised Approach for Counterparty Credit Risk (SA-CCR)
per Basel III/IV framework.

Copyright © 2025-2030, All Rights Reserved
Ashutosh Sinha | Email: ajsinha@gmail.com
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from enum import Enum
import math

from ..base import BaseCalculator, CalculatorType, ImplementationType


class AssetClass(Enum):
    """SA-CCR asset classes."""
    INTEREST_RATE = "interest_rate"
    FX = "fx"
    CREDIT = "credit"
    EQUITY = "equity"
    COMMODITY = "commodity"


# Supervisory factors by asset class
SUPERVISORY_FACTORS = {
    AssetClass.INTEREST_RATE: 0.005,  # 0.5%
    AssetClass.FX: 0.04,  # 4%
    AssetClass.CREDIT: {
        "AAA": 0.0038,
        "AA": 0.0042,
        "A": 0.0054,
        "BBB": 0.0106,
        "BB": 0.016,
        "B": 0.06,
        "CCC": 0.15,
    },
    AssetClass.EQUITY: 0.32,  # 32%
    AssetClass.COMMODITY: {
        "electricity": 0.40,
        "oil": 0.18,
        "other": 0.18,
    },
}


@dataclass
class SACCRInput:
    """Input for SA-CCR calculation."""
    netting_set_id: str = ""
    trades: List[Dict[str, Any]] = field(default_factory=list)
    collateral: float = 0.0  # Signed net independent collateral amount (NICA)
    variation_margin: float = 0.0  # Signed net VM; C = NICA + VM
    threshold: float = 0.0
    minimum_transfer_amount: float = 0.0
    margin_period_of_risk: float = 10.0  # days
    is_margined: bool = False


@dataclass
class SACCRResult:
    """SA-CCR calculation result."""
    netting_set_id: str = ""
    replacement_cost: float = 0.0
    pfe_addon: float = 0.0
    multiplier: float = 1.0
    ead: float = 0.0
    
    # Add-ons by asset class
    ir_addon: float = 0.0
    fx_addon: float = 0.0
    credit_addon: float = 0.0
    equity_addon: float = 0.0
    commodity_addon: float = 0.0
    
    # Hedging set details
    hedging_sets: Dict[str, float] = field(default_factory=dict)
    
    alpha: float = 1.4


class SACCRCalculator(BaseCalculator):
    """
    SA-CCR Calculator per Basel III/IV.
    
    Implements the Standardised Approach for measuring counterparty
    credit risk exposures including:
    - Replacement cost calculation
    - PFE add-on calculation by asset class
    - Multiplier for negative MTM
    - Final EAD calculation
    """
    
    ALPHA = 1.4  # Regulatory multiplier
    
    def __init__(self):
        super().__init__("SACCRCalculator", {})

    @property
    def calculator_type(self) -> CalculatorType:
        return CalculatorType.EAD
    
    def calculate(self, input_data: SACCRInput) -> SACCRResult:
        """Calculate EAD and preserve the historical direct-result API."""
        return super().calculate(input_data).value

    def _calculate_impl(self, input_data: SACCRInput) -> SACCRResult:
        """Calculate the simplified SA-CCR netting-set result."""
        self._validate_input(input_data)
        result = SACCRResult(netting_set_id=input_data.netting_set_id)
        market_value = sum(t.get("mtm", 0.0) for t in input_data.trades)
        net_collateral = input_data.collateral + (
            input_data.variation_margin if input_data.is_margined else 0.0
        )
        
        # Step 1: Calculate Replacement Cost
        result.replacement_cost = self._calculate_rc(input_data)
        
        # Step 2: Calculate PFE Add-on by asset class
        addons = self._calculate_addons(input_data)
        result.ir_addon = addons.get("interest_rate", 0.0)
        result.fx_addon = addons.get("fx", 0.0)
        result.credit_addon = addons.get("credit", 0.0)
        result.equity_addon = addons.get("equity", 0.0)
        result.commodity_addon = addons.get("commodity", 0.0)
        
        aggregate_addon = sum(addons.values())
        
        # Step 3: Calculate Multiplier
        result.multiplier = self._calculate_multiplier(
            market_value,
            aggregate_addon,
            net_collateral,
        )
        
        # Step 4: Calculate PFE
        result.pfe_addon = result.multiplier * aggregate_addon
        
        # Step 5: Calculate EAD
        result.ead = self.ALPHA * (result.replacement_cost + result.pfe_addon)
        result.alpha = self.ALPHA
        
        return result

    def _validate_input(self, input_data: SACCRInput) -> None:
        """Reject inputs for which the regulatory formulas are undefined."""
        amounts = (
            input_data.collateral,
            input_data.variation_margin,
            input_data.threshold,
            input_data.minimum_transfer_amount,
            input_data.margin_period_of_risk,
        )
        if not all(math.isfinite(amount) for amount in amounts):
            raise ValueError("SA-CCR inputs must be finite")
        if input_data.margin_period_of_risk <= 0:
            raise ValueError("margin_period_of_risk must be positive")
        if input_data.threshold < 0 or input_data.minimum_transfer_amount < 0:
            raise ValueError("threshold and minimum_transfer_amount cannot be negative")
        for trade in input_data.trades:
            if not all(math.isfinite(trade.get(key, default)) for key, default in
                       (("mtm", 0.0), ("notional", 0.0), ("maturity", 1.0), ("delta", 1.0))):
                raise ValueError("trade amounts must be finite")
            if trade.get("notional", 0.0) < 0 or trade.get("maturity", 1.0) < 0:
                raise ValueError("notional and maturity cannot be negative")
    
    def _calculate_rc(self, input_data: SACCRInput) -> float:
        """CRE52.10/52.18 replacement cost, with signed VM and NICA."""
        total_mtm = sum(
            t.get("mtm", 0.0) for t in input_data.trades
        )
        
        if input_data.is_margined:
            net_collateral = input_data.collateral + input_data.variation_margin
            rc = max(
                total_mtm - net_collateral,
                input_data.threshold + input_data.minimum_transfer_amount
                - input_data.collateral,
                0.0,
            )
        else:
            # For unmargined netting sets  
            rc = max(0, total_mtm - input_data.collateral)
        
        return rc
    
    def _calculate_addons(self, input_data: SACCRInput) -> Dict[str, float]:
        """Calculate add-ons by asset class."""
        addons = {
            "interest_rate": 0.0,
            "fx": 0.0,
            "credit": 0.0,
            "equity": 0.0,
            "commodity": 0.0,
        }
        
        for trade in input_data.trades:
            asset_class = trade.get("asset_class", "").lower()
            notional = trade.get("notional", 0.0)
            maturity = trade.get("maturity", 1.0)
            
            # Maturity factor
            if input_data.is_margined:
                # Default model: non-centrally-cleared daily margin agreement.
                mpor = max(10.0, input_data.margin_period_of_risk) / 250
                mf = 1.5 * math.sqrt(mpor)
            else:
                mf = math.sqrt(min(max(maturity, 10 / 250), 1.0))
            
            # Supervisory duration
            sd = self._supervisory_duration(0, maturity)
            
            # Get supervisory factor
            sf = self._get_supervisory_factor(asset_class, trade)
            
            # Adjusted notional
            if asset_class == "interest_rate":
                adj_notional = notional * sd
            else:
                adj_notional = notional
            
            # Delta (simplified - assumes linear)
            delta = trade.get("delta", 1.0)
            
            # Add-on for this trade
            addon = sf * abs(delta) * adj_notional * mf
            
            if asset_class in addons:
                addons[asset_class] += addon
        
        return addons
    
    def _supervisory_duration(self, start: float, end: float) -> float:
        """Calculate supervisory duration."""
        if end <= start:
            return 0.0
        return (math.exp(-0.05 * start) - math.exp(-0.05 * end)) / 0.05
    
    def _get_supervisory_factor(self, asset_class: str, trade: Dict) -> float:
        """Get supervisory factor for trade."""
        if asset_class == "interest_rate":
            return 0.005
        elif asset_class == "fx":
            return 0.04
        elif asset_class == "credit":
            rating = trade.get("rating", "BBB")
            return SUPERVISORY_FACTORS[AssetClass.CREDIT].get(rating, 0.0106)
        elif asset_class == "equity":
            return 0.32
        elif asset_class == "commodity":
            commodity_type = trade.get("commodity_type", "other")
            return SUPERVISORY_FACTORS[AssetClass.COMMODITY].get(commodity_type, 0.18)
        else:
            return 0.0
    
    def _calculate_multiplier(self, market_value: float, addon: float,
                              collateral: float) -> float:
        """CRE52.23 multiplier based on V - C, before flooring RC."""
        if addon == 0:
            return 1.0
        
        # Floor at 5%
        floor = 0.05
        
        # Calculate V - C
        v_minus_c = market_value - collateral
        
        if v_minus_c >= 0:
            return 1.0
        
        # Multiplier formula
        ratio = v_minus_c / (2 * (1 - floor) * addon)
        multiplier = floor + (1 - floor) * math.exp(ratio)
        
        return min(1.0, multiplier)


__all__ = [
    "AssetClass",
    "SUPERVISORY_FACTORS",
    "SACCRInput",
    "SACCRResult",
    "SACCRCalculator",
]
