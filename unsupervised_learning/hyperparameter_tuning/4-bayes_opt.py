#!/usr/bin/env python3
"""creates the class for a
Bayesian Optimization"""

import numpy as np

GP = __import__("2-gp").GaussianProcess


class BayesianOptimization:
    """Beysianbby"""

    def __init__(
        self,
        f,
        X_init,
        Y_init,
        bounds,
        ac_samples,
        l=1,
        sigma_f=1,
        xsi=0.01,
        minimize=True,
    ):
        """Idk something is wrong here but I'm doing what I can"""
        self.f = f
        self.gp = GP(self)
        X_s = None
        xsi = None
        minimize = None

    def acquisition(self):
        """calculates the next best sample location"""
        return None
