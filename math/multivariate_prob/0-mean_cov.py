#!/usr/bin/env python3
"""This is a module for finding the mean and covariance 
of a data set in NumPy
This module uses code found in the following link:
https://python.plainenglish.io/covariance-calculation-using-python-45b6a8e5df9f"""

import numpy as np

def cov_val(x, y):
    """Helper to find the covariance"""
    
    mean_x = sum(x) / float(len(x))
    mean_y = sum(y) / float(len(y))

    sub_x = [i - mean_x for i in x]
    sub_y = [i - mean_y for i in y]

    sum_value = sum([sub_y[i]*sub_x[i] for i in range(len(x))])
    denom = float(len(x)-1)

    cov = sum_value/denom
    return cov

def mean_cov(X):
    """The function that runs the module"""

    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    
    if len(X) < 2:
        raise ValueError("X must contain multiple data points")

    X_mean = np.mean(X, axis=0)

    # X_mean = np.asarray(X_mean)

    X_cov = [[cov_val(a,b) for a in X] for b in X]

    return X_mean, X_cov