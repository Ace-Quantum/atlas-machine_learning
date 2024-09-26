#!/usr/bin/env python3
"""This code was based on code found on the following link
https://stackoverflow.com/questions/52137856/steady-state-probabilities-markov-chain-python-implementation"""

import numpy as np


def regular(P):
    """Documentation"""

    # # Idk if we need to do the identity matrix thing
    # # If we do it'll go here
    # #   I'm gonna just try it anywa

    # # normalizing
    # P = P / np.sum(P, axis=1, keepdims=True)

    # # Initializing return matrix
    # ret_matrix = np.zeros((P.shape[0], 1))
    # ret_matrix[0] = 1

    # return np.matmul(np.linalg.inv(P), ret_matrix)

    # dim = P.shape[0]

    # P = P - np.eye(P.shape[0])

    # vec_ones = np.ones(dim)

    return None