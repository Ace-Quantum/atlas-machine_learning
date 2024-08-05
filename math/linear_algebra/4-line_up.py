#!/usr/bin/env python3
"""Idk what kind of documentation they want but here's this"""


def add_arrays(arr1, arr2):
    """More docs"""

    return_arr = []

    if len(arr1) != len(arr2):
        return None

    for i in range(len(arr1)):
        return_arr.append(arr1[i] + arr2[i])
        # return_arr[i] = arr1[i] + arr2[i]

    return return_arr
