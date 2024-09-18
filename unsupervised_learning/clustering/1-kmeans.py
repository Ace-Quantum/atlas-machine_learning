#!/usr/bin/env python3
"""Here's some documentation"""

import numpy as np


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

    # assigning clusters
    distances = np.sqrt(np.sum((X[:, np.newaxis] - C) ** 2, axis=2))
    clss = np.argmin(distances, axis=1)

    for _ in range(iterations):
        old_C = np.copy(C)

        # update the centroids
        C = np.array([np.mean(X[clss == i], axis=0) for i in range(k)])

        if np.all(old_C == C):
            break

    return C, clss
