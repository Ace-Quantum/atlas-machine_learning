#!/usr/bin/env python3
"""This code is based on this tutorial
https://www.youtube.com/watch?v=WT6jI8UgROI"""

import numpy as np

def matrix_power(M, iter):
    if iter == 0:
        return np.identity(len(M))
    elif iter == 1:
        return M
    else:
        return np.dot(M, matrix_power(M, iter - 1))

def markov_chain(P, s, t=1):
    """Documentation"""
    stepped_matrix = matrix_power(P, t)

    # print(stepped_matrix[0])

    # ret_matrix = np.dot(stepped_matrix)

    # return np.dot(stepped_matrix[:, 0], s)

    return stepped_matrix[0]