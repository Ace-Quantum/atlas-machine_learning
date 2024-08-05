#!/usr/bin/env python3
"""Builds an identity block"""

from tensorflow import keras as K


def identity_block(A_prev, filters):
    """Builds an identity block"""

    input_shortcut = A_prev

    layer = K.layers.Conv2D(
        filters=filters[0],
        kernel_size=(1, 1),
        padding="same",
        kernel_initializer=K.initializers.glorot_uniform(seed=0),
    )(A_prev)

    layer = K.layers.BatchNormalization(axis=3)(layer)
    layer = K.layers.Activation("relu")(layer)

    layer = K.layers.Conv2D(
        filters=filters[1],
        kernel_size=(3, 3),
        padding="same",
        kernel_initializer=K.initializers.glorot_uniform(seed=0),
    )(layer)

    layer = K.layers.BatchNormalization(axis=3)(layer)
    layer = K.layers.Activation("relu")(layer)

    layer = K.layers.Conv2D(
        filters=filters[2],
        kernel_size=(1, 1),
        padding="same",
        kernel_initializer=K.initializers.glorot_uniform(seed=0),
    )(layer)

    layer = K.layers.BatchNormalization(axis=3)(layer)

    layer = K.layers.Add()([layer, input_shortcut])
    layer = K.layers.Activation("relu")(layer)

    return layer
