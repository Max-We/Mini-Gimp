import click
from PIL import Image

from util import apply_threshold, apply_brightness, apply_contrast


@click.command()
@click.argument('image-path', type=click.types.Path(exists=True, dir_okay=False), required=True)
@click.option('--threshold', type=click.types.IntRange(0, 255), help='Applies a threshold filter to the image.')
@click.option('--brightness', type=click.types.IntRange(-255, 255), help='Modifies the brightness of the image.')
@click.option('--contrast', type=click.types.IntRange(-255, 255), help='Modifies the contrast of the image.')
@click.option('--blur', type=click.types.IntRange(0, 100), help='Applies a blur filter to the image.')
@click.option('--sharpen', type=click.types.IntRange(0, 100), help='Applies a sharpen filter to the image.')
def edit(image_path, threshold, brightness, contrast, blur, sharpen):
    image = Image.open(image_path)

    if threshold:
        image = apply_threshold(image, threshold)
    if brightness:
        image = apply_brightness(image, brightness)
    if contrast:
        image = apply_contrast(image, contrast)
    if blur:
        print("Blur")
    if sharpen:
        print("Sharpen")

    image.save("example_out.png")

if __name__ == '__main__':
    edit()