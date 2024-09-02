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

    if not isinstance(X, np.ndarray) or len(X) > 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    
    if len(X) < 2:
        raise ValueError("X must contain multiple data points")

    X_mean = np.mean(X, axis=0)

    return (np.array(X_mean, None))