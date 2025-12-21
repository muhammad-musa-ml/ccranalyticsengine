"""
CCR Analytics Engine - Models Module v1.2.0
============================================

Comprehensive domain models for CCR Analytics Engine.

Modules:
- base: Abstract base model
- trade: Trade and transaction models
- portfolio: Portfolio aggregation models
- counterparty: Counterparty and netting set models
- curve: Yield, credit, and volatility curves
- market_data: Market data snapshots
- products: 27 financial product types
- scenario: Stress testing scenarios
- exposure: Exposure calculation results
- rating: Credit ratings and transitions

Copyright © 2025-2030, All Rights Reserved
Ashutosh Sinha | Email: ajsinha@gmail.com
"""

__version__ = "1.2.0"

# Trade models
from .trade import Trade, TradeType, TradeStatus

# Portfolio models
from .portfolio import (
    PortfolioType, AggregationLevel, PortfolioSummary,
    Portfolio, PortfolioSnapshot
)

# Counterparty models
from .counterparty import Counterparty, NettingSet, CollateralAgreement

# Curve models
from .curve import Curve, CurveType, YieldCurve, CreditCurve, VolatilitySurface

# Market data models
from .market_data import MarketData, MarketDataSnapshot, Quote

# Product models
from .products import (
    PaymentFrequency, OptionType, OptionStyle, AssetClass,
    Product,
    InterestRateSwap, OvernightIndexSwap, ForwardRateAgreement,
    InterestRateCap, InterestRateFloor, Swaption,
    FXForward, FXSwap, FXOption, NonDeliverableForward,
    CreditDefaultSwap, CDSIndex, TotalReturnSwap,
    EquityOption, EquitySwap, VarianceSwap,
    CommoditySwap, CommodityForward,
    CrossCurrencySwap, Repo,
    Bond, FloatingRateNote,
)

# Scenario models
from .scenario import (
    ScenarioType, ShockType,
    RiskFactorShock, CurveShock,
    Scenario, ScenarioSet,
    SimulationPath, MonteCarloScenarioSet,
    REGULATORY_SCENARIOS,
)

# Exposure models
from .exposure import (
    ExposureType, ExposureMethod,
    ExposureProfile, ExposureResult,
    SACCRResult, NettingSetExposure,
)

# Rating models
from .rating import (
    RatingAgency, RatingScale,
    RATING_PD_MAP, RATING_SCORE_MAP,
    CreditRating, RatingHistory,
    TransitionMatrix, create_default_transition_matrix,
)

# Factory
from .factory import ModelFactory

__all__ = [
    "__version__",
    
    # Trade
    "Trade", "TradeType", "TradeStatus",
    
    # Portfolio
    "PortfolioType", "AggregationLevel", "PortfolioSummary",
    "Portfolio", "PortfolioSnapshot",
    
    # Counterparty
    "Counterparty", "NettingSet", "CollateralAgreement",
    
    # Curves
    "Curve", "CurveType", "YieldCurve", "CreditCurve", "VolatilitySurface",
    
    # Market Data
    "MarketData", "MarketDataSnapshot", "Quote",
    
    # Product Enums
    "PaymentFrequency", "OptionType", "OptionStyle", "AssetClass",
    
    # Products (27)
    "Product",
    "InterestRateSwap", "OvernightIndexSwap", "ForwardRateAgreement",
    "InterestRateCap", "InterestRateFloor", "Swaption",
    "FXForward", "FXSwap", "FXOption", "NonDeliverableForward",
    "CreditDefaultSwap", "CDSIndex", "TotalReturnSwap",
    "EquityOption", "EquitySwap", "VarianceSwap",
    "CommoditySwap", "CommodityForward",
    "CrossCurrencySwap", "Repo",
    "Bond", "FloatingRateNote",
    
    # Scenario
    "ScenarioType", "ShockType",
    "RiskFactorShock", "CurveShock",
    "Scenario", "ScenarioSet",
    "SimulationPath", "MonteCarloScenarioSet",
    "REGULATORY_SCENARIOS",
    
    # Exposure
    "ExposureType", "ExposureMethod",
    "ExposureProfile", "ExposureResult",
    "SACCRResult", "NettingSetExposure",
    
    # Rating
    "RatingAgency", "RatingScale",
    "RATING_PD_MAP", "RATING_SCORE_MAP",
    "CreditRating", "RatingHistory",
    "TransitionMatrix", "create_default_transition_matrix",
    
    # Factory
    "ModelFactory",
]
