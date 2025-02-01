#!/usr/bin/env python3

"""I'm gonna go out on a limb
and say that this is going to be as easy as this
https://www.tensorflow.org/api_docs/python/tf/image/rot90"""

import tensorflow as tf


def rotate_image(image):
    """Rotates an image"""
    return tf.image.rot90(image)
