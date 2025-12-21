# CCR Analytics Engine v1.2.0

## Comprehensive Counterparty Credit Risk Analytics Platform

A professional-grade Python library for counterparty credit risk (CCR) analytics, providing complete implementations of exposure calculations, valuation adjustments, and regulatory capital metrics.

---

## 🚀 Features

### Products (80+ Implementations)
| Category | Products |
|----------|----------|
| **Interest Rate** | IRS, OIS, FRA, Cap, Floor, Swaption, Basis Swap |
| **FX** | Forward, Swap, Option, Barrier, NDF, Digital |
| **Credit** | CDS, CDS Index, TRS, Credit Linked Note |
| **Equity** | Swap, Option, Forward, Variance Swap, Dividend Swap |
| **Commodity** | Swap, Option, Forward |
| **Cross-Currency** | XCCY Swap, Basis Swap, MTM Swap |
| **Repo** | Repo, Reverse Repo, Securities Lending, Buy/Sell Back |
| **Money Market** | CD, BA, Eurodollar, Fed Funds, MMF, Time Deposit |
| **Stocks** | Common, ADR, GDR, Preferred, Warrant, ETF, Mutual Fund |
| **Alternatives** | Crypto (Spot/Future/Perpetual), REIT, Carbon, PE, HF |
| **Futures** | Index, IR, Bond, VIX, Single Stock |
| **Fixed Income** | Treasury, Gilts, Bunds, MBS, ABS, CDO, CLO (20+ types) |

### Calculators (25+ Types)
| Category | Calculators |
|----------|-------------|
| **Credit Risk** | PD, LGD, EAD, Expected Loss |
| **Exposure** | CE, PFE, EE, EEE, Peak, Stressed |
| **Valuation Adjustments** | CVA, DVA, FVA, KVA, MVA, ColVA |
| **Capital** | Economic Capital, RAROC |
| **Margin** | Initial Margin (SIMM) |
| **Regulatory** | SA-CCR |

### Models (55+ Types)
- **Trade & Portfolio**: Trade, Portfolio, Netting Set
- **Counterparty**: Counterparty, Collateral Agreement
- **Market Data**: Curves, Surfaces, Snapshots
- **Scenario**: Stress Testing, Monte Carlo
- **Exposure**: Profiles, SA-CCR Results
- **Rating**: Credit Ratings, Transition Matrices

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-repo/ccranalytics.git
cd ccranalytics

# Install dependencies
pip install -r requirements.txt

# Optional: Install QuantLib for high-performance calculations
pip install QuantLib-Python
```

---

## 🔧 Quick Start

### Calculate CVA
```python
from calculator.python import CVACalculator, CVAInput

cva_calc = CVACalculator()
result = cva_calc.calculate(CVAInput(
    exposure_profile=[100, 120, 110, 90, 70],
    time_grid=[0.0, 0.25, 0.5, 0.75, 1.0],
    pd_curve={0.25: 0.01, 0.5: 0.015, 0.75: 0.02, 1.0: 0.025},
    lgd=0.45
))
print(f"CVA: ${result.cva:,.2f}")
```

### Create a Portfolio
```python
from models import Portfolio, InterestRateSwap
from datetime import date

portfolio = Portfolio(name="Trading Book")
swap = InterestRateSwap(
    notional=10_000_000,
    fixed_rate=0.05,
    effective_date=date(2024, 1, 1),
    maturity_date=date(2029, 1, 1)
)
portfolio.add_trade(swap)
summary = portfolio.calculate_summary()
```

### Calculate SA-CCR EAD
```python
from calculator.python import SACCRCalculator, SACCRInput

saccr = SACCRCalculator()
result = saccr.calculate(SACCRInput(
    netting_set_id="NS-001",
    trades=[{"asset_class": "interest_rate", "notional": 1e8, "maturity": 5.0}],
    is_margined=True
))
print(f"EAD: ${result.ead:,.2f}")
```

---

## 📁 Project Structure

```
ccranalytics/
├── calculator/           # Risk calculators
│   ├── python/          # Pure Python implementations (12 calculators)
│   └── qlib/            # QuantLib implementations (12 calculators)
├── products/            # Financial products
│   ├── python/          # Pure Python (80 products in 12 categories)
│   └── qlib/            # QuantLib (13 products)
├── models/              # Domain models
│   ├── trade.py         # Trade models
│   ├── portfolio.py     # Portfolio models
│   ├── scenario.py      # Stress testing
│   ├── exposure.py      # Exposure results
│   └── rating.py        # Credit ratings
├── core/                # Core utilities
├── engine/              # CCR Engine
├── mathlib/             # Mathematical library
├── data/                # Data generation
├── config/              # Configuration
└── docs/                # Documentation (80+ product docs)
```

---

## 📊 Calculators Summary

### Credit Risk Calculators
| Calculator | Description |
|------------|-------------|
| `PDCalculator` | Probability of Default |
| `LGDCalculator` | Loss Given Default |
| `EADCalculator` | Exposure at Default |
| `ExpectedLossCalculator` | Expected Loss = PD × LGD × EAD |

### Exposure Calculators
| Calculator | Description |
|------------|-------------|
| `CurrentExposureCalculator` | Current mark-to-market exposure |
| `PFECalculator` | Potential Future Exposure |
| `ExpectedExposureCalculator` | Expected Exposure profile |
| `EffectiveExpectedExposureCalculator` | Non-decreasing EE |
| `StressedExposureCalculator` | Stressed market scenarios |
| `PeakExposureCalculator` | Maximum exposure |

### Valuation Adjustment Calculators
| Calculator | Description |
|------------|-------------|
| `CVACalculator` | Credit Valuation Adjustment |
| `DVACalculator` | Debit Valuation Adjustment |
| `FVACalculator` | Funding Valuation Adjustment |
| `KVACalculator` | Capital Valuation Adjustment |
| `MVACalculator` | Margin Valuation Adjustment |

### Capital & Regulatory Calculators
| Calculator | Description |
|------------|-------------|
| `EconomicCapitalCalculator` | EC under various models |
| `RAROCCalculator` | Risk-Adjusted Return on Capital |
| `InitialMarginCalculator` | SIMM-based IM |
| `SACCRCalculator` | SA-CCR per Basel III/IV |

---

## 📈 Performance

- **Pure Python**: Optimized NumPy-based calculations
- **QuantLib**: High-performance C++ backend
- **Parallel Processing**: Multi-threaded execution support
- **Memory Efficient**: Streaming calculations for large portfolios

---

## 📄 License

Copyright © 2025-2030, All Rights Reserved  
Ashutosh Sinha | Email: ajsinha@gmail.com

**Legal Notice**: This software is proprietary and confidential. Unauthorized copying, distribution, modification, or use is strictly prohibited.

**Patent Pending**: Certain architectural patterns and implementations may be subject to patent applications.

---

## 🔖 Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.2.0 | Dec 2025 | Added XVA calculators, SA-CCR, enhanced models |
| v1.1.1 | Dec 2025 | Source refactoring, 80 individual product files |
| v1.1.0 | Dec 2025 | Expanded to 150+ products, documentation |
| v1.0.0 | Dec 2025 | Initial release |
