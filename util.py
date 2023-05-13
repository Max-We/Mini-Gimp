from PIL import Image

from kernels import create_blur_kernel, create_sharpen_kernel


# Threshold
def apply_threshold(image: Image, value: int) -> Image:
    img = image.convert("L").copy()
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y)) < value:
                new_value = 0
            else:
                new_value = 255
            img.putpixel((x, y), new_value)

    return img


# Brightness
def apply_brightness(image: Image, value: int) -> Image:
    img = image.copy()
    for x in range(img.width):
        for y in range(img.height):
            channels = list(img.getpixel((x, y)))
            img.putpixel((x, y), tuple([c + value for c in channels]))

    return img


# Contrast
# https://www.perplexity.ai/search/8a122732-bffb-4b6f-a0db-18c5b3555a18?s=t
def apply_contrast(image, value):
    img = image.copy()
    factor = (259 * (value + 255)) / (255 * (259 - value))
    for x in range(img.width):
        for y in range(img.height):
            channels = list(img.getpixel((x, y)))
            channels = [round(factor * (c - 128) + 128) for c in channels]
            img.putpixel((x, y), tuple(channels))

    return img

# Blur
def apply_blur(image, strength):
    # Input is 0-100 but everything above 10 is unusable
    normalized_strength = round(strength / 10)
    kernel, kernel_size = create_blur_kernel(normalized_strength)
    return _apply_kernel(image, kernel, kernel_size)

# Sharpen
def apply_sharpen(image, strength):
    # Input is 0-100 but everything above 5 is unusable
    normalized_strength = strength / 20
    kernel, kernel_size = create_sharpen_kernel(normalized_strength)
    return _apply_kernel(image, kernel, kernel_size)


def _apply_kernel(image, kernel, kernel_size):
    w, h = image.size
    # `k` is used to make the filter stop at the edge of the image
    # In a future version, padding / mirroring of the image would be nice to have for better result
    k = kernel_size//2
    img_out = image.copy()

    # Iterate all pixels of the image
    for x in range(1, w - k):
        for y in range(1, h - k):
            channels_out = [0 for _ in img_out.getbands()]
            # Iterate over the surrounding of the pixel
            for i in range(kernel_size):
                for j in range(kernel_size):
                    # Iterate all channels of the pixel and calculate the result
                    channels_in = list(image.getpixel((x - k + i, y - k + j)))
                    for c in range(len(channels_in)):
                        channels_out[c] += int(channels_in[c] * kernel[i][j])
            img_out.putpixel((x, y), tuple(channels_out))

    return img_out
