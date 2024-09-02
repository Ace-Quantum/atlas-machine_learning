#!/usr/bin/env python3
"""This module finds the correlation of a matrix"""

import numpy as np

def correlation(C):
    """This is the function that finds correlation"""

    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    row_len = len(C)

    dim = C.shape[1]

    if C.shape != (dim, dim):
        raise ValueError("C must be a 2D square matrix")