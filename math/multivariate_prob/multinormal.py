#!/usr/bin/env python3
"""This will be used to represent a Multivariate Normal Distribution"""

import numpy as np

class MultiNormal:
    def __init__(self, data):
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        
        if len(data[1]) < 2:
            raise ValueError("data must contain multiple data points")