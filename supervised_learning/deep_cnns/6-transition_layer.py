#!/usr/bin/env python3
"""Builds a transitional layer"""

from tensorflow import keras as K


def transitional_layer(X, nb_filters, compression):
    """Builds a transitional layer"""
