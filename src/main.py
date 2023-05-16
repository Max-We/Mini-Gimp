"""
Studienleistung 1 (Maximilian Weichart)

# Standardfilter:

- Threshold
- Brightness
- Contrast
- Blur
- Sharpen

Wahlpflichtfeatures:

- sinnvolle grafische Anzeige des Ergebnisses
- Farbkanäle vertauschen
- Erode / Dilate
"""
import click
from PIL import Image

from models import RGB
from ui import spawn_output_window
from util import apply_threshold, apply_brightness, apply_contrast, apply_blur, apply_sharpen, apply_swap_channels, \
    apply_erode, apply_dilate


@click.command()
@click.argument('image-path', type=click.types.Path(exists=True, dir_okay=False), required=True)
@click.option('--threshold', type=click.types.IntRange(0, 255), help='Applies a threshold filter to the image.')
@click.option('--brightness', type=click.types.IntRange(-255, 255), help='Modifies the brightness of the image.')
@click.option('--contrast', type=click.types.IntRange(-255, 255), help='Modifies the contrast of the image.')
@click.option('--blur', type=click.types.IntRange(0, 100), help='Applies a blur filter to the image.')
@click.option('--sharpen', type=click.types.IntRange(0, 100), help='Applies a sharpen filter to the image.')
@click.option('--swap-channels', nargs=2, type=click.types.Choice([e.name for e in RGB]), help='Swaps two channels of '
                                                                                               'an RGB image. '
                                                                                               'Example: '
                                                                                               '--swap-channels=r g.')
@click.option('--erode', is_flag=True, help='Applies erode to the image.')
@click.option('--dilate', is_flag=True, help='Applies dilate to the image.')
def edit(image_path, threshold, brightness, contrast, blur, sharpen, swap_channels, erode, dilate):
    image = Image.open(image_path)
    click.echo(f"Editing '{image_path}' ({image.mode})...")

    if threshold:
        click.echo("Applying threshold...")
        image = apply_threshold(image, threshold)
    if brightness:
        click.echo("Applying brightness...")
        image = apply_brightness(image, brightness)
    if contrast:
        click.echo("Applying contrast...")
        image = apply_contrast(image, contrast)
    if blur:
        click.echo("Applying blur...")
        image = apply_blur(image, blur)
    if sharpen:
        click.echo("Applying sharpen...")
        image = apply_sharpen(image, sharpen)
    if swap_channels:
        click.echo("Swapping channels...")
        image = apply_swap_channels(image, swap_channels)
    if erode:
        click.echo("Applying erode...")
        image = apply_erode(image)
    if dilate:
        click.echo("Applying dilate...")
        image = apply_dilate(image)

    spawn_output_window(image, image_path)


if __name__ == '__main__':
    edit()
