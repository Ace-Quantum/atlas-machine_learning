#!/usr/bin/env python3
"""Class construction for RNNcells"""

import numpy as np


class RNNCell:
    """Cell class for RNN cells
    I'm actually not sure yet how these are different
    than normal NN cells
    But that's what this project aims to teach us"""
    def __init__(self, i, h, o):
        """Initialization
        i - dimensionality of data
        h - dimensionality of the hidden state
        o - dimensionality of outputs
        Wh - concatinated hidden state/input data weight
        bh - concatinated hidden state/input data bias
        Wy - output weight
        by - output bias
        Initialized in random normal distribution
        Weights used on the right side of matrix multiplication
        Biases initialized to zero"""

        
        

    def forward(self, h_prev, x_t):
        """Forward propogation"""
        return None
