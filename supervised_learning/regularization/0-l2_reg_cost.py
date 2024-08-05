#!/usr/bin/env python3
"""Here's some documentation"""
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """Variables:
    cost - cost of the network without L2 regularization
    lambtha - regularization parameter
    weights - dictionary of the weights and biases (
        numpy.ndarrays) of the neural network
    L - number of layers in the neural network
    m - number of data points used
    Returns: the cost of the network accounting for L2 regularization"""

    reg_cost = 0

    # weight_matrices = [weights[f'W{i+1}'] for i in range(L)]
    # bias_vectors = [weights.get(f'b{i+1}', np.zeros_like(
    #     weight_matrices[i][0])) for i in range(L)]

    for i in range(1, L + 1):
        weight = weights[f"W{i}"]
        reg_cost += np.sum(np.square(weight))

    reg_term = lambtha / (2 * m) * reg_cost

    return cost + reg_term
