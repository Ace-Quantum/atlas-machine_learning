#!/usr/bin/env python3
"""Finding the minor of a matrix"""


def copy_matrix(matrix):
    """A helper function for copying matrices"""

    rows = len(matrix)
    cols = len(matrix[0])

    # make new matrix of 0's
    new_matrix = []
    while len(new_matrix) < rows:
        new_matrix.append([])
        while len(new_matrix[-1]) < cols:
            new_matrix[-1].append(0.0)

    for i in range(rows):
        for j in range(cols):
            new_matrix[i][j] = matrix[i][j]

    return new_matrix


def valid_matrix(matrix):
    """Checks if the matrix is a list of lists"""

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix:
        raise TypeError("matrix must be a list of lists")

    row_len = len(matrix)

    for row in matrix:
        if len(row) != row_len:
            raise ValueError("matrix must be a non-empty square matrix")


def determinant(matrix, total=0):
    """This will find the determinant"""

    if matrix == [[]]:
        return 1

    valid_matrix(matrix)

    # set up some indeces to use later
    indices = list(range(len(matrix)))

    if len(matrix) == 1:
        return matrix[0][0]

    # if matrix is 2x2 there's no need for recursion
    # we can just do the formula
    # Ok so this is also the base case I guess
    if len(matrix) == 2 and len(matrix[0]) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det

    # I found this code from
    # https://integratedmlai.com/
    # find-the-determinant-of-a-matrix-with-pure-python-without-numpy-or-scipy/
    # and tbh I'm not sure I actually understand it?

    for fc in indices:
        copy = copy_matrix(matrix)
        copy = copy[1:]
        height = len(copy)

        for i in range(height):
            copy[i] = copy[i][0:fc] + copy[i][fc + 1:]

        # Why find and keep sign?
        sign = (-1) ** (fc % 2)

        # this makes sense kind of I guess?
        sub_det = determinant(copy)

        # total all the returns
        total += sign * matrix[0][fc] * sub_det

    return total


def minor(matrix):
    """determines the minor of a matrix"""
    if len(matrix) == 1:
        return matrix[0]

    valid_matrix(matrix)

    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = []
    while len(new_matrix) < rows:
        new_matrix.append([])
        while len(new_matrix[-1]) < cols:
            new_matrix[-1].append(0.0)

    for i in range(rows):
        for j in range(cols):
            temp_copy = copy_matrix(matrix)

            temp_copy = temp_copy[:i] + temp_copy[i + 1:]
            for k in range(len(temp_copy)):
                temp_copy[k] = temp_copy[k][:j] + temp_copy[k][j + 1:]

            new_matrix[i][j] = determinant(temp_copy)

    return new_matrix


def cofactor(matrix):
    """Finds a cofactor"""
    valid_matrix(matrix)

    if len(matrix) == 1:
        return matrix

    minor_matrix = minor(matrix)

    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = [[0.0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            new_matrix[i][j] = minor_matrix[i][j] * (-1) ** (i + j)

    return new_matrix
