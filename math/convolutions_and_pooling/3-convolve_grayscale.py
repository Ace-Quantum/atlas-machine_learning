#!/usr/bin/env python3
"""Documentation"""


import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """Documentation"""

    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride

    if padding == 'same':
        pad_h = (sh * (h - 1) + kh - h) // 2
        pad_w = (sw * (w - 1) + kw - w) // 2
    elif padding == 'valid':
        pad_h, pad_w = 0, 0
    else:
        pad_h, pad_w = padding

    pad_images = np.pad(images, ((0, 0), (pad_h, pad_h),
                                 (pad_w, pad_w)), mode='constant')

    output_h = (h + 2 * pad_h - kh) // sh + 1
    output_w = (w + 2 * pad_w - kw) // sw + 1

    con_images = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            st_i = i * sh
            st_j = j * sw
            end_i = st_i + kh
            end_j = st_j + kw

            con_images[:, i, j] = np.sum(
                pad_images[:, st_i:end_i, st_j:end_j] * kernel, axis=(1, 2)
            )

    return con_images
