#!/usr/bin/env python3

"""Documentation"""

import tensorflow.keras as K


def save_model(network, filename):

    """Documentation"""
    network.save(filename)


def load_model(filename):

    """Documentation"""
    return K.models.load_model(filename)
