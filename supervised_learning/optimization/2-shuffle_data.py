#!/usr/bin/env python3
"""Documentation"""

import numpy as np


def shuffle_data(X, Y):
    """Documentation"""
    assert len(X) == len(Y)
    p = np.random.permutation(len(X))
    return X[p], Y[p]
