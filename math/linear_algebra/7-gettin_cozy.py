#!/usr/bin/env python3
"""Does the documentation go here or?"""
basic_matrix_cat = __import__("6-howdy_partner").cat_arrays
size_matrix = __import__("2-size_me_please").matrix_shape


def cat_matrices2D(mat1, mat2, axis=0):
    """Idk but I know I need some here"""

    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None
    if not mat1 or not mat2:
        return None

    return_arr = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]

    if axis == 0:
        return basic_matrix_cat(mat1, mat2)
    else:
        return_arr = []
        for i in range(len(mat1)):
            row = basic_matrix_cat(mat1[i], mat2[i])
            return_arr.append(row)
        return return_arr
