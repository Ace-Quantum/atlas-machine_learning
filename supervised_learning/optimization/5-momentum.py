#!/usr/bin/env python3

"""documentation"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """documentation"""
    v_new = beta1 * v + (1 - beta1) * grad
    var_new = var - alpha * v_new
    return var_new, v_new
