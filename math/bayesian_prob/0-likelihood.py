#!/usr/bin/env python3
"""This function finds likelyhoods for things"""

import numpy as np


def likelihood(x, n, P):
    """determine likelihood"""

    # Verifications
    if not isinstance(n, int):
        raise ValueError("n must be a positive integer")

    if not n > 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int):
        raise ValueError("x must be an integer that is greater than or equal to 0")

    if x <= 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray):
        raise TypeError("P must be a 1D numpy.ndarray")

    all_in_range = all(0 <= P[val] <= 1 for val in P)
    if not all_in_range:
        raise ValueError("All values in P must be in range [0, 1]")

    return None
