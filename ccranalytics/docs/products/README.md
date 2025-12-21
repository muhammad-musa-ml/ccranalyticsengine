# CCR Analytics Engine - Product Documentation v1.2.0

## Overview

This directory contains comprehensive documentation for all 80 products implemented in the CCR Analytics Engine. Each product document includes:

- Product description and characteristics
- Mathematical pricing framework
- Risk metrics and Greeks
- SA-CCR regulatory treatment
- CCR exposure methodology
- Implementation examples
- Market conventions

---

## Product Catalog by Asset Class

### Fixed Income (20 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Treasury Bill | `fixed_income/treasury_bill.md` | ✓ | ✓ |
| 2 | Treasury Note | `fixed_income/treasury_note.md` | ✓ | ✓ |
| 3 | Treasury Bond | `fixed_income/treasury_bond.md` | ✓ | ✓ |
| 4 | TIPS | `fixed_income/tips.md` | ✓ | ○ |
| 5 | UK Gilt | `fixed_income/uk_gilt.md` | ✓ | ✓ |
| 6 | German Bund | `fixed_income/german_bund.md` | ✓ | ✓ |
| 7 | JGB | `fixed_income/jgb.md` | ✓ | ✓ |
| 8 | French OAT | `fixed_income/french_oat.md` | ✓ | ✓ |
| 9 | Municipal Bond | `fixed_income/municipal_bond.md` | ✓ | ○ |
| 10 | Agency Bond | `fixed_income/agency_bond.md` | ✓ | ○ |
| 11 | Corporate Bond | `fixed_income/corporate_bond.md` | ✓ | ✓ |
| 12 | Floating Rate Note | `fixed_income/floating_rate_note.md` | ✓ | ✓ |
| 13 | Convertible Bond | `fixed_income/convertible_bond.md` | ✓ | ○ |
| 14 | Commercial Paper | `fixed_income/commercial_paper.md` | ✓ | ○ |
| 15 | Medium Term Note | `fixed_income/medium_term_note.md` | ✓ | ○ |
| 16 | MBS | `fixed_income/mbs.md` | ✓ | ○ |
| 17 | ABS | `fixed_income/abs.md` | ✓ | ○ |
| 18 | CDO | `fixed_income/cdo.md` | ✓ | ○ |
| 19 | CLO | `fixed_income/clo.md` | ✓ | ○ |
| 20 | Bond (Base) | `fixed_income/bond.md` | ✓ | ✓ |

### Interest Rate Derivatives (7 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Interest Rate Swap | `interest_rate/interest_rate_swap.md` | ✓ | ✓ |
| 2 | Overnight Index Swap | `interest_rate/overnight_index_swap.md` | ✓ | ✓ |
| 3 | Forward Rate Agreement | `interest_rate/forward_rate_agreement.md` | ✓ | ○ |
| 4 | Interest Rate Cap | `interest_rate/interest_rate_cap.md` | ✓ | ✓ |
| 5 | Interest Rate Floor | `interest_rate/interest_rate_floor.md` | ✓ | ✓ |
| 6 | Swaption | `interest_rate/swaption.md` | ✓ | ✓ |
| 7 | Basis Swap | `interest_rate/basis_swap.md` | ✓ | ○ |

### FX Products (6 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | FX Forward | `fx/fx_forward.md` | ✓ | ✓ |
| 2 | FX Swap | `fx/fx_swap.md` | ✓ | ○ |
| 3 | FX Option | `fx/fx_option.md` | ✓ | ✓ |
| 4 | FX Barrier Option | `fx/fx_barrier_option.md` | ✓ | ○ |
| 5 | Non-Deliverable Forward | `fx/ndf.md` | ✓ | ○ |
| 6 | FX Digital Option | `fx/fx_digital.md` | ✓ | ○ |

### Credit Derivatives (4 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Credit Default Swap | `credit/credit_default_swap.md` | ✓ | ○ |
| 2 | CDS Index | `credit/cds_index.md` | ✓ | ○ |
| 3 | Total Return Swap | `credit/total_return_swap.md` | ✓ | ○ |
| 4 | Credit Linked Note | `credit/credit_linked_note.md` | ✓ | ○ |

### Equity Derivatives (5 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Equity Swap | `equity/equity_swap.md` | ✓ | ○ |
| 2 | Equity Option | `equity/equity_option.md` | ✓ | ○ |
| 3 | Equity Forward | `equity/equity_forward.md` | ✓ | ○ |
| 4 | Variance Swap | `equity/variance_swap.md` | ✓ | ○ |
| 5 | Dividend Swap | `equity/dividend_swap.md` | ✓ | ○ |

### Commodity Derivatives (3 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Commodity Swap | `commodity/commodity_swap.md` | ✓ | ○ |
| 2 | Commodity Option | `commodity/commodity_option.md` | ✓ | ○ |
| 3 | Commodity Forward | `commodity/commodity_forward.md` | ✓ | ○ |

