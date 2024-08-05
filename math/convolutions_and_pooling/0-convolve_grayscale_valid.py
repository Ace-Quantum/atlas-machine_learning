#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Documentation"""

    m, h, w = images.shape
    kh, kw = kernel.shape

    output_h = h - kh + 1
    output_w = w - kw + 1

    con_images = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            con_images[:, i, j] = np.sum(
                images[:, i:i+kh, j:j+kw] * kernel, axis=(1, 2)
            )

    return con_images
