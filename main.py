import click

@click.command()
@click.argument('image', type=click.types.Path(exists=True, dir_okay=False), required=True)
@click.option('--threshold', type=click.types.IntRange(0, 255), help='Applies a threshold filter to the image.')
@click.option('--brightness', type=click.types.IntRange(-255, 255), help='Modifies the brightness of the image.')
@click.option('--contrast', type=click.types.IntRange(-255, 255), help='Modifies the contrast of the image.')
@click.option('--blur', type=click.types.IntRange(0, 100), help='Applies a blur filter to the image.')
@click.option('--sharpen', type=click.types.IntRange(0, 100), help='Applies a sharpen filter to the image.')
def edit(image, threshold, brightness, contrast, blur, sharpen):
    if threshold:
        print("Threshold")
    if brightness:
        print("Brightness")
    if contrast:
        print("Contrast")
    if blur:
        print("Blur")
    if sharpen:
        print("Sharpen")

if __name__ == '__main__':
    edit()