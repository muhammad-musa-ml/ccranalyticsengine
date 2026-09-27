# SA-CCR formula audit: simplified calculator

The original `SACCRCalculator` could not be instantiated because it did not
implement two abstract methods and called `BaseCalculator` with unsupported
keyword arguments. The calculator now runs through the existing direct-result
API and records calls through the base class.

Three numerical corrections follow the Basel Framework's CRE52:

| Component | Original implementation | Corrected implementation | Source |
|---|---|---|---|
| Margined replacement cost | Sum of two floored terms; VM absent from `V-C` | `max(V-C, TH+MTA-NICA, 0)` with `C=NICA+VM` | CRE52.18 |
| PFE multiplier | Used floored RC minus NICA | Uses signed `V-C`, including VM | CRE52.23 |
| Maturity factor | Omitted the 1.5 margined factor and 10-day unmargined floor | `1.5 sqrt(MPOR/250)` with a 10-business-day minimum for bilateral daily margin; `sqrt(min(max(M,10/250),1))` without margin | CRE52.48 and CRE52.53 |

`SACCRInput.collateral` is interpreted as signed **net independent collateral
amount** (NICA); `variation_margin` is signed net VM (positive when held,
negative when posted). Amounts must already reflect applicable haircuts. The
`margin_period_of_risk` input assumes a non-centrally-cleared, daily-margined
netting set; other margin arrangements need their own MPOR floor.

## Reproduce

From the repository root:

```bash
python -m unittest discover -s tests -p 'test_saccr_regression.py' -v
python -m scripts.benchmark_saccr
```

The benchmark writes [`saccr_results.csv`](../evidence/saccr_results.csv)
and [`saccr_error.svg`](../evidence/saccr_error.svg). It uses deterministic
toy FX netting sets and compares the old formulas (transcribed in the
benchmark), the corrected code, and independent scalar formulas from CRE52.
The graph plots absolute error. A dot on the axis marks zero error, since a
zero-height bar would be invisible.
These numbers measure **formula error**. They do not measure runtime speed or
production capital accuracy. The correction can increase or decrease EAD.

## Remaining scope

The add-on calculation is still a simplified trade-level sum. It does not
implement all Basel hedging sets, signed position offsetting, asset-class
correlations, option supervisory delta, or special MPOR cases. A result from
this module should not be presented as a complete regulatory SA-CCR exposure
until those rules have been implemented and independently validated.

Primary source: [BIS Basel Framework, CRE52](https://www.bis.org/committees/bcbs/basel-framework/standard/cre/52/inforce/2019-12-15/published/2020-06-05).
