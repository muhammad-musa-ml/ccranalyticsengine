"""
CCR Analytics Engine - Products Module v1.2.0
==============================================

Complete product implementations for CCR Analytics Engine.

Implementations:
- Pure Python: 80+ products across all asset classes
- QuantLib: 13 high-performance products

Copyright © 2025-2030, All Rights Reserved
Ashutosh Sinha | Email: ajsinha@gmail.com
"""

__version__ = "1.2.0"

from .base import (
    BaseProduct, AssetClass, Currency,
    DayCountConvention, PaymentFrequency, BusinessDayConvention,
    OptionType, OptionStyle, BarrierType, SettlementType,
    FloatingRateIndex,
    MarketData, PricingResult, CCRExposureProfile, SACCRExposure,
    SACCRParameters, year_fraction, discount_factor
)

from .product_types import ProductType

# Import all Python products
from .python import *

# Import QuantLib products (if available)
try:
    from .qlib import (
        QUANTLIB_AVAILABLE,
        InterestRateSwapQL, SwaptionQL, InterestRateCapQL, InterestRateFloorQL,
        FXForwardQL, FXOptionQL,
        FixedRateBondQL, FloatingRateBondQL, ZeroCouponBondQL,
    )
except ImportError:
    QUANTLIB_AVAILABLE = False

__all__ = [
    # Base
    "BaseProduct", "AssetClass", "Currency", "ProductType",
    "DayCountConvention", "PaymentFrequency", "BusinessDayConvention",
    "OptionType", "OptionStyle", "BarrierType", "SettlementType",
    "FloatingRateIndex",
    "MarketData", "PricingResult", "CCRExposureProfile", "SACCRExposure",
    "SACCRParameters", "year_fraction", "discount_factor",
    # QuantLib
    "QUANTLIB_AVAILABLE",
]
