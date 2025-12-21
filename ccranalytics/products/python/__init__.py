"""
CCR Analytics Engine - Python Products v1.2.0
==============================================

Pure Python implementations of 80+ financial products.

Copyright © 2025-2030, All Rights Reserved
Ashutosh Sinha | Email: ajsinha@gmail.com
"""

__version__ = "1.2.0"

# Interest Rate (7)
from .interest_rate import (
    InterestRateSwap, IRSLeg, OvernightIndexSwap, ForwardRateAgreement,
    InterestRateCap, InterestRateFloor, Swaption, BasisSwap
)

# FX (6)
from .fx import (
    FXForward, FXSwap, FXOption, FXBarrierOption, 
    NonDeliverableForward, FXDigitalOption
)

# Credit (4)
from .credit import (
    CreditDefaultSwap, CDSIndex, TotalReturnSwap, CreditLinkedNote
)

# Equity Derivatives (5)
from .equity import (
    EquitySwap, EquityOption, EquityForward, VarianceSwap, DividendSwap
)

# Commodity (3)
from .commodity import CommoditySwap, CommodityOption, CommodityForward

# Cross-Currency (3)
from .cross_currency import (
    CrossCurrencySwap, CrossCurrencyBasisSwap, MTMCrossCurrencySwap
)

# Repo (4)
from .repo import Repo, ReverseRepo, SecuritiesLending, BuySellBack

# Money Market (7)
from .money_market import (
    CertificateOfDeposit, BankersAcceptance, EurodollarDeposit,
    FederalFunds, MoneyMarketFund, TimeDeposit, DiscountNote
)

# Stocks (8)
from .stocks import (
    CommonStock, ADR, GDR, PreferredStock, Warrant, ETF, MutualFund, IndexPosition
)

# Alternatives (8)
from .alternatives import (
    CryptoSpot, CryptoFuture, CryptoPerpetual, REIT,
    CarbonCredit, CarbonFuture, PrivateEquityInterest, HedgeFundInterest
)

# Futures (5)
from .futures import (
    IndexFuture, InterestRateFuture, BondFuture, VIXFuture, SingleStockFuture
)

# Fixed Income (20)
from .fixed_income import (
    TreasuryBill, TreasuryNote, TreasuryBond, TIPS,
    UKGilt, GermanBund, JGB, FrenchOAT,
    MunicipalBond, AgencyBond, CorporateBond,
    FloatingRateNote, ConvertibleBond, CommercialPaper, MediumTermNote,
    MBS, ABS, CDO, CLO, ZeroCouponBond
)

__all__ = [
    # Interest Rate (8)
    "InterestRateSwap", "IRSLeg", "OvernightIndexSwap", "ForwardRateAgreement",
    "InterestRateCap", "InterestRateFloor", "Swaption", "BasisSwap",
    # FX (6)
    "FXForward", "FXSwap", "FXOption", "FXBarrierOption", 
    "NonDeliverableForward", "FXDigitalOption",
    # Credit (4)
    "CreditDefaultSwap", "CDSIndex", "TotalReturnSwap", "CreditLinkedNote",
    # Equity (5)
    "EquitySwap", "EquityOption", "EquityForward", "VarianceSwap", "DividendSwap",
    # Commodity (3)
    "CommoditySwap", "CommodityOption", "CommodityForward",
    # Cross-Currency (3)
    "CrossCurrencySwap", "CrossCurrencyBasisSwap", "MTMCrossCurrencySwap",
    # Repo (4)
    "Repo", "ReverseRepo", "SecuritiesLending", "BuySellBack",
    # Money Market (7)
    "CertificateOfDeposit", "BankersAcceptance", "EurodollarDeposit",
    "FederalFunds", "MoneyMarketFund", "TimeDeposit", "DiscountNote",
    # Stocks (8)
    "CommonStock", "ADR", "GDR", "PreferredStock", 
    "Warrant", "ETF", "MutualFund", "IndexPosition",
    # Alternatives (8)
    "CryptoSpot", "CryptoFuture", "CryptoPerpetual", "REIT",
    "CarbonCredit", "CarbonFuture", "PrivateEquityInterest", "HedgeFundInterest",
    # Futures (5)
    "IndexFuture", "InterestRateFuture", "BondFuture", "VIXFuture", "SingleStockFuture",
    # Fixed Income (20)
    "TreasuryBill", "TreasuryNote", "TreasuryBond", "TIPS",
    "UKGilt", "GermanBund", "JGB", "FrenchOAT",
    "MunicipalBond", "AgencyBond", "CorporateBond",
    "FloatingRateNote", "ConvertibleBond", "CommercialPaper", "MediumTermNote",
    "MBS", "ABS", "CDO", "CLO", "ZeroCouponBond",
]
