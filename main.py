import click
from PIL import Image

from models import RGB
from util import apply_threshold, apply_brightness, apply_contrast, apply_blur, apply_sharpen, apply_swap_channels


@click.command()
@click.argument('image-path', type=click.types.Path(exists=True, dir_okay=False), required=True)
@click.option('--threshold', type=click.types.IntRange(0, 255), help='Applies a threshold filter to the image.')
@click.option('--brightness', type=click.types.IntRange(-255, 255), help='Modifies the brightness of the image.')
@click.option('--contrast', type=click.types.IntRange(-255, 255), help='Modifies the contrast of the image.')
@click.option('--blur', type=click.types.IntRange(0, 100), help='Applies a blur filter to the image.')
@click.option('--sharpen', type=click.types.IntRange(0, 100), help='Applies a sharpen filter to the image.')
@click.option('--swap-channels', nargs=2, type=click.types.Choice([e.name for e in RGB]), help='Swaps two channels of an RGB image. Example: --swap-channels=r g.')
def edit(image_path, threshold, brightness, contrast, blur, sharpen, swap_channels):
    image = Image.open(image_path)

    if threshold:
        image = apply_threshold(image, threshold)
    if brightness:
        image = apply_brightness(image, brightness)
    if contrast:
        image = apply_contrast(image, contrast)
    if blur:
        image = apply_blur(image, blur)
    if sharpen:
        image = apply_sharpen(image, sharpen)
    if swap_channels:
        image = apply_swap_channels(image, swap_channels)

    image.save("example_out.png")

if __name__ == '__main__':
    edit()