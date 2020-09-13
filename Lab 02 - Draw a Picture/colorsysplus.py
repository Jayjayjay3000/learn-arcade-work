"""
An expansion based off of colorsys
"""

import colorsys


def increment_hue(color, increment: float):
    color = [x / 255 for x in color]
    color = colorsys.rgb_to_hls(color[0], color[1], color[2])
    color = tuple(map(sum, zip(color, (increment, 0, 0))))
    color = colorsys.hls_to_rgb(color[0], color[1], color[2])
    color = [x * 255 for x in color]
    return color
