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
        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """Return covariance matrix"""

        m, _ = X1.shape
        n, _ = X2.shape

        k = np.zeros((m, n))

        for i in range(m):
            for j in range(n):
                diff = np.linalg.norm(X1[i] - X2[j])
                k[i, j] = self.sigma_f**2 * np.exp(
                    -(diff**2) / (2 * self.l**2))

        return k

    def predict(self, X_s):
        """Predicts mean and standard deviation"""

        Kernel_s = self.kernel(X_s, self.X)

        Kernel_s_s = self.kernel(X_s, X_s)

        Kernel_inv = np.linalg.inv(self.K)

        mu_s = Kernel_s.dot(Kernel_inv).dot(self.Y).reshape(-1)

        sigma_s = Kernel_s_s - Kernel_s.dot(Kernel_inv).dot(Kernel_s.T)

        return mu_s, np.sqrt(np.diag(sigma_s))
