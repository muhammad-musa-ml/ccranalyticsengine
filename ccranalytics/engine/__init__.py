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
CCR Analytics Engine - Engine Module
=====================================

Main engine for CCR analytics calculations.

Usage:
    from .engine import create_engine, CCREngine
    
    # Using context manager
    with create_engine() as engine:
        result = engine.calculate(CalculatorType.PD, input_data)
    
    # Manual lifecycle
    engine = CCREngine()
    engine.start()
    result = engine.calculate(CalculatorType.CVA, input_data)
    engine.stop()
"""

from .ccr_engine import (
    CCREngine,
    create_engine,
    EngineStatus,
    CalculationPriority,
    CalculationTask,
    CalculationJob,
    TaskResult,
    JobResult
)

__all__ = [
    'CCREngine',
    'create_engine',
    'EngineStatus',
    'CalculationPriority',
    'CalculationTask',
    'CalculationJob',
    'TaskResult',
    'JobResult'
]
