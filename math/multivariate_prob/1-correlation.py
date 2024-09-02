#!/usr/bin/env python3
"""This module finds the correlation of a matrix"""

import numpy as np


def correlation(C):
    """This is the function that finds correlation"""

    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    row_len = len(C)

    dim = C.shape[0]

    if C.shape != (dim, dim):
        raise ValueError("C must be a 2D square matrix")

    # ret_matrix = C.corrcoef()

    ret_matrix = np.zeros((dim, dim))

    for i in range(dim):
        for j in range(dim):
            if i==j:
                ret_matrix[i, j] = 1
            else:
                ret_matrix[i, j] = C[i, j] / np.sqrt(C[i, i] * C[j, j])

    return ret_matrix
