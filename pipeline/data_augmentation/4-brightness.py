#!/usr/bin/env python3

"""I'm gonna go out on a limb
and say that this is going to be as easy as this
https://www.tensorflow.org/api_docs/python/tf/image/adjust_brightness"""

import tensorflow as tf


def change_brightness(image, max_delta):
    """Changes Brightness of an image"""
    return tf.image.random_brightness(image, max_delta)
