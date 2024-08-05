#!/usr/bin/env python3
"""This is some documentation"""

size_matrix = __import__("2-size_me_please").matrix_shape


def add_matrices2D(mat1, mat2):
    """This is even more documentation"""

    rows = len(mat1)
    cols = len(mat1[0])

    return_arr = [[0 for _ in range(cols)] for _ in range(rows)]

    if len(mat1) == 0 or len(mat1[0]) == 0:
        return return_arr

    if len(mat2) == 0 or len(mat2[0]) == 0:
        return return_arr

    if size_matrix(mat1) != size_matrix(mat2):
        return None

    for i in range(rows):
        for j in range(cols):
            return_arr[i][j] = mat1[i][j] + mat2[i][j]

    return return_arr
