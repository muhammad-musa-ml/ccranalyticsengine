# Models Documentation v1.2.0

## Overview

The Models module provides 55+ domain models for the CCR Analytics Engine, organized into logical categories.

## Model Categories

| Category | File | Classes | Description |
|----------|------|---------|-------------|
| Trade | [trade.md](trade.md) | 5 | Trade, TradeType, TradeStatus |
| Portfolio | [portfolio.md](portfolio.md) | 5 | Portfolio, PortfolioSummary |
| Counterparty | [counterparty.md](counterparty.md) | 8 | Counterparty, NettingSet, CSA |
| Curve | [curve.md](curve.md) | 6 | YieldCurve, CreditCurve, VolSurface |
| Market Data | [market_data.md](market_data.md) | 7 | MarketData, Quote, Snapshot |
| Products | [products.md](products.md) | 27 | All product domain models |
| Scenario | [scenario.md](scenario.md) | 8 | Scenario, ScenarioSet, MC |
| Exposure | [exposure.md](exposure.md) | 6 | ExposureProfile, SACCRResult |
| Rating | [rating.md](rating.md) | 8 | CreditRating, TransitionMatrix |

## Quick Reference

### Trade Management
```python
from models import Trade, Portfolio, NettingSet
```

### Market Data
```python
from models import YieldCurve, CreditCurve, MarketDataSnapshot
```

### Credit Risk
```python
from models import CreditRating, TransitionMatrix, ExposureResult
```

### Stress Testing
```python
from models import Scenario, ScenarioSet, MonteCarloScenarioSet
```

## Class Counts by Module

| Module | Classes | Enums | Functions |
|--------|---------|-------|-----------|
| trade | 3 | 2 | 0 |
| portfolio | 4 | 2 | 0 |
| counterparty | 3 | 2 | 0 |
| curve | 4 | 1 | 0 |
| market_data | 3 | 2 | 0 |
| products | 27 | 4 | 0 |
| scenario | 6 | 2 | 0 |
| exposure | 4 | 2 | 0 |
| rating | 4 | 2 | 1 |
| **Total** | **58** | **19** | **1** |

---

Copyright © 2025-2030, All Rights Reserved | Ashutosh Sinha
