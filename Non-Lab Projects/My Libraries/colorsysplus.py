"""
Lines A: These 2 lines of code are rewritten and slightly altered from
    https://stackoverflow.com/questions/36386627/how-to-divide-each-element-in-a-tuple-by-a-single-integer,
    in the second example of the first answer in the page.

Line B: This line of code is rewritten from https://www.geeksforgeeks.org/python-addition-of-tuples/,
    in the second method of the page.
"""

# Importing libraries
from colorsys import *


def increment_hue(color, increment: float):
    """
    Increments a 0 ~ 255 RGB color's hue.

    :param color: color you want to have hue incremented.
    :param increment: amount hue is incremented by. 0 = same hue, 1/2 = -1/2 = opposite hue on the color wheel, etc.
    :return: new color with hue incremented.
    """
    # Converting from 0 ~ 255 range to 0 ~ 1 range
    color = tuple(x / 255 for x in color)  # *** A ***

    # Converting from RGB to HLS color
    color = rgb_to_hls(color[0], color[1], color[2])

    # Incrementing the color's hue
    color = tuple(map(sum, zip(color, (increment, 0, 0))))  # *** B ***

    # Converting from HLS to RGB color
    color = hls_to_rgb(color[0], color[1], color[2])

    # Converting from 0 ~ 1 range to 0 ~ 255 range
    color = tuple(x * 255 for x in color)  # *** A ***

    # Returning the new color
    return color
