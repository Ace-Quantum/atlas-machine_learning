#!/usr/bin/env python3
"""Documentation"""


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """documentation"""
    v = beta1 * v + (1 - beta1) * grad
    s = beta2 * s + (1 - beta2) * (grad**2)

    v_cor = v / (1 - beta1**t)
    s_cor = s / (1 - beta2**t)

    var -= alpha * v_cor / ((s_cor**0.5) + epsilon)

    return var, v, s
