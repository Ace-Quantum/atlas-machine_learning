#!/usr/bin/env python3
"""sparsity"""

import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims, lambtha):
    """Creates a sparse autoencoder"""
    # encoder
    in_layer = keras.Input(shape=(input_dims,))
    encoded = in_layer
    for n in hidden_layers:
        encoded = keras.layers.Dense(n, activation="relu")(encoded)

    # latent w/ L1
    late_layer = keras.layers.Dense(
        latent_dims,
        activation="relu",
        activity_regularizer=keras.regularizers.l1(lambtha),
    )(encoded)

    encoder = keras.Model(in_layer, late_layer)

    # decoder
    decoded_in_layer = keras.Input(shape=(latent_dims,))
    decoded = decoded_in_layer

    for n in reversed(hidden_layers):
        decoded = keras.layers.Dense(n, activation="relu")(decoded)

    output_layer = keras.layers.Dense(input_dims, activation="sigmoid")(decoded)

    decoder = keras.Model(decoded_in_layer, output_layer)

    # sparse autoencoder build
    autoencoder_in_layer = keras.Input(shape=(input_dims,))
    encoded_output_layer = encoder(autoencoder_in_layer)
    reconstructed_output_layer = decoder(encoded_output_layer)

    autoencoder = keras.Model(autoencoder_in_layer, reconstructed_output_layer)

    # compile
    autoencoder.compile(optimizer="adam", loss="binary_crossentropy")

    return encoder, decoder, autoencoder
