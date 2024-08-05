#!/usr/bin/env python3

"""Behold, documentation"""

import numpy as np


def normalization_constants(X):
    """I should at some point put effort into documentation"""

    mean_vals = np.mean(X, axis=0)
    standard_vals = np.std(X, axis=0)

    return mean_vals, standard_vals
