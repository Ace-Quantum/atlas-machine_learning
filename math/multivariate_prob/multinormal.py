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

        self.mean = np.mean(data, axis=0)
