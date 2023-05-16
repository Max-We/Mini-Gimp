import numpy as np


# Creates a blur kernel with various strength (achieved by scaling its size)
# https://en.wikipedia.org/wiki/Kernel_(image_processing)
def create_blur_kernel(kernel_size):
    non_normalized = np.ones((kernel_size, kernel_size))
    return non_normalized / np.sum(non_normalized), kernel_size


# Creates a sharpen kernel with varying strength
# https://en.wikipedia.org/wiki/Kernel_(image_processing)
# https://www.taylorpetrick.com/blog/post/convolution-part3#sharpen
def create_sharpen_kernel(strength):
    ones = np.array([[0, 0, 0],
                     [0, 1, 0],
                     [0, 0, 0]])
    laplace = np.array([[0, -1, 0],
                        [-1, 4, -1],
                        [0, -1, 0]])
    return ones + laplace * strength, 3


# Kernel used for dilation / erosion
cross_kernel = np.array([[0, 1, 0],
                         [1, 1, 1],
                         [0, 1, 0]])
