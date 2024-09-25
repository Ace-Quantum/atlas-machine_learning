#!/usr/bin/env python3
"""This code is based on this tutorial
https://www.youtube.com/watch?v=WT6jI8UgROI"""

import numpy as np


def matrix_power(M, iter):
    """Recursive function to get the state after iter steps"""
    if iter == 0:
        return np.identity(len(M))
    elif iter == 1:
        return M
    else:
        return np.dot(M, matrix_power(M, iter - 1))


def markov_chain(P, s, t=1):
    """Documentation"""
    stepped_matrix = np.array(matrix_power(P, t))

    # print(stepped_matrix)

    # print(type(stepped_matrix))

    # ret_array = []

    ret_array = np.dot(s, stepped_matrix)

    # ret_array = np.zeros(len(P))

    # for i in range(len(P)):
    # ret_array[i] = stepped_matrix[0, i]

    # print(ret_array)

    # print(type(ret_array))

    # ret_matrix = np.dot(stepped_matrix)

    # spec_matrix = stepped_matrix[:, 0]

    # return np.dot(stepped_matrix, s)

    return ret_array
