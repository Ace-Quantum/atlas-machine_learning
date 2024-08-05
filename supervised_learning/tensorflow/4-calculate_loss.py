#!/usr/bin/env python3

"""Idk where to put documentation"""
import tensorflow.compat.v1 as tf

tf.disable_eager_execution()

"""Idk where to put documentation"""


def calculate_loss(y, y_pred):
    """Idk where to put documentation"""
    loss = tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_pred)

    mean_loss = tf.reduce_mean(loss)
    return mean_loss
