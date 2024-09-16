#!/usr/bin/env python3
"""Here's some documentation"""

import numpy as np


def initialize(X, k):
    """Documentation"""
    
    if not isinstance(X, np.ndarray):
        return None
    if not isinstance(k, int) or k <= 0:
        return None
    if len(X.shape < 2):
        return None
    
    n, d = X.shape
    if n == 0 or d == 0:
        return None
    
    min_values = X.min(axis=0)
    max_values = X.max(axis=0)

    centroids = np.random.uniform(min_values, max_values, size=(k, d))

    return centroids
