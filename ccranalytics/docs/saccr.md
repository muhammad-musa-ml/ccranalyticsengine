# SA-CCR (Standardized Approach for Counterparty Credit Risk) v1.1.0

## Overview

The Standardized Approach for Measuring Counterparty Credit Risk Exposures (SA-CCR) is the Basel III regulatory framework for calculating Exposure at Default (EAD) for derivative transactions. SA-CCR replaced the prior Current Exposure Method (CEM) and Standardized Method (SM).

**Effective Date:** January 1, 2022 (Basel Committee timeline)

**Reference Documents:**
- BCBS 279 (March 2014)
- BCBS 424 (December 2017)
- CRR2/CRD5 (EU implementation)

---

## SA-CCR Formula

### Basic EAD Formula

```
EAD = α × (RC + PFE)
```

Where:
- **α (Alpha)** = 1.4 (regulatory multiplier)
- **RC** = Replacement Cost
- **PFE** = Potential Future Exposure

---

## Replacement Cost (RC)

### Unmargined Transactions

```
RC = max(V - C, 0)
```

Where:
- V = Current mark-to-market value (positive = asset)
- C = Net collateral held (positive = received)

### Margined Transactions

```
RC = max(V - C, TH + MTA - NICA, 0)
```

Where:
- TH = Threshold
- MTA = Minimum Transfer Amount
- NICA = Net Independent Collateral Amount

---

## Potential Future Exposure (PFE)

### PFE Formula

```
PFE = multiplier × AddOnAggregate
```

### Multiplier

```
multiplier = min(1, floor + (1 - floor) × exp((V - C) / (2 × (1 - floor) × AddOnAggregate)))
```

Where:
- floor = 0.05 (5%)

**Purpose:** Reduces PFE when portfolio has negative value (out-of-the-money)

### Aggregate Add-On

```
AddOnAggregate = Σ AddOn(asset_class)
```

For each asset class: Interest Rate, FX, Credit, Equity, Commodity

---

## Asset Class Add-On Calculations

### Interest Rate

```
AddOn(IR) = Σ(currency) [|Σ(maturity_bucket) (SF × d × EffectiveNotional × MF)|]
```

**Supervisory Factor (SF):** 0.50%

**Maturity Buckets:**
| Bucket | Tenor |
|--------|-------|
| 1 | 0-1 year |
| 2 | 1-5 years |
| 3 | > 5 years |

**Correlation within currency:** ρ = 0.7 (between buckets)

### FX

```
AddOn(FX) = Σ(currency_pair) |SF × d × EffectiveNotional × MF|
```

**Supervisory Factor (SF):** 4.0%

### Credit

**Single Name:**
| Rating | SF |
|--------|-----|
| AAA-AA | 0.38% |
| A | 0.42% |
| BBB | 0.54% |
| BB | 1.06% |
| B | 1.06% |
| CCC | 6.00% |

**Index:**
| Type | SF |
|------|-----|
| Investment Grade | 0.38% |
| Sub-Investment Grade | 1.06% |

**Correlation:**
- Same entity: 100%
- Different entities (same index family): 80%
- Different index families: 50%

### Equity

| Type | SF |
|------|-----|
| Single Name | 32% |
| Index | 20% |

**Correlation:**
- Same entity: 100%
- Different entities: 50%

### Commodity

| Type | SF |
|------|-----|
| Electricity | 40% |
| Oil/Gas | 18% |
| Metals | 18% |
| Agricultural | 18% |
| Other | 18% |

---

## Effective Notional Calculation

### Linear Products

```
EffectiveNotional = Notional × SupervisoryDuration
```

**Supervisory Duration:**
```
SD = (exp(-0.05 × S) - exp(-0.05 × E)) / 0.05
```

Where:
- S = Start date (years)
- E = End date (years)

### Options

```
EffectiveNotional = δ × Notional × SupervisoryDuration
```

**Delta Calculation:**
```
δ = N((ln(P/K) + 0.5 × σ² × T) / (σ × √T))  [Call]
δ = N((ln(P/K) + 0.5 × σ² × T) / (σ × √T)) - 1  [Put]
```

**Supervisory Volatility (σ):**
| Asset Class | Volatility |
|-------------|------------|
| Interest Rate | 50% |
| FX | 15% |
| Credit | 100% |
| Equity | 120% |
| Commodity | 150% |

---

## Maturity Factor (MF)

### Unmargined Transactions

```
MF = √(min(M, 1))
```

Where M = remaining maturity in years (floored at 10 business days)

### Margined Transactions

```
MF = 1.5 × √(MPOR/250)
```

**Margin Period of Risk (MPOR):**
| Scenario | MPOR |
|----------|------|
| Bilateral | 10 business days |
| CCP | 5 business days |
| Disputed trades | 20+ business days |

---

## Netting and Hedging Sets

### Netting Set Requirements

1. Legally enforceable master netting agreement
2. Same counterparty
3. Same legal entity

### Hedging Sets

**Interest Rate:** By currency
**FX:** By currency pair
**Credit:** By reference entity/index
**Equity:** By reference entity/index
**Commodity:** By commodity type

### Hedging Set Aggregation

