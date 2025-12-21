# CCR Analytics Engine - Architecture Documentation

Copyright © 2025-2030, All Rights Reserved  
Ashutosh Sinha | Email: ajsinha@gmail.com

---

## Table of Contents

1. [Overview](#1-overview)
2. [System Architecture](#2-system-architecture)
3. [Module Structure](#3-module-structure)
4. [Design Patterns](#4-design-patterns)
5. [Data Flow](#5-data-flow)
6. [Threading Model](#6-threading-model)
7. [Extension Points](#7-extension-points)

---

## 1. Overview

The CCR Analytics Engine is a high-performance, multi-threaded system designed for comprehensive counterparty credit risk analytics. It provides dual implementations (pure Python and QuantLib) for all calculations, enabling performance comparison and flexibility.

### 1.1 Key Features

- **Dual Implementation**: Every calculator has both Python and QuantLib versions
- **Multi-threaded Execution**: Concurrent calculation support via ThreadPoolExecutor
- **Modular Design**: Clean separation of concerns across modules
- **Factory Pattern**: Centralized object creation and management
- **Protocol-Based Interfaces**: Type-safe abstractions using Python protocols
- **Comprehensive Metrics**: Full suite of CCR metrics (PD, LGD, EAD, CVA, PFE, etc.)
- **Stress Testing**: Historical, hypothetical, and reverse stress scenarios
- **Monte Carlo Simulation**: Multiple stochastic process implementations

### 1.2 Technology Stack

- **Language**: Python 3.9+
- **Numerical Computing**: NumPy, SciPy
- **Financial Library**: QuantLib-Python (optional)
- **Concurrency**: concurrent.futures, threading
- **Configuration**: Properties file parser
- **Logging**: Python logging with custom formatters

---

## 2. System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CCR Analytics Engine                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         Engine Module                                │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │   │
│  │  │  CCREngine  │  │ TaskQueue   │  │ThreadPool   │                 │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      Calculator Module                               │   │
│  │  ┌──────────────────────────┐  ┌──────────────────────────┐        │   │
│  │  │    Python Calculators    │  │   QuantLib Calculators   │        │   │
│  │  │  ┌────┐ ┌────┐ ┌────┐   │  │  ┌────┐ ┌────┐ ┌────┐   │        │   │
│  │  │  │ PD │ │LGD │ │EAD │   │  │  │ PD │ │LGD │ │EAD │   │        │   │
│  │  │  └────┘ └────┘ └────┘   │  │  └────┘ └────┘ └────┘   │        │   │
│  │  │  ┌────┐ ┌────┐ ┌────┐   │  │  ┌────┐ ┌────┐ ┌────┐   │        │   │
│  │  │  │CVA │ │PFE │ │ EE │   │  │  │CVA │ │PFE │ │ EE │   │        │   │
│  │  │  └────┘ └────┘ └────┘   │  │  └────┘ └────┘ └────┘   │        │   │
│  │  └──────────────────────────┘  └──────────────────────────┘        │   │
│  │                      Calculator Factory                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│          ┌─────────────────────────┴─────────────────────────┐             │
│          ▼                                                   ▼             │
│  ┌────────────────────┐                        ┌────────────────────┐      │
│  │   Models Module    │                        │    Math Module     │      │
│  │  ┌─────┐ ┌─────┐  │                        │  ┌─────────────┐   │      │
│  │  │Trade│ │Curve│  │                        │  │PathGenerator│   │      │
│  │  └─────┘ └─────┘  │                        │  └─────────────┘   │      │
│  │  ┌─────┐ ┌─────┐  │                        │  ┌─────────────┐   │      │
│  │  │Mkt  │ │Cpty │  │                        │  │ MonteCarlo  │   │      │
│  │  │Data │ │     │  │                        │  │   Engine    │   │      │
│  │  └─────┘ └─────┘  │                        │  └─────────────┘   │      │
│  │   Model Factory   │                        │   Math Factory     │      │
│  └────────────────────┘                        └────────────────────┘      │
│          │                                                   │             │
│          └─────────────────────────┬─────────────────────────┘             │
│                                    ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         Core Module                                  │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │   │
│  │  │Properties│ │  Logger  │ │  Timer   │ │ThreadPool│ │Validators│  │   │
│  │  │Configtor │ │          │ │          │ │          │ │          │  │   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘  │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐                            │   │
│  │  │DateUtils │ │NumUtils  │ │Exceptions│                            │   │
│  │  └──────────┘ └──────────┘ └──────────┘                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│  ┌──────────────────┐  ┌──────────┴───────────┐  ┌──────────────────┐      │
│  │   Data Module    │  │   Config Module      │  │   Docs Module    │      │
│  │  ┌────────────┐  │  │  ┌────────────────┐  │  │  ┌────────────┐  │      │
│  │  │ Generator  │  │  │  │ application.   │  │  │  │  Formulas  │  │      │
│  │  │            │  │  │  │ properties     │  │  │  │ Architecture│ │      │
│  │  └────────────┘  │  │  └────────────────┘  │  │  │ Quickstart │  │      │
│  └──────────────────┘  └──────────────────────┘  └──────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Module Structure

### 3.1 Core Module (`ccranalytics/core/`)

Provides foundational utilities used across all modules.

| Component | Description |
|-----------|-------------|
| `properties_configurator.py` | Configuration file parser with environment variable support |
| `logger.py` | Customized logging with rotation and formatting |
| `timer.py` | Performance timing utilities and decorators |
| `thread_pool.py` | Custom thread pool implementation |
| `exceptions.py` | Custom exception hierarchy |
| `validators.py` | Data validation utilities |
| `date_utils.py` | Date manipulation and business day calculations |
| `numeric_utils.py` | Numerical computation helpers |

### 3.2 Models Module (`ccranalytics/models/`)

Domain models representing financial entities.

| Component | Description |
|-----------|-------------|
| `base.py` | Base classes and protocols |
| `trade.py` | Trade representation |
| `curve.py` | Yield curves and discount factors |
| `market_data.py` | Market data containers |
| `counterparty.py` | Counterparty information |
| `products.py` | Financial product definitions (IRS, FX, CDS, etc.) |
| `factory.py` | Model factory for object creation |

### 3.3 Calculator Module (`ccranalytics/calculator/`)

All CCR metric calculators with dual implementations.

#### Python Implementation (`calculator/python/`)
| Calculator | Metrics |
|------------|---------|
| `pd_calculator.py` | Probability of Default |
| `lgd_calculator.py` | Loss Given Default |
| `ead_calculator.py` | Exposure at Default |
| `el_calculator.py` | Expected Loss |
| `ce_calculator.py` | Current Exposure |
| `pfe_calculator.py` | Potential Future Exposure |
| `ee_calculator.py` | Expected Exposure |
| `cva_calculator.py` | Credit Valuation Adjustment |
| `ec_calculator.py` | Economic Capital |
| `raroc_calculator.py` | Risk-Adjusted Return on Capital |
| `im_calculator.py` | Initial Margin |
| `stress_calculators.py` | Stress Testing & Peak Exposure |

#### QuantLib Implementation (`calculator/qlib/`)
Same set of calculators using QuantLib for enhanced performance and accuracy.

### 3.4 Math Module (`ccranalytics/mathlib/`)

Mathematical utilities for simulation and path generation.

| Component | Description |
|-----------|-------------|
| `base.py` | Base classes, protocols, and configurations |
| `python/path_generator.py` | Pure Python path generation |
| `qlib/path_generator.py` | QuantLib-based path generation |
| `factory.py` | Math component factory |

#### Supported Stochastic Processes
- Geometric Brownian Motion (GBM)
- Ornstein-Uhlenbeck (OU)
- Cox-Ingersoll-Ross (CIR)
- Vasicek
- Hull-White
- Heston Stochastic Volatility
- Merton Jump-Diffusion

### 3.5 Engine Module (`ccranalytics/engine/`)

The main execution engine for CCR analytics.

| Component | Description |
|-----------|-------------|
| `ccr_engine.py` | Main CCREngine class with multi-threading support |

### 3.6 Data Module (`ccranalytics/data/`)

Test data generation utilities.

| Component | Description |
|-----------|-------------|
| `generator.py` | Generate counterparties, trades, market data, stress scenarios |

### 3.7 Config Module (`ccranalytics/config/`)

Configuration files.

| Component | Description |
|-----------|-------------|
| `application.properties` | Main configuration file |

### 3.8 Docs Module (`ccranalytics/docs/`)

Documentation.

| Component | Description |
|-----------|-------------|
| `mathematical_formulas.md` | Mathematical documentation |
| `architecture.md` | This document |
| `quickstart.md` | Getting started guide |
| `api_reference.md` | API documentation |

---

## 4. Design Patterns

### 4.1 Protocol Pattern (Interface)

```python
class DataCalculatorLike(Protocol):
    """Protocol defining calculator interface."""
    
    def __init__(self, name: str, config: Dict[str, Any]): ...
    
    def calculate(self, data: Any) -> Any: ...
    
    def details(self) -> Dict[str, Any]: ...
```

### 4.2 Factory Pattern

```python
class CalculatorFactory:
    """Centralized calculator creation."""
    
    _instance = None
    _calculators: Dict[Tuple, BaseCalculator] = {}
    
    @classmethod
    def get_instance(cls) -> 'CalculatorFactory':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def get_calculator(
        self,
        calc_type: CalculatorType,
        implementation: str = "python"
    ) -> BaseCalculator:
        ...
```

### 4.3 Template Method Pattern

```python
class BaseCalculator(ABC):
    """Base calculator with template method."""
    
    def calculate(self, data: Any) -> CalculationResult:
        self._validate_input(data)
        start_time = time.time()
        result = self._perform_calculation(data)
        elapsed = time.time() - start_time
        return CalculationResult(result, elapsed, self._name)
    
    @abstractmethod
    def _perform_calculation(self, data: Any) -> Any:
        """Subclasses implement this."""
        pass
```

### 4.4 Strategy Pattern

```python
# Different PD calculation strategies
class PDCalculator(BaseCalculator):
    def _perform_calculation(self, data: Any) -> float:
        method = data.get('method', 'through_the_cycle')
        
        if method == 'point_in_time':
            return self._calculate_pit_pd(data)
        elif method == 'through_the_cycle':
            return self._calculate_ttc_pd(data)
        elif method == 'merton':
            return self._calculate_merton_pd(data)
```

### 4.5 Singleton Pattern

```python
class PropertiesConfigurator:
    """Singleton configuration manager."""
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

## 5. Data Flow

### 5.1 Calculation Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│  CCREngine  │────▶│  Factory    │────▶│ Calculator  │
│   Request   │     │             │     │             │     │             │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                           │                                       │
                           │                                       ▼
                           │                              ┌─────────────┐
                           │                              │   Models    │
                           │                              │ (Trade,Mkt) │
                           │                              └─────────────┘
                           │                                       │
                           ▼                                       ▼
                    ┌─────────────┐                       ┌─────────────┐
                    │   Result    │◀──────────────────────│    Math     │
                    │ Aggregation │                       │ (Simulation)│
                    └─────────────┘                       └─────────────┘
```

### 5.2 CCR Metrics Pipeline

```
Market Data + Trades
        │
        ▼
┌───────────────┐
│ Current Exp.  │───────────────────────────────────────┐
└───────────────┘                                        │
        │                                                │
        ▼                                                │
┌───────────────┐     ┌───────────────┐                 │
│  Path Gen.    │────▶│   Monte       │                 │
│  (Stochastic) │     │   Carlo       │                 │
└───────────────┘     └───────────────┘                 │
        │                    │                          │
        │                    ▼                          │
        │            ┌───────────────┐                  │
        │            │   EE / PFE    │──────────────────┤
        │            └───────────────┘                  │
        │                    │                          │
        ▼                    ▼                          │
┌───────────────┐     ┌───────────────┐                 │
│   PD / LGD    │────▶│     CVA       │◀────────────────┘
└───────────────┘     └───────────────┘
        │                    │
        ▼                    ▼
┌───────────────┐     ┌───────────────┐
│  EAD / EL     │     │   EC / IM     │
└───────────────┘     └───────────────┘
        │                    │
        └────────────┬───────┘
                     ▼
              ┌───────────────┐
              │    RAROC      │
              └───────────────┘
```

---

## 6. Threading Model

### 6.1 Engine Threading Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                        CCREngine                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    ThreadPoolExecutor                     │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐    │  │
│  │  │ Worker 1 │ │ Worker 2 │ │ Worker 3 │ │ Worker N │    │  │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘    │  │
│  │       │            │            │            │           │  │
│  │       ▼            ▼            ▼            ▼           │  │
│  │  ┌──────────────────────────────────────────────────┐   │  │
│  │  │               Task Queue                          │   │  │
│  │  │  [Task1] [Task2] [Task3] [Task4] [Task5] ...     │   │  │
│  │  └──────────────────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Task Distribution:                                            │
│  - Each calculator runs in its own thread                      │
│  - Jobs can be parallel or sequential                          │
│  - Priority queue for critical calculations                    │
│  - Callbacks supported for async operations                    │
└────────────────────────────────────────────────────────────────┘
```

### 6.2 Thread Safety

- **Immutable Data**: Calculation inputs are immutable
- **Thread-Local Storage**: Calculator instances cached per-thread
- **Lock-Free Queues**: Task submission uses thread-safe queues
- **Atomic Operations**: Statistics updated atomically

---

## 7. Extension Points

### 7.1 Adding a New Calculator

1. Create calculator class in `calculator/python/`:
```python
class NewMetricCalculator(BaseCalculator):
    def __init__(self, name: str, config: Dict[str, Any]):
        super().__init__(name, CalculatorType.NEW_METRIC, config)
    
    def _perform_calculation(self, data: Any) -> float:
        # Implementation
        return result
```

2. Add QuantLib version in `calculator/qlib/`

3. Register in factory:
```python
# In calculator/factory.py
CalculatorType.NEW_METRIC: {
    'python': 'NewMetricCalculator',
    'quantlib': 'QLNewMetricCalculator'
}
```

### 7.2 Adding a New Stochastic Process

1. Add process type to `ProcessType` enum in `math/base.py`

2. Implement in both path generators:
```python
# In math/python/path_generator.py
def _generate_new_process(self, params: PathGenerationParams) -> np.ndarray:
    # Implementation
    return paths
```

### 7.3 Adding a New Product

1. Create product class in `models/products.py`:
```python
@dataclass
class NewProduct(Product):
    specific_field: float
    
    def value(self, market_data: Any) -> float:
        # Valuation logic
        return value
```

2. Register in model factory

---

## Appendix: Performance Considerations

### Memory Optimization
- Use NumPy arrays for large datasets
- Lazy loading of market data
- Path generation with memory-mapped arrays for large simulations

### Computation Optimization
- Vectorized operations via NumPy
- QuantLib for numerical integration
- Cached discount factors and survival probabilities
- Parallel Monte Carlo paths

### Scaling Guidelines
- 8 workers for typical workloads
- Increase workers for I/O-bound operations
- Consider distributed computing for >100k trades

---

*Document Version: 1.0.0*  
*Last Updated: 2025*
