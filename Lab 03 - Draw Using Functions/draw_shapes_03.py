# Importing libraries
import arcade
import numpy as np
import colorsysplus_03 as colorsysplus


def horizontal_line(start_x: float, end_x: float, y: float, color, line_width: float = 1):
    """
    Draw a horizontal line. Good for saving space by cutting out a parameter.

    :param start_x: x position of line starting point.
    :param end_x: x position of line ending point.
    :param y: y position of line starting and ending points.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param line_width: Width of the line in pixels.
    """
    arcade.draw_line(start_x, y, end_x, y, color, line_width)


def cl_horizontal_line(center_x: float, length: float, y: float, color, line_width: float = 1):
    """
    Draw a horizontal line by specifying center point and length.

    :param center_x: x position of line center point.
    :param length: length of line.
    :param y: y position of line starting and ending points.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param line_width: Width of the line in pixels.
    """
    arcade.draw_line(center_x - length / 2, y, center_x + length / 2, y, color, line_width)


def cla_line(center_x: float, center_y: float, length: float, tilt_angle: float, color, line_width: float = 1):
    """
    Draw a line by specifying center point, length, and angle tilted counterclockwise from horizontal position.

    :param center_x: x position of line center point.
    :param center_y: y position of line center point.
    :param length: length of line.
    :param tilt_angle: angle tilted counterclockwise from horizontal position.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param line_width: Width of the line in pixels.
    """
    length_x = length * np.cos(np.radians(tilt_angle))
    length_y = length * np.sin(np.radians(tilt_angle))
    arcade.draw_line(center_x - length_x / 2, center_y - length_y / 2, center_x + length_x / 2, center_y + length_y / 2,
                     color, line_width)


def circle_arc_outline(center_x: float, center_y: float, radius: float, color, start_angle: float, end_angle: float,
                       border_width: float = 1, tilt_angle: float = 0, num_segments: int = 128):
    """
    Draw the outside edge of a circular arc. Useful for drawing curved lines.
    Good for saving space by cutting out a parameter.

    :param center_x: x position that is the center of the arc.
    :param center_y: y position that is the center of the arc.
    :param radius: radius of the arc.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param start_angle: start angle of the arc in degrees.
    :param end_angle: end angle of the arc in degrees.
    :param border_width: width of line in pixels.
    :param tilt_angle: angle the arc is tilted.
    :param num_segments: float of triangle segments that make up this circle.
        Higher is better quality, but slower render time.
    """
    arcade.draw_arc_outline(center_x, center_y, radius * 2, radius * 2,
                            color, start_angle, end_angle, border_width, tilt_angle, num_segments)


def star(star_object):
    """
    Draws a star by drawing an even number of lines pointing out of a central point.

    :param star_object: object used to make star. line_amount is the amount of lines used to make the star.
    """
    for line_number in range(star_object.line_amount):
        # Setting angle variable to prepare for drawing the next line
        line_angle = 180 * line_number / star_object.line_amount

        # Drawing a line through the star
        cla_line(star_object.x, star_object.y, star_object.size, line_angle, star_object.color, star_object.line_width)


def moon_outline(moon_object, num_segments: int = 128):
    """
    Draws the outline of a crescent moon.

    :param moon_object: object used to make the moon.
        phase_ratio is how "crescent" the moon is. 0 = half moon, 1 = new moon, -1 = full moon, etc.
    :param num_segments: float of triangle segments that make up this circle.
        Higher is better quality, but slower render time.
    """
    # Making variables to prepare for drawing the moon outline
    diameter = moon_object.size
    radius = diameter / 2
    phase = moon_object.phase_ratio * diameter

    # Drawing the moon's outer arc
    circle_arc_outline(moon_object.x, moon_object.y, radius, moon_object.color, -90, 90,
                       moon_object.line_width, -moon_object.tilt_angle, num_segments)

    # Drawing the moon's inner arc
    arcade.draw_arc_outline(moon_object.x, moon_object.y, phase, diameter, moon_object.color, -90, 90,
                            moon_object.line_width, -moon_object.tilt_angle, num_segments)


def road_lines(center_x: float, starting_line, end_length: float, end_y: float, amount: int, frequency: float,
               end_width: float = 1, width_decrease_ratio: float = 1/6, rainbowness: float = 0):
    """
    Draws a series of perspective lines, reminiscent of a strait road.

    :param center_x: x position of road center.
    :param starting_line: object used to make the first, bottom line.
    :param end_length: length road lines converge to.
    :param end_y: y position road lines converge to.
    :param amount: amount of road lines.
    :param frequency: fraction each road line gets toward the horizon.
    :param end_width: Width the road lines converge to in pixels.
    :param width_decrease_ratio: fraction each road line reduces the width toward the end_width.
    :param rainbowness: amount color hue is incremented by each road line.
        0 = same hue, 1/2 = -1/2 = opposite hue on the color wheel, etc.
    """
    # Making variables to prepare for drawing the road lines
    length = starting_line.size
    y = starting_line.y
    color = starting_line.color
    width = starting_line.line_width

    # Drawing the road lines
    for line_number in range(amount):
        # Drawing a road line
        cl_horizontal_line(center_x, length, y, color, width)

        # Changing variables to prepare for drawing the next road line
        length = end_length * frequency + length * (1 - frequency)
        y = end_y * frequency + y * (1 - frequency)
        width = end_width * frequency + width * (1 - width_decrease_ratio)
        if rainbowness:
            color = colorsysplus.increment_hue(color, rainbowness)


def road(starting_road_line, road_side_lines, horizon_line,
         window_width: int, center_x: float, road_line_amount: int, road_line_frequency: float,
         road_line_end_width: float = 1, road_line_width_decrease_ratio: float = 1/6, road_rainbowness: float = 0):
    """
    Draws a perspective view of a strait road, including a horizon line.

    :param starting_road_line: object used to make the first, bottom road line.
    :param road_side_lines: object used to make the road-side line's color and line width.
    :param horizon_line: object used to make the horizon line.
    :param window_width: width of the window you are drawing road on. used for drawing the horizon.
    :param center_x: x position of road center.
    :param road_line_amount: amount of road lines.
    :param road_line_frequency: fraction each road line gets toward the horizon line.
    :param road_line_end_width: Width the road lines converge to in pixels.
    :param road_line_width_decrease_ratio: fraction each road line reduces the width toward the end_width.
    :param road_rainbowness: amount color of road lines' hue is incremented by each road line.
        0 = same hue, 1/2 = -1/2 = opposite hue on the color wheel, etc.
    """
    # Drawing the road lines
    road_lines(center_x, starting_road_line, 0, horizon_line.y, road_line_amount, road_line_frequency,
               road_line_end_width, road_line_width_decrease_ratio, road_rainbowness)

    # Drawing the road-side lines
    arcade.draw_line(0, 0, center_x, horizon_line.y, road_side_lines.color, road_side_lines.line_width)
    arcade.draw_line(window_width, 0, center_x, horizon_line.y, road_side_lines.color, road_side_lines.line_width)

    # Drawing the horizon
    horizontal_line(0, window_width, horizon_line.y, horizon_line.color, horizon_line.line_width)
