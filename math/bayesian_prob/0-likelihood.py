#!/usr/bin/env python3
"""This function finds likelyhoods for things"""

import numpy as np


def likelihood(x, n, P):
    """determine likelihood"""

    # Verifications
    if n < 0:
        raise ValueError("n must be a positive integer")

    if x <= 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray):
        raise TypeError("P must be a 1D numpy.ndarray")

    if not all(P[val] >= 0 and P[val] <= 1 for val in P):
        raise ValueError("All values in P must be in range [0, 1]")

    return None
