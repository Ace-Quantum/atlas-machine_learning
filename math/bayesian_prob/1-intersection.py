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
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")

    if x <= 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if not all((P >= 0) & (P <= 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    coeff = np.math.factorial(n) // (
        np.math.factorial(x) * np.math.factorial(n - x))

    likelihood = coeff * (P ** x) * ((1 - P) ** (n - x))

    return likelihood


def intersection(x, n, P, Pr):
    """calculates intersecting data points"""
    temp = likelihood(x, n, P)

    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    if not all((Pr >= 0) & (Pr <= 1)):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    if np.sum(Pr) != 1:
        raise ValueError("Pr must sum to 1")

    return None
