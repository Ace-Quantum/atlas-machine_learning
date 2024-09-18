#!/usr/bin/env python3
"""Here's some documentation"""

import numpy as np
pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """Documentation"""

    if not isinstance(X, np.ndarray) or not isinstance(pi, np.ndarray):
        return None, None
    if not len(X.shape) == 2 or not len(pi.shape) == 2:
        return None, None

    n, d = X.shape
    k = pi.shape[0]

    g = np.zeros((k, n))

    for i in range(k):
        g[i] = pi[i] * pdf(X, m[i], S[i])

    total_probs = np.sum(g, axis=0)

    if np.any(total_probs ==0):
        return None, None
    
    g /= total_probs

    log_likelihood = np.sum(np.log(total_probs))

    return g, log_likelihood