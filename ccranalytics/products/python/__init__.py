"""
CCR Analytics Engine - Python Products v1.3.0
==============================================

Copyright © 2025-2030, All Rights Reserved
Ashutosh Sinha | Email: ajsinha@gmail.com

Legal Notice: This module and the associated software architecture are proprietary 
and confidential. Unauthorized copying, distribution, modification, or use is 
strictly prohibited without explicit written permission from the copyright holder.

---

Pure Python implementations of 81 financial products across 12 asset classes.

Product Categories:
- Interest Rate (8): IRS, OIS, FRA, Cap, Floor, Swaption, Basis Swap, IRSLeg
- FX (6): Forward, Swap, Option, Barrier, NDF, Digital
- Credit (4): CDS, CDS Index, TRS, Credit Linked Note
- Equity (5): Swap, Option, Forward, Variance Swap, Dividend Swap
- Commodity (3): Swap, Option, Forward
- Cross-Currency (3): XCCY Swap, Basis Swap, MTM Swap
- Repo (4): Repo, Reverse Repo, Securities Lending, Buy/Sell Back
- Money Market (7): CD, BA, Eurodollar, Fed Funds, MMF, Time Deposit, Discount Note
- Stocks (8): Common, ADR, GDR, Preferred, Warrant, ETF, Mutual Fund, Index Position
- Alternatives (8): Crypto (Spot/Future/Perpetual), REIT, Carbon, PE, Hedge Fund
- Futures (5): Index, IR, Bond, VIX, Single Stock
- Fixed Income (20): Treasuries, Gilts, Bunds, JGB, OAT, Muni, Agency, Corporate,
                     FRN, Convertible, CP, MTN, MBS, ABS, CDO, CLO, Zero Coupon
"""

__version__ = "1.3.0"

# Interest Rate (8)
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
    "__version__",
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
