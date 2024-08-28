#!/usr/bin/env python3
"""This is meant to teach me to code to find a determinant of a matrix"""

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

def determinant(matrix, total=0):
    """This will find the determinant"""

    if type(matrix) != list or type(matrix[0]) != list:
        return TypeError("matrix must be a list of lists")

    # Error handling if matrix is not square
    if len(matrix) != len(matrix[0]):
        return ValueError("matrix must be a square matrix")


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
            copy[i] = copy[i][0:fc] + copy[i][fc+1:]

        # Why find and keep sign?
        sign = (-1) ** (fc % 2)

        # this makes sense kind of I guess?
        sub_det = determinant(copy_matrix)

        # total all the returns
        total += sign * matrix[0][fc] * sub_det

    return total