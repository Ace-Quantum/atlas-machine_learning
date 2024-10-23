#!/usr/bin/env python3
"""convoluted"""

import tensorflow.keras as keras


def autoencoder(input_dims, filters, latent_dims):
    """Creates a convoluted autoencoder"""
    # encoder
    in_layer = keras.Input(shape=input_dims)
    encoded = in_layer
    for f in filters:
        encoded = keras.layers.Conv2D(
            f, (3, 3), padding="same", activation="relu")(encoded)

        encoded = keras.layers.MaxPooling2D(pool_size=(2, 2))(encoded)

    latent = encoded
    # encoded = keras.layers.Conv2D(
        # latent_dims[0], (3, 3), padding="valid")(encoded)

    encoder = keras.Model(in_layer, latent)

    # decoder
    decoded_in_layer = keras.Input(shape=latent_dims)
    decoded = decoded_in_layer

    for f in reversed(filters[:-1]):
        decoded = keras.layers.Conv2D(
            f, (3, 3), padding="same", activation="relu")(decoded)
        decoded = keras.layers.UpSampling2D(size=(2, 2))(decoded)

    decoded = keras.layers.Conv2D(
        filters[0], (3, 3), padding="valid", activation="relu"
    )(decoded)

    out_layer = keras.layers.Conv2D(
        input_dims[-1], (3, 3), padding="same", activation="sigmoid"
    )(decoded)

    decoder = keras.Model(decoded_in_layer, out_layer)

    autoencoder_in = keras.Input(shape=input_dims)
    encoded_out = encoder(autoencoder_in)
    reconstructed_out = decoder(encoded_out)

    autoencoder = keras.Model(autoencoder_in, reconstructed_out)

    # compile
    autoencoder.compile(optimizer="adam", loss="binary_crossentropy")

    return encoder, decoder, autoencoder
