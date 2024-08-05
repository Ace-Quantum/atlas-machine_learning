#!/usr/bin/env python3

"""Performs Backwards Prop with Pooling"""

import numpy as np

"""Variables:
dA: numpy array containing partial derivatives respective to pooling output
A_prev: contains output of previous layer
kernel_shape: the shape of the pooling kernel
stride: measure of how far and the kernel moves about the output.
mode: determines type of pooling
reterns partial derivatives in respect to the previous layer"""


def pool_backward(dA, A_prev, kernel_shape, stride=(1, 1), mode="max"):
    """Idk what you expect here I put all the notes above"""
    # Grabbing the new dimensions of the to-be return array
    m, h_new, w_new, c_new = dA.shape
    # Grabbing the shape of the previous layer
    # I'm not actually sure I need these though
    _, h_prev, w_prev, _ = A_prev.shape
    # Grabbing the dimensions of the kernel
    # Also not sure we need these either tbh
    kh, kw = kernel_shape
    # Grabbing the dimensions of the stride
    sh, sw = stride

    # Setting up dA_prev with the matching dimension of the previous output
    dA_prev = np.zeros_like(A_prev)

    # determine the new dimensions of the output
    # I need clarification on this
    # h_out = int((h_prev - kh) / sh) + 1
    # w_out = int((w_prev - kw) / sw) + 1

    # Iterate through the training input
    for i in range(m):
        # Grab each input individually
        # a_prev = A_prev[i]

        # work through the height of what will be our return
        for h in range(h_new):

            # work through the width of what will be our return
            for w in range(w_new):

                # work through the channels of what will be our return
                for c in range(c_new):

                    # defining slice dimensions

                    # vertical start and stop
                    # in regards to our output height,
                    # the height of our stride,
                    # and the kernel height:
                    vertical_start = h * sh
                    vertical_end = vertical_start + kh

                    # Horizontal start and stop, determined in the same way
                    horizontal_start = w * sw
                    horizontal_end = horizontal_start + kw

                    # determine pooling method
                    if mode == "max":
                        # pull the slice of output from a_prev
                        # Why is the end a colon?
                        a_prev_slice = A_prev[
                            i,
                            vertical_start:vertical_end,
                            horizontal_start:horizontal_end,
                            c,
                        ]

                        # load the mask array with zeroes
                        mask = a_prev_slice == np.max(a_prev_slice)

                        # Assign the values to the return statement,
                        # applying the mask to the derivitives
                        dA_prev[
                            i,
                            vertical_start:vertical_end,
                            horizontal_start:horizontal_end,
                            c,
                        ] += (
                            mask * dA[i, h, w, c]
                        )

                    elif mode == "avg":
                        # In the instance of instead wanting an average pooling
                        # we simply pull the individual derivitive
                        # and apply the average to the layer.
                        da = dA[i, h, w, c]

                        dA_prev[
                            i,
                            vertical_start:vertical_end,
                            horizontal_start:horizontal_end,
                            c,
                        ] += da / (kh * kw)

    return dA_prev
