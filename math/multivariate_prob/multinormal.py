#!/usr/bin/env python3
"""This will be used to represent a Multivariate Normal Distribution"""

import numpy as np


class MultiNormal:
    """A class to hold the matrix mentioned above"""

    def __init__(self, data):
        """Initialization"""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        if len(data[0]) < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.zeros(len(data))

        for i in range(len(data)):
            self.mean[i] = np.mean(data[i], axis=0)

        self.mean = self.mean.reshape(1, -1)

        self.cov = None