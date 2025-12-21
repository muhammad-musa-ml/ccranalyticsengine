# Copyright © 2025-2030, All Rights Reserved
# Ashutosh Sinha | Email: ajsinha@gmail.com
#
# Legal Notice: This module and the associated software architecture are proprietary
# and confidential. Unauthorized copying, distribution, modification, or use is
# strictly prohibited without explicit written permission from the copyright holder.
#
# Patent Pending: Certain architectural patterns and implementations described in
# this module may be subject to patent applications.

"""
CCR Analytics Engine - Math Module
===================================

Mathematical utilities for CCR analytics including:
- Stochastic path generation (GBM, OU, CIR, Heston, etc.)
- Monte Carlo simulation engines
- Statistical utilities
- Numerical methods

Implementations:
- Pure Python: Cross-platform, no external dependencies
- QuantLib: High-performance, industry-standard library

Usage:
    from .mathlib import get_math_factory
    from .mathlib.base import PathGenerationParams, ProcessType
    
    factory = get_math_factory()
    generator = factory.create_path_generator()
    
    params = PathGenerationParams(
        initial_value=100.0,
        drift=0.05,
        volatility=0.2,
        maturity=1.0,
        num_paths=10000,
        num_steps=252
    )
    
    result = generator.generate_paths(params, ProcessType.GBM)
"""

from .base import (
    ProcessType,
    ImplementationType,
    PathGenerationParams,
    PathResult,
    MonteCarloConfig,
    BasePathGenerator,
    BaseMonteCarloEngine,
    PathGeneratorLike,
    MonteCarloEngineLike,
    StatisticalUtilsLike
)

from .factory import MathFactory, get_math_factory

__all__ = [
    # Enums
    'ProcessType',
    'ImplementationType',
    
    # Data classes
    'PathGenerationParams',
    'PathResult',
    'MonteCarloConfig',
    
    # Base classes
    'BasePathGenerator',
    'BaseMonteCarloEngine',
    
    # Protocols
    'PathGeneratorLike',
    'MonteCarloEngineLike',
    'StatisticalUtilsLike',
    
    # Factory
    'MathFactory',
    'get_math_factory'
]
