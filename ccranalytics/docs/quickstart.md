# CCR Analytics Engine - Quickstart Guide

Copyright © 2025-2030, All Rights Reserved  
Ashutosh Sinha | Email: ajsinha@gmail.com

---

## Table of Contents

1. [Installation](#1-installation)
2. [Quick Start](#2-quick-start)
3. [Basic Usage](#3-basic-usage)
4. [Configuration](#4-configuration)
5. [Examples](#5-examples)
6. [Troubleshooting](#6-troubleshooting)

---

## 1. Installation

### 1.1 Prerequisites

- Python 3.9 or higher
- pip package manager
- (Optional) QuantLib-Python for enhanced performance

### 1.2 Install Dependencies

```bash
# Core dependencies
pip install numpy scipy

# Optional: QuantLib for enhanced performance
pip install QuantLib-Python
```

### 1.3 Install CCR Analytics Engine

```bash
# Clone or extract the package
cd ccranalytics

# Verify installation
python -c "import ccranalytics; print('Installation successful!')"
```

---

## 2. Quick Start

### 2.1 Minimal Example

```python
from ccranalytics.engine import CCREngine
from ccranalytics.data import DataGenerator

# Generate test data
generator = DataGenerator()
portfolio = generator.generate_portfolio(
    num_counterparties=10,
    trades_per_counterparty=5
)

# Create and start engine
engine = CCREngine()
engine.start()

# Calculate CCR metrics for a trade
trade_data = {
    'trade_id': portfolio['trades'][0].trade_id,
    'notional': portfolio['trades'][0].notional,
    'mtm': portfolio['trades'][0].mtm,
    'counterparty_id': portfolio['trades'][0].counterparty_id,
    'pd': 0.02,
    'lgd': 0.45,
    'maturity': 5.0
}

# Run calculation
result = engine.calculate('pd', trade_data)
print(f"PD Result: {result.value}")

# Cleanup
engine.stop()
```

### 2.2 Using Context Manager

```python
from ccranalytics.engine import CCREngine

with CCREngine() as engine:
    result = engine.calculate('pd', {'rating': 'BBB', 'method': 'rating_based'})
    print(f"PD: {result.value:.4%}")
```

---

## 3. Basic Usage

### 3.1 Individual Calculators

```python
from ccranalytics.calculator import CalculatorFactory, CalculatorType

# Get factory instance
factory = CalculatorFactory.get_instance()

# Get a calculator (Python implementation)
pd_calc = factory.get_calculator(CalculatorType.PD, implementation='python')

# Calculate PD
result = pd_calc.calculate({
    'rating': 'A',
    'method': 'rating_based'
})
print(f"PD: {result.value:.4%}")

# Get QuantLib implementation
pd_calc_ql = factory.get_calculator(CalculatorType.PD, implementation='quantlib')
```

### 3.2 Available Calculators

| Calculator Type | Description |
|----------------|-------------|
| `PD` | Probability of Default |
| `LGD` | Loss Given Default |
| `EAD` | Exposure at Default |
| `EL` | Expected Loss |
| `CE` | Current Exposure |
| `PFE` | Potential Future Exposure |
| `EE` | Expected Exposure |
| `CVA` | Credit Valuation Adjustment |
| `EC` | Economic Capital |
| `RAROC` | Risk-Adjusted Return on Capital |
| `IM` | Initial Margin |
| `STRESSED_EXPOSURE` | Stress Testing |
| `PEAK_EXPOSURE` | Peak Exposure |

### 3.3 Comprehensive CCR Analysis

```python
from ccranalytics.engine import CCREngine

with CCREngine() as engine:
    # Calculate all CCR metrics at once
    metrics = engine.calculate_ccr_metrics(
        trade_data={
            'trade_id': 'T001',
            'notional': 10_000_000,
            'mtm': 250_000,
            'maturity': 5.0,
            'product_type': 'IRS'
        },
        counterparty_data={
            'counterparty_id': 'CP001',
            'rating': 'BBB',
            'pd': 0.02,
            'lgd': 0.45
        },
        market_data={
            'discount_rate': 0.03,
            'volatility': 0.20,
            'credit_spread': 0.015
        }
    )
    
    print("CCR Metrics Summary:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value}")
```

---

## 4. Configuration

### 4.1 Loading Configuration

```python
from ccranalytics.core import PropertiesConfigurator

# Load configuration
config = PropertiesConfigurator('config/application.properties')

# Access values
max_workers = config.get_int('engine.max_workers', default=8)
confidence = config.get_float('calculator.confidence_level', default=0.99)
implementation = config.get('engine.default_implementation', default='python')
```

### 4.2 Key Configuration Options

```properties
# Engine settings
engine.max_workers=8
engine.default_implementation=python
engine.timeout=300

# Calculator settings
calculator.confidence_level=0.99
calculator.num_simulations=10000

# PFE specific
calculator.pfe.confidence_level=0.95
calculator.pfe.time_points=12

# CVA specific
calculator.cva.integration_points=100
calculator.cva.use_wrong_way_risk=false
```

---

## 5. Examples

### 5.1 PD Calculation

```python
from ccranalytics.calculator import CalculatorFactory, CalculatorType

factory = CalculatorFactory.get_instance()
pd_calc = factory.get_calculator(CalculatorType.PD)

# Rating-based PD
result = pd_calc.calculate({
    'method': 'rating_based',
    'rating': 'BBB'
})
print(f"Rating-based PD: {result.value:.4%}")

# Merton model PD
result = pd_calc.calculate({
    'method': 'merton',
    'asset_value': 100_000_000,
    'debt': 60_000_000,
    'asset_volatility': 0.25,
    'time_horizon': 1.0
})
print(f"Merton PD: {result.value:.4%}")
```

### 5.2 CVA Calculation

```python
from ccranalytics.calculator import CalculatorFactory, CalculatorType

factory = CalculatorFactory.get_instance()
cva_calc = factory.get_calculator(CalculatorType.CVA)

result = cva_calc.calculate({
    'expected_exposures': [100000, 150000, 200000, 180000, 150000],
    'time_points': [0.5, 1.0, 2.0, 3.0, 5.0],
    'pd': 0.02,
    'lgd': 0.45,
    'discount_rate': 0.03,
    'credit_spread': 0.015
})

print(f"CVA: ${result.value:,.2f}")
```

### 5.3 PFE with Monte Carlo

```python
from ccranalytics.calculator import CalculatorFactory, CalculatorType

factory = CalculatorFactory.get_instance()
pfe_calc = factory.get_calculator(CalculatorType.PFE)

result = pfe_calc.calculate({
    'method': 'monte_carlo',
    'initial_exposure': 1_000_000,
    'volatility': 0.20,
    'drift': 0.05,
    'maturity': 5.0,
    'confidence_level': 0.95,
    'num_simulations': 10000,
    'num_time_points': 60
})

print(f"PFE Profile: {result.value}")
```

### 5.4 Stress Testing

```python
from ccranalytics.calculator import CalculatorFactory, CalculatorType

factory = CalculatorFactory.get_instance()
stress_calc = factory.get_calculator(CalculatorType.STRESSED_EXPOSURE)

result = stress_calc.calculate({
    'base_exposure': 10_000_000,
    'scenario': '2008_crisis',
    'product_type': 'IRS',
    'sensitivities': {
        'dv01': 50000,
        'duration': 4.5,
        'fx_delta': 0,
        'vega': 25000
    }
})

print(f"Stressed Exposure: ${result.value:,.2f}")
```

### 5.5 Path Generation

```python
from ccranalytics.mathlib import MathFactory, ProcessType, PathGenerationParams

factory = MathFactory.get_instance()
path_gen = factory.create_path_generator(implementation='python')

# Generate GBM paths
params = PathGenerationParams(
    initial_value=100.0,
    drift=0.05,
    volatility=0.20,
    maturity=1.0,
    num_steps=252,
    num_paths=1000
)

result = path_gen.generate_paths(ProcessType.GBM, params)
print(f"Path shape: {result.paths.shape}")
print(f"Final values mean: {result.paths[:, -1].mean():.2f}")
```

### 5.6 Batch Processing

```python
from ccranalytics.engine import CCREngine, CalculationJob, CalculationTask

with CCREngine() as engine:
    # Create batch job
    tasks = [
        CalculationTask(
            task_id=f'pd_{i}',
            calculator_type='pd',
            input_data={'rating': rating, 'method': 'rating_based'}
        )
        for i, rating in enumerate(['AAA', 'AA', 'A', 'BBB', 'BB', 'B'])
    ]
    
    job = CalculationJob(
        job_id='batch_pd',
        tasks=tasks,
        parallel=True
    )
    
    # Submit and wait for results
    result = engine.submit_job(job)
    
    for task_id, task_result in result.results.items():
        print(f"{task_id}: {task_result.value:.4%}")
```

### 5.7 Performance Benchmarking

```python
from ccranalytics.engine import CCREngine

with CCREngine() as engine:
    # Compare Python vs QuantLib performance
    benchmark_result = engine.benchmark(
        calculator_types=['pd', 'lgd', 'ead', 'cva'],
        test_data={
            'rating': 'BBB',
            'method': 'rating_based',
            'notional': 10_000_000,
            'mtm': 500_000,
            'collateral': 200_000
        },
        iterations=100
    )
    
    print("\nBenchmark Results:")
    print("-" * 60)
    for calc_type, results in benchmark_result.items():
        print(f"\n{calc_type.upper()}:")
        print(f"  Python:   {results['python']['avg_time']*1000:.3f}ms")
        print(f"  QuantLib: {results['quantlib']['avg_time']*1000:.3f}ms")
        print(f"  Speedup:  {results['speedup']:.2f}x")
```

---

## 6. Troubleshooting

### 6.1 Common Issues

**QuantLib not found:**
```python
# Check if QuantLib is available
try:
    import QuantLib
    print(f"QuantLib version: {QuantLib.__version__}")
except ImportError:
    print("QuantLib not installed. Using Python implementation.")
```

**Configuration not loading:**
```python
import os
config_path = 'config/application.properties'
if not os.path.exists(config_path):
    print(f"Config file not found: {config_path}")
```

**Memory issues with large simulations:**
```python
# Reduce simulation size or use chunking
params = PathGenerationParams(
    num_paths=1000,  # Reduce from 100000
    num_steps=50     # Reduce from 252
)
```

### 6.2 Logging

```python
from ccranalytics.core import CCRLogger
import logging

# Enable debug logging
logger = CCRLogger.get_logger('debug_session')
logger.setLevel(logging.DEBUG)
```

### 6.3 Getting Help

- Check the mathematical formulas documentation
- Review the architecture documentation
- Examine the API reference
- Contact: ajsinha@gmail.com

---

*Document Version: 1.0.0*  
*Last Updated: 2025*
