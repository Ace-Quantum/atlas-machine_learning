#!/usr/bin/env python3
"""This is a module for finding the mean and covariance 
of a data set in NumPy
This module uses code found in the following link:
https://python.plainenglish.io/covariance-calculation-using-python-45b6a8e5df9f"""

import numpy as np

def cov_val(x, y):
    """Helper to find the covariance"""
    
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    sub_x = x - mean_x
    sub_y = y - mean_y

    cov = np.dot(sub_x, sub_y) / (len(x) - 1)

    return cov

def mean_cov(X):
    """The function that runs the module"""

    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    
    if len(X) < 2:
        raise ValueError("X must contain multiple data points")

    X_mean = np.mean(X, axis=0)

    X_mean = np.array(X_mean)

    X_cov = np.zeros((X.shape[1], X.shape[1]))

    for i in range(X.shape[1]):
        for j in range(i, X.shape[1]):
            comb_cov = cov_val(X[:, i], X[:, j])

            X_cov[i, j] = comb_cov
            X_cov[j, i] = comb_cov

    X_mean = X_mean.reshape(1, -1)

    return X_mean, X_cov