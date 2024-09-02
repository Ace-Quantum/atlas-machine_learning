#!/usr/bin/env python3
"""This will be used to represent a Multivariate Normal Distribution"""

import numpy as np


def cov_val(x, y):
    """Helper to find the covariance"""

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    sub_x = x - mean_x
    sub_y = y - mean_y

    cov = np.dot(sub_x, sub_y) / (len(x) - 1)

    return cov


class MultiNormal:
    """A class to hold the matrix mentioned above"""

    def __init__(self, data):
        """Initialization"""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        if len(data[0]) < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.zeros(data.shape[0])

        for i in range(data.shape[0]):
            self.mean[i] = np.mean(data[i], axis=0)

        self.mean = self.mean.reshape(-1, 1)

        self.cov = np.zeros((data.shape[0], data.shape[0]))

        for i in range(data.shape[0]):
            for j in range(data.shape[0]):
                comb_cov = cov_val(data[i, :], data[j, :])

                self.cov[i, j] = comb_cov
                self.cov[j, i] = comb_cov
