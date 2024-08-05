#!/usr/bin/env python3
"""Documentation"""


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """Documentation"""
    s_new = beta2 * s + (1 - beta2) * (grad**2)

    var_new = var - alpha * grad / (s_new + epsilon) ** 0.5

    return var_new, s_new
