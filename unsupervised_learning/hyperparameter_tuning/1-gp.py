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
        self.K = None

        def kernel(self, X1, X2):
            """Return covariance matrix"""
            return None

        def predict(self, X_s):
            """predicts the mean and st.dev of points
            in a Gaussian process"""
            return None
