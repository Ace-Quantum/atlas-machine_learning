#!/usr/bin/env python3

from tensorflow import keras as K

inception_network = __import__('1-inception_network').inception_network

if __name__ == '__main__':
    model = inception_network()
    model.summary()