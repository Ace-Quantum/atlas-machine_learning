#!/usr/bin/env python3

"""Idk where to put documentation"""
import tensorflow.compat.v1 as tf

tf.disable_eager_execution()


"""Idk where to put documentation"""


def calculate_accuracy(y, y_pred):
    """Idk where to put documentation"""
    y = tf.cast(y, tf.int32)
    # y_pred = tf.argmax(y_pred, axis=1)

    correct_predictions = tf.equal(tf.argmax(y, axis=1), tf.argmax(y_pred, axis=1))

    accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

    return accuracy
