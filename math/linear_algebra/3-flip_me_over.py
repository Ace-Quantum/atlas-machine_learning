#!/usr/bin/env python3
"""This file is solely for the purpose of transposing matrixes"""


def matrix_transpose(matrix):
    """this function transposes a matrix"""

    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return (transposed)
