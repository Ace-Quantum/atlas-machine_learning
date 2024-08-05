#!/usr/bin/env python3

"""Documentation"""

from tensorflow import keras as K


def lenet5(X):
    """Documentation"""
    initializer = K.initializers.he_normal(seed=0)

    conv1 = K.layers.Conv2D(6, (5, 5),
                            padding="same", kernel_initializer=initializer,
                            activation="relu")(X)

    pool1 = K.layers.MaxPooling2D((2, 2), strides=(2, 2))(conv1)

    conv2 = K.layers.Conv2D(
        16, (5, 5), padding="valid", kernel_initializer=initializer,
        activation="relu")(pool1)

    pool2 = K.layers.MaxPooling2D((2, 2), strides=(2, 2))(conv2)

    flat = K.layers.Flatten()(pool2)

    fc1 = K.layers.Dense(120, kernel_initializer=initializer,
                         activation="relu")(flat)

    fc2 = K.layers.Dense(84, kernel_initializer=initializer,
                         activation="relu")(fc1)

    output = K.layers.Dense(10, kernel_initializer=initializer,
                            activation="softmax")(fc2)

    model = K.models.Model(inputs=X, outputs=output)

    model.compile(
        optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
    )
    return model
