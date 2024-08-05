#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """Documentation"""
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    pad_images = np.pad(images, ((0, 0), (ph, ph), (
        pw, pw)), mode='constant')

    output_h = h + 2 * ph - kh + 1
    output_w = w + 2 * pw - kw + 1

    con_images = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            con_images[:, i, j] = np.sum(
                pad_images[:, i:i+kh, j:j+kw] * kernel, axis=(1, 2)
            )

    return con_images
