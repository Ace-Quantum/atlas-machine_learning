#!/usr/bin/env python3
"""creates the class for a
1D Gaussian Distribution"""

import numpy as np


class GaussianProcess:
    """class as defined earlier"""

    def __init__(self, X_init, Y_init, l=1, sigma_f=1):
        """Initialize variables"""
        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        # vvv to be changed
        self.K = self.kernel(self.X, self.Y)

    def kernel(self, X1, X2):
        """Return covariance matrix"""
        m, n = X1.shape[0], X2.shape[0]

        X1 = X1.reshape(m, 1)
        X2 = X2.reshape(n, 1)

        pair_diff = X1 - X2.T

        sq_eucl_dist = np.sum(pair_diff ** 2, axis=1)

        k = self.sigma_f**2 * np.exp(-sq_eucl_dist / (2 * self.l**2))

        return k
