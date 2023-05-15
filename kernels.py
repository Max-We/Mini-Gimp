import numpy as np

# https://en.wikipedia.org/wiki/Kernel_(image_processing)
def create_blur_kernel(kernel_size):
    non_normalized = np.ones((kernel_size, kernel_size))
    return non_normalized / np.sum(non_normalized), kernel_size

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

kernel_erode = np.array([[0, 1, 0],
                         [1, 1, 1],
                         [0, 1, 0]])

