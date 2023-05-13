from PIL import Image


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

# Sharpen
