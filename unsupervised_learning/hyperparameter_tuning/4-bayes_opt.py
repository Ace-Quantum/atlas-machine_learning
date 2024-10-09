#!/usr/bin/env python3
"""creates the class for a
Bayesian Optimization"""

import numpy as np

GP = __import__('2-gp').GaussianProcess
from scipy.stats import norm


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

        self.f = f
        self.gp = GP(X_init, Y_init, l=l, sigma_f=sigma_f)
        self.l = l
        self.X_s = np.linspace(bounds[0], bounds[1], ac_samples).reshape(-1, 1)
        self.xsi = xsi
        self.minimize = minimize

    def acquisition(self):
        mu_s = self.gp.predict(self.X_s)[0]

        sigma_s = self.gp.predict(self.X_s)[1]

        Exp_Imp = mu_s - self.xsi + sigma_s * norm.cdf((self.xsi - mu_s) / sigma_s)

        max_Exp_Imp_idx = np.argmax(Exp_Imp)

        X_next = self.X_s[max_Exp_Imp_idx]

        return X_next, Exp_Imp
