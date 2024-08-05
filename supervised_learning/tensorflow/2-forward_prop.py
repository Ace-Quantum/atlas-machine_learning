#!/usr/bin/env python3


"""Idk where to put documentation"""

create_layer = __import__("1-create_layer").create_layer

"""Idk where to put documentation"""


def forward_prop(x, layer_sizes=[], activations=[]):
    """Idk where to put documentation"""
    prev_layer = x

    for size, activation in zip(layer_sizes, activations):
        prev_layer = create_layer(prev_layer, size, activation)

    return prev_layer
