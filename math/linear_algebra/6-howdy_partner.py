#!/usr/bin/env python3
"""Hey look here's some documentation"""


def cat_arrays(arr1, arr2):
    """Oh wow, even more documentation?"""

    cat_arr = []

    for i in range(len(arr1)):
        cat_arr.append(arr1[i])

    # print("inbetween")
    # print(cat_arr)

    for i in range(len(arr2)):
        cat_arr.append(arr2[i])

    return cat_arr
