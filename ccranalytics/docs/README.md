# CCR Analytics Engine Documentation

## Overview

Complete documentation for the CCR Analytics Engine v1.1.0, covering calculators, metrics, and trading products.

---

## Calculators

Individual calculator documentation with formulas, inputs, and usage examples.

| Calculator | Description | File |
|------------|-------------|------|
| [PD Calculator](calculators/pd_calculator.md) | Probability of Default estimation | `pd_calculator.md` |
| [LGD Calculator](calculators/lgd_calculator.md) | Loss Given Default calculation | `lgd_calculator.md` |
| [EAD Calculator](calculators/ead_calculator.md) | Exposure at Default computation | `ead_calculator.md` |
| [EL Calculator](calculators/el_calculator.md) | Expected Loss calculation | `el_calculator.md` |
| [CE Calculator](calculators/ce_calculator.md) | Current Exposure measurement | `ce_calculator.md` |
| [PFE Calculator](calculators/pfe_calculator.md) | Potential Future Exposure | `pfe_calculator.md` |
| [EE Calculator](calculators/ee_calculator.md) | Expected Exposure profiles | `ee_calculator.md` |
| [CVA Calculator](calculators/cva_calculator.md) | Credit Valuation Adjustment | `cva_calculator.md` |
| [EC Calculator](calculators/ec_calculator.md) | Economic Capital estimation | `ec_calculator.md` |
| [IM Calculator](calculators/im_calculator.md) | Initial Margin calculation | `im_calculator.md` |
| [Stress Calculators](calculators/stress_calculators.md) | Stress testing tools | `stress_calculators.md` |

---

## Metrics

Documentation for key CCR metrics and their interpretation.

| Metric | Description | File |
|--------|-------------|------|
| [Expected Loss](metrics/expected_loss.md) | Average anticipated credit loss | `expected_loss.md` |
| [CVA](metrics/cva.md) | Market value of counterparty risk | `cva.md` |
| [PFE](metrics/pfe.md) | Maximum expected exposure at confidence level | `pfe.md` |
| [Economic Capital](metrics/economic_capital.md) | Capital for unexpected losses | `economic_capital.md` |
| [EPE](metrics/epe.md) | Expected Positive Exposure | `epe.md` |

---

## Trading Products

Product-specific documentation including valuation and CCR characteristics.

| Product | Description | File |
|---------|-------------|------|
| [Interest Rate Swap](products/interest_rate_swap.md) | Fixed-floating rate exchange | `interest_rate_swap.md` |
| [FX Forward](products/fx_forward.md) | Forward currency exchange | `fx_forward.md` |
| [Credit Default Swap](products/credit_default_swap.md) | Credit protection instrument | `credit_default_swap.md` |
| [Cross-Currency Swap](products/cross_currency_swap.md) | Multi-currency swap | `cross_currency_swap.md` |
| [Equity Options](products/equity_options.md) | Options on equity underlyings | `equity_options.md` |

---

## Quick Reference

### Calculator Input Requirements

| Calculator | Required Inputs |
|------------|-----------------|
| PD | `credit_rating` or `asset_value, debt_value, asset_volatility` |
| LGD | `seniority` or `collateral_value, exposure_value` |
| EAD | `current_exposure, notional` |
| EL | `pd, lgd, ead` |
| CE | `mark_to_market` |
| PFE | `current_mtm, notional, remaining_maturity, volatility` |
| EE | `current_mtm, notional, remaining_maturity, volatility` |
| CVA | `ee_profile, time_grid, credit_spread` |
| EC | `exposures, pds, lgds` |
| IM | `notional, product_type, remaining_maturity` |

### Common Product Types

```python
product_types = [
    "irs",           # Interest Rate Swap
    "fx_forward",    # FX Forward
    "fx_option",     # FX Option
    "cds",           # Credit Default Swap
    "xccy_swap",     # Cross-Currency Swap
    "equity_option", # Equity Option
    "commodity",     # Commodity Derivative
    "repo",          # Repurchase Agreement
]
```

### Regulatory References

| Framework | Key Documents |
|-----------|---------------|
| Basel III | CRR/CRD IV, SA-CCR, CVA Capital |
| EMIR | Margin Requirements, Clearing |
| Dodd-Frank | Swap Dealer Rules, Clearing |
| IFRS 9 | Expected Credit Loss Accounting |

---

## Architecture

For system architecture documentation, see:
- [Architecture Overview](architecture.md)
- [Quick Start Guide](quickstart.md)
- [Mathematical Formulas](mathematical_formulas.md)

---

## Support

For questions or issues:
- Email: ajsinha@gmail.com
- Copyright © 2025-2030, All Rights Reserved
