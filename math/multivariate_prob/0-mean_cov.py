#!/usr/bin/env python3
"""This is a module for finding the mean and covariance 
of a data set in NumPy"""

import numpy as np



def mean_cov(X):
    """The function that runs the module"""

    # num_data = X[0]
    # X_means = []

    # for i in range(len(num_data)):
    #     X_means.append(np.mean(X[i]))

    X_mean = np.mean(X, axis=0)
    # X_cov = np.cov(X, ddof=1)

    return (X_mean, None)