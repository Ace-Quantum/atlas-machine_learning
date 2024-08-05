#!/usr/bin/env python3

import numpy as np
convolve_grayscale_valid = __import__('0-convolve_grayscale_valid').convolve_grayscale_valid

if __name__ == "__main__":
    # Example grayscale images
    images = np.random.rand(5, 10, 10)  # 5 images of size 10x10
    # Example kernel
    kernel = np.random.rand(3, 3)  # 3x3 kernel
    
    convolved_images = convolve_grayscale_valid(images, kernel)
    print(convolved_images)