# Threshold
def threshold(image, value):
    img = image.copy()
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y)) < value:
                new_value = 0
            else:
                new_value = 255
            img.putpixel((x, y), new_value)
    return img

# Brightness

# Contrast

# Blur

# Sharpen
