#!/usr/bin/env python3
"""Documentation"""

import tensorflow.keras as K

# import tensorflow as tf


def build_model(nx, layers, activations, lambtha, keep_prob):
    """Documentation"""
    # shape = (None, nx
    model = K.models.Sequential()

    # l2 = regularizer l2=lambtha
    l2 = K.regularizers.l2(lambtha)

    # define first layer as before, but with input shape
    model.add(
        K.layers.Dense(
            units=layers[0],
            activation=activations[0],
            kernel_regularizer=l2,
            input_shape=(nx,),
        )
    )

    if len(layers) > 1:
        model.add(K.layers.Dropout(rate=1 - keep_prob))

    for i in range(1, len(layers)):
        model.add(
            K.layers.Dense(
                units=layers[i],
                activation=activations[i],
                kernel_regularizer=l2,
            )
        )

        if i < len(layers) - 1:
            model.add(K.layers.Dropout(rate=1 - keep_prob))

    # model.compile(optimizer="adam", loss="mean_squared_error")

    return model
