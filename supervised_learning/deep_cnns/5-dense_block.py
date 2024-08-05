#!/usr/bin/env python3
"""Builds a dense block"""
"""This is code from a tutorial from
https://towardsdatascience.com/exploring-densenets-from-paper-to-keras-dcc01725488b"""

from tensorflow import keras as K

# I honestly don't know what I'm doing here anymore

def dense_block(X, nb_filters, growth_rate, layers):
    """Builds a dense block"""
    # X - The output from the previous layer
    # nb_filters - the number of filters in X
    # growth_rate - self explanitory
    # layers - number of layers

    # x = K.layers.BatchNormalization()(X)
    # x = K.layers.Activation('relu')(x)

    for i in range(layers):
        y = K.layers.BatchNormalization()(X)
        y = K.layers.Activation('relu')(y)
        y = K.layers.Conv2D(filters=growth_rate * (i + 1),
                            kernel_size=3,
                            padding='same',
                            kernel_initializer=K.initializers.HeNormal(seed=0))(y)
        
        x = K.layers.concatenate([x, y])

        nb_filters += growth_rate

    return x, nb_filters
