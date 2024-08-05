#!/usr/bin/env python3
"""Here's some documentation"""
import tensorflow as tf


def l2_reg_cost(cost, model):
    """And some more documentation"""
    l2_loss = tf.constant(0.0)
    layer_losses = []

    for layer in model.layers:
        if layer.__class__.__name__ == 'Dense':
            l2_loss = tf.reduce_sum(
                tf.square(layer.kernel)) + tf.reduce_sum(tf.square(layer.bias))
            layer_losses.append(l2_loss)

    total_cost = cost + tf.stack(layer_losses)

    return total_cost
