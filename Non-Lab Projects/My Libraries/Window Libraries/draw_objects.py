# Importing libraries
import colorsysplus as colorsys
from draw_shapes import *


# Defining classes
class Star(Able):
    """
    Class for drawable stars.
    """
    def __init__(self):
        """
        Creates class attributes.
        """
        super().__init__()
        self.line_amount = None

    def draw(self):
        """
        Draws a star by drawing an even number of lines pointing out of a central point.
        """
        for line_number in range(self.line_amount):
            # Setting angle variable to prepare for drawing the next line
            line_angle: float = 180 * line_number / self.line_amount

            # Drawing a line through the star
            cla_line(self.x, self.y, self.size, line_angle, self.color, self.line_width)

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        pass


class Moon(Able):
    """
    Class for drawable moons.
    """
    def __init__(self):
        """
        Creates class attributes.
        """
        super().__init__()
        self.phase_ratio = None
        self.num_segments: int = 128

    def draw_outline(self):
        """
        Draws the outline of a crescent moon.
        """
        # Making variables to prepare for drawing the moon outline
        diameter: float = self.size
        radius: float = diameter / 2
        phase: float = self.phase_ratio * diameter

        # Drawing the moon's outer arc
        circle_arc_outline(self.x, self.y, radius, self.color, -90, 90,
                           self.line_width, -self.tilt_angle, self.num_segments)

        # Drawing the moon's inner arc
        arc_outline(self.x, self.y, phase, diameter, self.color, -90, 90,
                    self.line_width, -self.tilt_angle, self.num_segments)

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        pass


# Defining functions
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
    y: float = starting_line.y
    length: float = starting_line.size
    color = starting_line.color
    width: float = starting_line.line_width

    # Drawing the road lines
    for line_number in range(amount):
        # Drawing a road line
        cl_horizontal_line(center_x, length, y, color, width)

        # Changing variables to prepare for drawing the next road line
        length: float = end_length * frequency + length * (1 - frequency)
        y: float = end_y * frequency + y * (1 - frequency)
        if rainbowness:
            color = colorsys.increment_hue(color, rainbowness)
        width: float = end_width * frequency + width * (1 - width_decrease_ratio)


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
    line(0, 0, center_x, horizon_line.y, road_side_lines.color, road_side_lines.line_width)
    line(window_width, 0, center_x, horizon_line.y, road_side_lines.color, road_side_lines.line_width)

    # Drawing the horizon
    horizontal_line(0, window_width, horizon_line.y, horizon_line.color, horizon_line.line_width)
