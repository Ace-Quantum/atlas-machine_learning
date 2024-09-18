#!/usr/bin/env python3
"""Here's some documentation"""

import numpy as np

pdf = __import__('5-pdf').pdf


def expectation(X, pi, m, S):
    """Documentation"""

    if not isinstance(X, np.ndarray) or not isinstance(pi, np.ndarray):
        return None, None
    if not isinstance(m, np.ndarray) or not isinstance(S, np.ndarray):
        return None, None

    if not len(X.shape) == 2 or not len(pi.shape) == 1:
        return None, None
    if not len(m.shape) == 2 or not len(S.shape) == 3:
        return None, None

    n, d = X.shape
    k = pi.shape[0]

    if not d == m.shape[1]: #or not d== S.shape[1]:
        None, None
    # if not d == S.shape[2]

    g = np.zeros((k, n))

    for i in range(k):
        g[i] = pi[i] * pdf(X, m[i], S[i])

    total_probs = np.sum(g, axis=0)

    if np.any(total_probs == 0):
        return None, None

    g /= total_probs

    log_likelihood = np.sum(np.log(total_probs))

    return g, log_likelihood
