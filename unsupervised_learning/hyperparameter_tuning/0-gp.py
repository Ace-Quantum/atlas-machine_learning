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
        self.K = self.kernel(X_init, Y_init)

    def kernel(self, X1, X2):
        """Return covariance matrix"""

        # m, n = X1.shape[0], X2.shape[0]

        # diff = X1 - X2.T

        # sq_dist = np.sum(diff ** 2, axis=1)

        # k = self.sigma_f**2 * np.exp(-0.5 / (2 * self.l**2/))

        # sq_dist = np.sum(X1**2, 1).reshape(-1, 1) + np.sum(X2**2, 1) - 2 * np.dot(X1, X2.T)

        # sq_dist = np.sum((X1 - X2.T)**2, axis=1)

        # return self.sigma_f**2 * np.exp(-0.5 / self.l**2 * sq_dist)

        # return k
