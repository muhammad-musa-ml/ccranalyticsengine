"""
CCR Analytics Engine - Data Module
==================================

Test data generation utilities for the CCR Analytics Engine.

Copyright © 2025-2030, All Rights Reserved
Ashutosh Sinha | Email: ajsinha@gmail.com

Legal Notice: This module and the associated software architecture are proprietary 
and confidential. Unauthorized copying, distribution, modification, or use is 
strictly prohibited without explicit written permission from the copyright holder.

Patent Pending: Certain architectural patterns and implementations described in 
this module may be subject to patent applications.
"""

from .generator import (
    ProductType,
    CreditRating,
    GeneratedTrade,
    GeneratedCounterparty,
    GeneratedMarketData,
    DataGenerator,
    create_test_dataset,
)

__all__ = [
    "ProductType",
    "CreditRating",
    "GeneratedTrade",
    "GeneratedCounterparty",
    "GeneratedMarketData",
    "DataGenerator",
    "create_test_dataset",
]
