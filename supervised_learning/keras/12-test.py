#!/usr/bin/env python3

"""Documentation"""

import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """Documentation"""
    model = network
    loss, accuracy = model.evaluate(data, labels, verbose=verbose)
    return [loss, accuracy]
