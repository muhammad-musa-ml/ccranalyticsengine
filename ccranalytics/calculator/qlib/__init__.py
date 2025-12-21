"""
CCR Analytics Engine - QuantLib Calculator Implementations v1.2.0
===================================================================

QuantLib-based high-performance CCR calculators.

Copyright © 2025-2030, All Rights Reserved
Ashutosh Sinha | Email: ajsinha@gmail.com
"""

from .pd_calculator import QLPDCalculator
from .lgd_calculator import QLLGDCalculator
from .ead_calculator import QuantLibEADCalculator
from .el_calculator import QuantLibELCalculator
from .ce_calculator import QuantLibCECalculator
from .pfe_calculator import QuantLibPFECalculator
from .ee_calculator import QuantLibEECalculator, QuantLibEffectiveEECalculator
from .cva_calculator import QuantLibCVACalculator
from .ec_calculator import QuantLibECCalculator
from .raroc_calculator import QuantLibRAROCCalculator
from .im_calculator import QuantLibIMCalculator
from .stress_calculators import QLStressedExposureCalculator, QLPeakExposureCalculator

# Aliases for consistency
EECalculatorQL = QuantLibEECalculator
CVACalculatorQL = QuantLibCVACalculator
PFECalculatorQL = QuantLibPFECalculator

__all__ = [
    # PD/LGD
    'QLPDCalculator',
    'QLLGDCalculator',
    # Exposure
    'QuantLibEADCalculator',
    'QuantLibELCalculator',
    'QuantLibCECalculator',
    'QuantLibPFECalculator',
    'QuantLibEECalculator',
    'QuantLibEffectiveEECalculator',
    # Advanced
    'QuantLibCVACalculator',
    'QuantLibECCalculator',
    'QuantLibRAROCCalculator',
    'QuantLibIMCalculator',
    # Stress
    'QLStressedExposureCalculator',
    'QLPeakExposureCalculator',
    # Aliases
    'EECalculatorQL',
    'CVACalculatorQL',
    'PFECalculatorQL',
]
