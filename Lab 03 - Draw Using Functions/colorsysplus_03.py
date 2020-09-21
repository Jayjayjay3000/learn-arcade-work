# Importing libraries
import colorsys_03 as colorsys


def increment_hue(color, increment: float):
    """
    Increments a 0 ~ 255 RGB color's hue.

    :param color: color you want to have hue incremented.
    :param increment: amount hue is incremented by. 0 = same hue, 1/2 = -1/2 = opposite hue on the color wheel, etc.
    :return: new color with hue incremented.
    """
    # Converting from 0 ~ 255 range to 0 ~ 1 range
    color = [x / 255 for x in color]

    # Converting from RGB to HLS color
    color = colorsys.rgb_to_hls(color[0], color[1], color[2])

    # Incrementing the color's hue
    color = tuple(map(sum, zip(color, (increment, 0, 0))))

    # Converting from HLS to RGB color
    color = colorsys.hls_to_rgb(color[0], color[1], color[2])

    # Converting from 0 ~ 1 range to 0 ~ 255 range
    color = [x * 255 for x in color]

    # Returning the new color
    return color
