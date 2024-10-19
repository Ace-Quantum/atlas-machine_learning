#!/usr/bin/env python3

"""This program is a vanilla autoencoder
for the purposes of compressing and decompressing data"""

import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """Encodes and decodes"""
    # the encoder protion
    in_layer = keras.Input(shape=(input_dims,))

    encoded_layer = in_layer

    for n in hidden_layers:
        encoded_layer = keras.layers.Dense(n, activation="relu")(encoded_layer)

    latent = keras.layers.Dense(latent_dims, activation="relu")(encoded_layer)

    encoded_layer = keras.Model(in_layer, latent)

    # the decoder portion
    decoded_in_layer = keras.Input(shape=(latent_dims,))

    decoded = decoded_in_layer
    for n in reversed(hidden_layers):
        decoded = keras.layers.Dense(n, activation="relu")(decoded)

    output_layer = keras.layers.Dense(input_dims, activation="sigmoid")(decoded)

    decoder = keras.Model(decoded_in_layer, output_layer)

    # All together now
    auto_input = keras.Input(shape=(input_dims,))
    encoded_output = encoded_layer(auto_input)
    reconstructed_output = decoder(encoded_output)

    autoencoder = keras.Model(auto_input, reconstructed_output)

    autoencoder.compile(optimizer="adam", loss="binary_crossentropy")

    return encoded_layer, decoder, autoencoder