Within hedging set (full offsetting):
```
AddOn(HS) = |Σ (δ × d × EffectiveNotional × MF)|
```

Between hedging sets (partial offsetting based on correlation):
```
AddOn(AC) = √(Σ AddOn(HS)² + Σ Σ ρ × AddOn(HSi) × AddOn(HSj))
```

---

## Special Cases

### Cross-Currency Swaps

- Interest rate add-on for BOTH legs (in respective currencies)
- FX add-on for notional exchange

### CDO/Basket Credit Derivatives

```
EffectiveNotional = Notional × (D - A)
```

Where:
- A = Attachment point
- D = Detachment point

### Basis Swaps

- Each leg generates separate add-on
- Different hedging sets within same currency

### Forward-Starting Trades

- Use trade start date, not valuation date
- Full maturity for supervisory duration

---

## Implementation in CCR Analytics Engine

### Code Example

```python
from products.base import SACCRParameters

# Get supervisory factor
sf_ir = SACCRParameters.get_supervisory_factor(AssetClass.INTEREST_RATE)
sf_fx = SACCRParameters.get_supervisory_factor(AssetClass.FX)
sf_credit = SACCRParameters.get_supervisory_factor(AssetClass.CREDIT, "BBB")

# Calculate maturity factor
mf = SACCRParameters.calculate_maturity_factor(remaining_maturity)

# Full SA-CCR calculation via product
result = product.calculate_saccr(market_data)
print(f"Replacement Cost: {result.replacement_cost:,.2f}")
print(f"PFE Add-On: {result.pfe_add_on:,.2f}")
print(f"EAD: {result.ead:,.2f}")
```

### SACCRExposure Result

```python
@dataclass
class SACCRExposure:
    replacement_cost: float          # RC
    pfe_add_on: float               # PFE
    ead: float                      # Final EAD = 1.4 × (RC + PFE)
    asset_class: AssetClass
    hedging_set_contributions: Dict[str, float]
    metadata: Dict[str, Any]
```

---

## Supervisory Parameters Reference

### Complete Supervisory Factor Table

| Asset Class | Sub-Class | SF |
|-------------|-----------|-----|
| Interest Rate | All | 0.50% |
| FX | All | 4.0% |
| Credit - Single | AAA-AA | 0.38% |
| Credit - Single | A | 0.42% |
| Credit - Single | BBB | 0.54% |
| Credit - Single | BB | 1.06% |
| Credit - Single | B | 1.06% |
| Credit - Single | CCC | 6.00% |
| Credit - Index | IG | 0.38% |
| Credit - Index | SG | 1.06% |
| Equity - Single | All | 32% |
| Equity - Index | All | 20% |
| Commodity | Electricity | 40% |
| Commodity | Oil/Gas | 18% |
| Commodity | Metals | 18% |
| Commodity | Agricultural | 18% |
| Commodity | Other | 18% |

### Supervisory Correlation Parameters

| Asset Class | Within Entity | Cross Entity |
|-------------|---------------|--------------|
| Credit | 100% | 50-80% |
| Equity | 100% | 50% |
| Commodity | 100% | 40% |
| IR (same ccy) | 70% (buckets) | - |
| IR (diff ccy) | 50% | - |

---

## Comparison with Prior Methods

| Feature | CEM | SM | SA-CCR |
|---------|-----|-----|--------|
| Netting Recognition | Limited | Partial | Full |
| Collateral Treatment | Simple | Simple | Comprehensive |
| Optionality | None | None | Delta |
| Volatility Scaling | No | No | Yes |
| Hedging | None | Basic | Full |
| Add-On Factors | Maturity bands | Asset class | Granular |

---

## Regulatory Capital Calculation

```
RWA_CCR = EAD × RW(counterparty)
```

**Risk Weights by Counterparty:**
| Type | RW (SA) |
|------|---------|
| Sovereigns (AAA) | 0% |
| Banks (A) | 50% |
| Corporates (BBB) | 100% |
| CCP (Qualifying) | 2% |
| CCP (Non-Qualifying) | 100%+ |

---

## Best Practices

1. **Data Quality**
   - Accurate notionals and maturity dates
   - Proper product classification
   - Correct hedging set assignment

2. **Netting Set Management**
   - Legal opinion on enforceability
   - Proper CSA mapping
   - Margin agreement terms

3. **Model Validation**
   - Benchmark against regulatory examples
   - Sensitivity testing
   - Regular recalibration

4. **Reporting**
   - Asset class breakdown
   - Hedging set detail
   - RC vs PFE composition

---

## References

- Basel Committee on Banking Supervision (2014). "The standardised approach for measuring counterparty credit risk exposures." BCBS 279.
- European Banking Authority (2019). "Final Report on SA-CCR Implementation."
- Federal Reserve (2020). "SA-CCR Implementation Guidelines."

---

Copyright © 2025-2030, All Rights Reserved  
Ashutosh Sinha | Email: ajsinha@gmail.com

Legal Notice: This documentation and the associated software architecture are proprietary
and confidential. Unauthorized copying, distribution, modification, or use is strictly
prohibited without explicit written permission from the copyright holder.

Patent Pending: Certain architectural patterns and implementations described in this
documentation may be subject to patent applications.
