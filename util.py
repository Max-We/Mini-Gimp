import numpy as np
from PIL import Image

from kernels import create_blur_kernel, create_sharpen_kernel, cross_kernel
from models import RGB


# Applies the threshold function to an image (only BW)
def apply_threshold(image, value):
    img = image.convert("L").copy()
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y)) < value:
                new_value = 0
            else:
                new_value = 255
            img.putpixel((x, y), new_value)

    return img


# Changes the brightness of an image
def apply_brightness(image, value):
    img = image.copy()
    for x in range(img.width):
        for y in range(img.height):
            channels = np.atleast_1d(img.getpixel((x, y)))
            img.putpixel((x, y), tuple([int(c + value) for c in channels]))

    return img


# Changes the contrast of an image
# https://www.perplexity.ai/search/8a122732-bffb-4b6f-a0db-18c5b3555a18?s=t
def apply_contrast(image, value):
    img = image.copy()
    factor = (259 * (value + 255)) / (255 * (259 - value))
    for x in range(img.width):
        for y in range(img.height):
            channels = np.atleast_1d(img.getpixel((x, y)))
            channels = [round(factor * (c - 128) + 128) for c in channels]
            img.putpixel((x, y), tuple(channels))

    return img


# Swaps channels of an RGB image
def apply_swap_channels(image, swap_channels):
    img = image.copy().convert("RGB")
    c1, c2 = [RGB[c].value for c in swap_channels]

    for x in range(img.width):
        for y in range(img.height):
            channels = list(img.getpixel((x, y)))
            # Syntax from ChatGPT
            channels[c1], channels[c2] = channels[c2], channels[c1]
            channels = tuple(channels)

            img.putpixel((x, y), channels)
    return img


# Applies erosion to the image
def apply_erode(image):
    return _apply_erode_dilate(image, "erode")


# Applies dilation to the image
def apply_dilate(image):
    return _apply_erode_dilate(image, "dilate")


# Applies erosion / dilation to the image
# https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html
def _apply_erode_dilate(image, mode):
    w, h = image.size
    img_out = image.copy()
    n_channels = len(img_out.getbands())

    kernel_size = 3
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            # Naming for variable from https://www.perplexity.ai/search/7e0e61da-bd66-49b6-94e7-29ee46d41a17?s=t
            # Result: ks x ks x channels
            receptive_field = np.zeros((kernel_size, kernel_size, n_channels))

            # Get values for receptive field
            for i in range(kernel_size):
                for j in range(kernel_size):
                    receptive_field[i][j] = image.getpixel((x - 1 + i, y - 1 + j)) if cross_kernel[i][j] == 1 else (
                        [None for _ in range(n_channels)])

            # Apply effect to each channel individually
            # Idea for applying on each channel individually: https://stackoverflow.com/a/43535662
            pixel_updated = [0 for _ in range(n_channels)]
            for c in range(receptive_field.shape[-1]):
                channel_pixels = receptive_field[:, :, c]
                # Choose minimum / maximum value
                if mode == "erode":
                    pixel_updated[c] = int(np.nanmin(channel_pixels))
                elif mode == "dilate":
                    pixel_updated[c] = int(np.nanmax(channel_pixels))
                else:
                    print(f"Unknown edit mode '{mode}' (only 'erode', 'dilate' allowed).")
                    return image

            img_out.putpixel((x, y), tuple(pixel_updated))
    return img_out


# Applies a simple box-blur filter to the image
def apply_blur(image, strength):
    # Input is 0-100 but everything above 10 is unusable, therefore it should be normalized for usability
    normalized_strength = round(strength / 10)
    kernel, kernel_size = create_blur_kernel(normalized_strength)
    return _apply_kernel(image, kernel, kernel_size)


# Applies a simple sharpen filter to the image
def apply_sharpen(image, strength):
    # Input is 0-100 but everything above 5 is unusable, therefore it should be normalized for usability
    normalized_strength = strength / 20
    kernel, kernel_size = create_sharpen_kernel(normalized_strength)
    return _apply_kernel(image, kernel, kernel_size)

# Applies a kernel to the input image
def _apply_kernel(image, kernel, kernel_size):
    w, h = image.size
    # `k` is used to make the filter stop at the edge of the image
    # In a future version, padding / mirroring of the image would be nice to have for better result
    k = kernel_size // 2
    img_out = image.copy()

    # Iterate all pixels of the image
    for x in range(1, w - k):
        for y in range(1, h - k):
            channels_out = [0 for _ in img_out.getbands()]
            # Iterate over the surrounding of the pixel
            for i in range(kernel_size):
                for j in range(kernel_size):
                    # Iterate all channels of the pixel and calculate the result
                    # The `np.atleast_1d` functionality was found using ChatGPT
                    channels_in = np.atleast_1d(image.getpixel((x - k + i, y - k + j))).astype(float)
                    for c in range(channels_in.size):
                        channels_out[c] += int(channels_in[c] * kernel[i][j])
            img_out.putpixel((x, y), tuple(channels_out))

    return img_out
