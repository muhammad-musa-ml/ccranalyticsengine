# Calculators Documentation v1.2.0

## Overview

The Calculator module provides 25+ risk calculators with both Pure Python and QuantLib implementations.

## Calculator Categories

### Credit Risk Calculators

| Calculator | File | Description |
|------------|------|-------------|
| PD | [pd_calculator.md](pd_calculator.md) | Probability of Default |
| LGD | [lgd_calculator.md](lgd_calculator.md) | Loss Given Default |
| EAD | [ead_calculator.md](ead_calculator.md) | Exposure at Default |
| EL | [el_calculator.md](el_calculator.md) | Expected Loss |

### Exposure Calculators

| Calculator | File | Description |
|------------|------|-------------|
| CE | [ce_calculator.md](ce_calculator.md) | Current Exposure |
| PFE | [pfe_calculator.md](pfe_calculator.md) | Potential Future Exposure |
| EE | [ee_calculator.md](ee_calculator.md) | Expected Exposure |
| Stress | [stress_calculators.md](stress_calculators.md) | Stressed/Peak Exposure |

### Valuation Adjustment Calculators (XVA)

| Calculator | File | Description |
|------------|------|-------------|
| CVA | [cva_calculator.md](cva_calculator.md) | Credit Valuation Adjustment |
| DVA | [dva_calculator.md](dva_calculator.md) | Debit Valuation Adjustment |
| FVA | [fva_calculator.md](fva_calculator.md) | Funding Valuation Adjustment |
| KVA | [kva_calculator.md](kva_calculator.md) | Capital Valuation Adjustment |
| MVA | [mva_calculator.md](mva_calculator.md) | Margin Valuation Adjustment |

### Capital & Performance Calculators

| Calculator | File | Description |
|------------|------|-------------|
| EC | [ec_calculator.md](ec_calculator.md) | Economic Capital |
| RAROC | [raroc_calculator.md](raroc_calculator.md) | Risk-Adjusted Return on Capital |
| IM | [im_calculator.md](im_calculator.md) | Initial Margin (SIMM) |

### Regulatory Calculators

| Calculator | File | Description |
|------------|------|-------------|
| SA-CCR | [saccr_calculator.md](saccr_calculator.md) | Standardised Approach CCR |

## Quick Reference

### Credit Risk
```python
from calculator.python import PDCalculator, LGDCalculator, EADCalculator
```

### Exposure
```python
from calculator.python import CurrentExposureCalculator, PFECalculator, ExpectedExposureCalculator
```

### XVA
```python
from calculator.python import CVACalculator, DVACalculator, FVACalculator, KVACalculator, MVACalculator
```

### Regulatory
```python
from calculator.python import SACCRCalculator, InitialMarginCalculator
```

## Implementation Types

| Type | Module | Description |
|------|--------|-------------|
| Python | `calculator.python` | Pure Python with NumPy |
| QuantLib | `calculator.qlib` | QuantLib C++ backend |

## Calculator Relationships

```
┌─────────────────────────────────────────────────┐
│                  Input Data                      │
│   (Trades, Market Data, Counterparty Info)       │
└─────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│              Exposure Calculators                │
│   CE, EE, PFE, Stressed Exposure                 │
└─────────────────────────────────────────────────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Credit Risk  │ │     XVA      │ │  Regulatory  │
│  PD, LGD,    │ │  CVA, DVA,   │ │   SA-CCR,    │
│  EAD, EL     │ │  FVA, KVA,   │ │     IM       │
│              │ │     MVA      │ │              │
└──────────────┘ └──────────────┘ └──────────────┘
          │             │             │
          └─────────────┼─────────────┘
                        ▼
┌─────────────────────────────────────────────────┐
│              Capital Calculators                 │
│           EC, RAROC, Capital Charge              │
└─────────────────────────────────────────────────┘
```

---

Copyright © 2025-2030, All Rights Reserved | Ashutosh Sinha
