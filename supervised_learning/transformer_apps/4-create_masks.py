#!/usr/bin/env python3
# Only allowed tensorflow

"""Definition for creating masks"""

import tensorflow as tf

def create_masks(inputs, target):
    """Creates masks"""

    encoder_mask = tf.cast(tf.math.equal(inputs, 0), tf.float32)
    encoder_mask = encoder_mask[:, tf.newaxis, tf.newaxis, :]

    decoder_padding_mask = tf.cast(tf.math.equal(target, 0), tf.float32)
    decoder_padding_mask = decoder_padding_mask[:, tf.newaxis, tf.newaxis, :]

    len_out = tf.shape(target)[1]
    l_a_mask = 1 - tf.linalg.band_part(tf.ones((len_out, len_out)), -1, 0)

    comb = tf.maximum(l_a_mask, decoder_padding_mask[:, tf.newaxis, :, :])

    decoder_mask = encoder_mask

    return encoder_mask, comb, decoder_mask