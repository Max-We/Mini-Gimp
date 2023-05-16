# Mini-GIMP

Mini-GIMP is a small py project that implements some features to edit images from scratch.

![](showcase.webm)

```text
Usage: main.py [OPTIONS] IMAGE_PATH

Options:
  --threshold INTEGER RANGE   Applies a threshold filter to the image.
                              [0<=x<=255]
  --brightness INTEGER RANGE  Modifies the brightness of the image.
                              [-255<=x<=255]
  --contrast INTEGER RANGE    Modifies the contrast of the image.
                              [-255<=x<=255]
  --blur INTEGER RANGE        Applies a blur filter to the image.  [0<=x<=100]
  --sharpen INTEGER RANGE     Applies a sharpen filter to the image.
                              [0<=x<=100]
  --swap-channels [r|g|b]...  Swaps two channels of an RGB image. Example:
                              --swap-channels=r g.
  --erode                     Applies erode to the image.
  --dilate                    Applies dilate to the image.
  --help                      Show this message and exit.
```

## Standardfilters

- Threshold
- Brightness
- Contrast
- Blur
- Sharpen

## Elective features

- UI for displaying the result
- Swap color-channels
- Erode / Dilate
