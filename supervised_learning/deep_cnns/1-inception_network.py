#!/usr/bin/env python3
"""Builds an inception network"""

from tensorflow import keras as K
inception_block = __import__('0-inception_block').inception_block


def inception_network():
    """Builds an inception block"""

    model_start = K.layers.Input(shape=(224, 224, 3))

    layers = K.layers.Conv2D(
        kernel_size=(7, 7),
        filters=64,
        strides=(2, 2),
        padding='same',
        activation='relu'
    )(model_start)

    layers = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same'
    )(layers)

    # Ok I think we need something else for these two layers

    layers = K.layers.Conv2D(
        filters=64,
        kernel_size=(1, 1),
        padding='same',
        activation='relu'
    )(layers)

    layers = K.layers.Conv2D(
        filters=192,
        kernel_size=(3, 3),
        padding='same',
        activation='relu'
    )(layers)

    # So I'm unsure what to do here

    layers = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same'
    )(layers)

    layers = (inception_block(layers, [64, 96, 128, 16, 32, 32]))

    layers = (inception_block(layers, [128, 128, 192, 32, 96, 64]))

    layers = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same'
    )(layers)

    layers = (inception_block(layers, [192, 96, 208, 16, 48, 64]))

    layers = (inception_block(layers, [160, 112, 224, 24, 64, 64]))

    layers = (inception_block(layers, [128, 128, 256, 24, 64, 64]))

    layers = (inception_block(layers, [112, 144, 288, 32, 64, 64]))

    layers = (inception_block(layers, [256, 160, 320, 32, 128, 128]))

    layers = K.layers.MaxPooling2D(
        pool_size=(3, 3),
        strides=(2, 2),
        padding='same'
    )(layers)

    layers = (inception_block(layers, [256, 160, 320, 32, 128, 128]))

    layers = (inception_block(layers, [384, 192, 384, 48, 128, 128]))

    layers = K.layers.AveragePooling2D(
        pool_size=(7, 7),
    )(layers)

    # flat_1 = K.layers.Flatten()(layers)

    dropout_layer = K.layers.Dropout(.4)(layers)

    dense_layer = K.layers.Dense(1000, activation='softmax')(dropout_layer)

    # softmax_layer = K.layers.Softmax()(dense_layer)

    return K.models.Model(model_start, dense_layer)
