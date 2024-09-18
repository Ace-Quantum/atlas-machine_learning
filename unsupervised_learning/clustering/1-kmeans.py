#!/usr/bin/env python3
"""Here's some documentation"""

import numpy as np


def kmeans(X, k, iterations=1000):
    """Documentation"""

    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None
    
    n, d = X.shape

    C = np.random.uniform(low=np.min(X, axis=0), high=np.max(X, axis=0), size=(k, d))

    clss = np.zeros(n)

    for i in range(iterations):
        distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)

        clss = np.argmin(distances, axis=1)

        C_new = np.zeros((k, d))

        for j in range(k):
            cluster_points = X[clss == j]

            if np.any(clss == j):
                C_new[j] = cluster_points.mean(axis=0)

            else:
                C_new[j] = np.random.uniform(
                    low=np.min(X, axis=0),
                    high=np.max(X, axis=0),
                    size=(d)
                )
        
        if np.all(C_new == C):
            break

        C = C_new

    return C, clss