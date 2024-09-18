#!/usr/bin/env python3
"""Here's some documentation"""

import numpy as np


def kmeans(X, k, iterations=1000):
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

    min_values = np.min(X, axis=0)
    max_values = np.max(X, axis=0)

    C = np.random.uniform(min_values, max_values, size=(k, d))

    # return centroids


    # C = initialize(X, k)
    if C is None:
        return None, None

    # n, d = X.shape

    clss = np.zeros(n)

    for _ in range(iterations):
        distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
        clss = np.argmin(distances, axis=1)

        C_new = np.zeros((k, d))

        for j in range(k):
            cluster_points = X[clss == j]

            if np.any(clss == j):
                C_new[j] = cluster_points.mean(axis=0)
            else:
                C_new[j] = np.random.uniform(min_values, max_values, size=(d))

        if np.all(C_new == C):
            break

        C = C_new

        # calculating new centroids
        # new_C = np.zeros((k, d))

        # for i in range(k):
        #     cluster_points = X[clss == i]

        #     if len(cluster_points) == 0:
        #         C[i] = np.random.uniform(min_values, max_values, size=d)
        #     else:
        #         C[i] = np.mean(cluster_points, axis=0)
            # -------- attempts to update centroids --------
                
            #     if np.any(clss == i):
            #         new_clss[i] = X[clss == i].mean(axis=0)
            #     else:
            #         new_clss[i] = np.random.uniform(
            #             low=X.min(axis=0), high=X.max(axis=0), size=(d,)
            #         )
            # C = new_clss

    # return_clusters = ~np.all(new_C == 0, axis=1)
    # C = C[return_clusters]
    # clss = clss[return_clusters]

    return C, clss