### Cross-Currency (3 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Cross-Currency Swap | `cross_currency/cross_currency_swap.md` | ✓ | ○ |
| 2 | Cross-Currency Basis Swap | `cross_currency/cross_currency_basis_swap.md` | ✓ | ○ |
| 3 | MTM Cross-Currency Swap | `cross_currency/mtm_cross_currency_swap.md` | ✓ | ○ |

### Securities Financing (4 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Repo | `repo/repo.md` | ✓ | ○ |
| 2 | Reverse Repo | `repo/reverse_repo.md` | ✓ | ○ |
| 3 | Securities Lending | `repo/securities_lending.md` | ✓ | ○ |
| 4 | Buy/Sell Back | `repo/buy_sell_back.md` | ✓ | ○ |

### Money Market (7 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Certificate of Deposit | `money_market/certificate_of_deposit.md` | ✓ | ○ |
| 2 | Banker's Acceptance | `money_market/bankers_acceptance.md` | ✓ | ○ |
| 3 | Eurodollar Deposit | `money_market/eurodollar_deposit.md` | ✓ | ○ |
| 4 | Federal Funds | `money_market/federal_funds.md` | ✓ | ○ |
| 5 | Money Market Fund | `money_market/money_market_fund.md` | ✓ | ○ |
| 6 | Time Deposit | `money_market/time_deposit.md` | ✓ | ○ |
| 7 | Discount Note | `money_market/discount_note.md` | ✓ | ○ |

### Stocks & ETFs (8 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Common Stock | `stocks/common_stock.md` | ✓ | ○ |
| 2 | ADR | `stocks/adr.md` | ✓ | ○ |
| 3 | GDR | `stocks/gdr.md` | ✓ | ○ |
| 4 | Preferred Stock | `stocks/preferred_stock.md` | ✓ | ○ |
| 5 | Warrant | `stocks/warrant.md` | ✓ | ○ |
| 6 | ETF | `stocks/etf.md` | ✓ | ○ |
| 7 | Mutual Fund | `stocks/mutual_fund.md` | ✓ | ○ |
| 8 | Index Position | `stocks/index_position.md` | ✓ | ○ |

### Alternative Investments (8 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Cryptocurrency Spot | `alternatives/crypto_spot.md` | ✓ | ○ |
| 2 | Cryptocurrency Future | `alternatives/crypto_future.md` | ✓ | ○ |
| 3 | Cryptocurrency Perpetual | `alternatives/crypto_perpetual.md` | ✓ | ○ |
| 4 | REIT | `alternatives/reit.md` | ✓ | ○ |
| 5 | Carbon Credit | `alternatives/carbon_credit.md` | ✓ | ○ |
| 6 | Carbon Future | `alternatives/carbon_future.md` | ✓ | ○ |
| 7 | Private Equity Interest | `alternatives/private_equity_interest.md` | ✓ | ○ |
| 8 | Hedge Fund Interest | `alternatives/hedge_fund_interest.md` | ✓ | ○ |

### Futures (5 Products)

| # | Product | File | Python | QuantLib |
|---|---------|------|--------|----------|
| 1 | Index Future | `futures/index_future.md` | ✓ | ○ |
| 2 | Interest Rate Future | `futures/interest_rate_future.md` | ✓ | ○ |
| 3 | Bond Future | `futures/bond_future.md` | ✓ | ○ |
| 4 | VIX Future | `futures/vix_future.md` | ✓ | ○ |
| 5 | Single Stock Future | `futures/single_stock_future.md` | ✓ | ○ |

---

## Implementation Summary

| Implementation | Products | Coverage |
|----------------|----------|----------|
| **Pure Python** | 80 | 100% |
| **QuantLib** | 13 | 16% |

### QuantLib Products

1. InterestRateSwapQL
2. SwaptionQL
3. InterestRateCapQL
4. InterestRateFloorQL
5. FXForwardQL
6. FXOptionQL
7. FixedRateBondQL
8. FloatingRateBondQL
9. ZeroCouponBondQL

---

## Document Standards

All product documentation follows this structure:

1. **Product Overview** - Key attributes table
2. **Description** - What the product is
3. **Mathematical Framework** - Pricing formulas
4. **Risk Metrics** - Greeks and sensitivities
5. **SA-CCR Treatment** - Regulatory capital
6. **CCR Exposure** - Credit risk methodology
7. **Implementation Example** - Code sample
8. **Market Conventions** - Trading standards
9. **Copyright Notice** - Legal information

---

Copyright © 2025-2030, All Rights Reserved  
Ashutosh Sinha | Email: ajsinha@gmail.com

Legal Notice: This documentation and the associated software architecture are proprietary
and confidential. Unauthorized copying, distribution, modification, or use is strictly
prohibited without explicit written permission from the copyright holder.
