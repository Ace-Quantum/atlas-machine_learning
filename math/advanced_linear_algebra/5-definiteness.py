#!/usr/bin/env python3
"""This will find the definiteness of a matrix"""

import numpy as np

def valid_matrix(matrix):
    """Checks if the matrix is a list of lists"""

    if not isinstance(matrix, list):
        None

    if not all(isinstance(row, list) for row in matrix):
        None

    if not matrix:
        None

    row_len = len(matrix)

    for row in matrix:
        if len(row) != row_len:
            None

def definiteness(matrix):
    """Returns the definiteness of a marix"""
    
    if isinstance(matrix, np.ndarray) == False:
        return TypeError("matrix must be a numpy.ndarray")
    

