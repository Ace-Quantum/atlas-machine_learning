#!/usr/bin/env python3
"""Here's some documentation"""

import numpy as np
initialize = __import__('0-initialize').initialize


def initialize(X, k):
    """Documentation"""

    if not isinstance(X, np.ndarray):
        return None
    if not isinstance(k, int) or k <= 0:
        return None
    if len(X.shape) != 2:
        return None

    n, d = X.shape
    if n == 0 or d == 0:
        return None

    min_values = X.min(axis=0)
    max_values = X.max(axis=0)

    centroids = np.random.uniform(min_values, max_values, size=(k, d))

    return centroids

def kmeans(X, k, iterations=1000):
    """Documentation"""
    
    C = initialize(X, k)
    if C is None:
        return None, None
    
    n, d = X.shape
    
    for _ in range(iterations):
        clss = np.argmin(np.linalg.norm(X[:, np.newaxis] - C, axis=2), axis=1)

        # calculating new centroids
        new_C = np.array([X[clss == i].mean(axis=0) if np.any(
            clss ==i) else C[i] for i in range(k)])

        if np.all(C == new_C):
            break

        C = new_C

    # return_clusters = ~np.all(new_C == 0, axis=1)
    # C = C[return_clusters]
    # clss = clss[return_clusters]

    return C, clss
