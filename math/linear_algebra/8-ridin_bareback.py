#!/usr/bin/env python3
"""Honestly idk where the heck the documentation needs to go"""
size_check = __import__("2-size_me_please").matrix_shape


def mat_mul(mat1, mat2):
    """Let's not split hairs over it though"""

    rows = size_check(mat1)[0]
    cols = size_check(mat2)[1]

    return_arr = [[0 for _ in range(cols)] for _ in range(rows)]

    # print("Size mat1: " + str(size_check(mat1)))
    # print("Size mat2: " + str(size_check(mat2)))
    # print("Size return_arr: " + str(size_check(return_arr)))

    if size_check(mat1)[1] != size_check(mat2)[0]:
        return None

    for i in range(rows):
        for j in range(cols):
            for k in range(len(mat2)):
                return_arr[i][j] += mat1[i][k] * mat2[k][j]
                # print(return_arr[i][j])

    # print(return_arr)
    return return_arr
