#!/usr/bin/env python3

"""I'm gonna go out on a limb
and say that this is going to be as easy as this
https://www.tensorflow.org/api_docs/python/tf/image/random_crop"""

import tensorflow as tf


def crop_image(image, size):
    """Crops an image"""
    return tf.image.random_crop(image, size)
