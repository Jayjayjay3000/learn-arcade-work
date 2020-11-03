# Importing libraries
import arcade
import numpy as np
import colorsysplus_03 as colorsysplus


# Defining classes
class Window(arcade.Window):
    """
    Class for windows.
    """
    def __init__(self, width: int = 800, height: int = 600, title: str = "Arcade Window", background_color=(0, 0, 0),
                 fullscreen: bool = False, resizable: bool = False, update_rate=1/60, antialiasing: bool = True):
        """
        Constructs a new window as well as set the window's background color.

        :param width: Window width
        :param height: Window height
        :param title: Title (appears in title bar)
        :param background_color: List of 3 or 4 bytes in RGB/RGBA format.
        :param fullscreen: Should this be full screen?
        :param resizable: Can the user resize the window?
        :param update_rate: How frequently to update the window.
        :param antialiasing: Should OpenGL's anti-aliasing be enabled?
        """
        # Making the new window
        super().__init__(width, height, title, fullscreen, resizable, update_rate, antialiasing)

        # Setting additional class attributes
        self.color = background_color
        self.drawables: list = []

        # Setting the window's background color
        arcade.set_background_color(self.color)

    def draw_drawables(self):
        """
        Draws the objects in the drawables list by calling their on draw methods.
        """
        # Looping through all objects in drawables and drawing them
        for current_drawable in self.drawables:
            current_drawable.on_draw()

    def on_initial_draw(self):
        """
        >> Remember to ask Craven on how to draw something only once using the window class <<
        """
        pass

    def on_draw(self):
        """
        Renders the window.
        """
        # Starting to render the window
        arcade.start_render()


class Able:
    """
    Class for generic things you can draw.
    """
    def __init__(self):
        """
        Creates class attributes.
        """
        self.window = None
        self.x_ratio = None
        self.x = None
        self.y_ratio = None
        self.y = None
        self.size_ratio = None
        self.size = None
        self.color = None
        self.line_width = None
        self.tilt_angle = None

    def set_x_from_ratio(self):
        """
        Sets this drawable's x-position depending on its ratio to the width of the window it's drawn on.
        """
        self.x = self.x_ratio * self.window.width

    def set_y_from_ratio(self):
        """
        Sets this drawable's y-position depending on its ratio to the height of the window it's drawn on.
        """
        self.y = self.y_ratio * self.window.height

    def set_position_from_ratio(self):
        """
        Sets this drawable's position depending on its ratio to the width and height of the window it's drawn on.
        """
        self.set_x_from_ratio()
        self.set_y_from_ratio()

    def set_size_from_ratio(self, use_width: bool = True):
        """
        Sets this drawable's size depending on its ratio to the width or height of the window it's drawn on.

        :param use_width: Whether to use the width or height of the window this is drawn on.
            Width if true, height if false.
        """
        if use_width:
            self.size = self.size_ratio * self.window.width
        else:
            self.size = self.size_ratio * self.window.height

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        pass


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
        arcade.draw_arc_outline(self.x, self.y, phase, diameter, self.color, -90, 90,
                                self.line_width, -self.tilt_angle, self.num_segments)

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        pass


# Defining functions
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


def vertical_line(x: float, start_y: float, end_y: float, color, line_width: float = 1):
    """
    Draw a horizontal line. Good for saving space by cutting out a parameter.

    :param x: x position of line starting and ending points.
    :param start_y: x position of line starting point.
    :param end_y: y position of line ending point.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param line_width: Width of the line in pixels.
    """
    arcade.draw_line(x, start_y, x, end_y, color, line_width)


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
    length_x: float = length * np.cos(np.radians(tilt_angle))
    length_y: float = length * np.sin(np.radians(tilt_angle))
    arcade.draw_line(center_x - length_x / 2, center_y - length_y / 2, center_x + length_x / 2, center_y + length_y / 2,
                     color, line_width)


def square_outline(center_x: float, center_y: float, side_length: float, color,
                   border_width: float = 1, tilt_angle: float = 0):
    """
    Draw a square outline.

    :param center_x: x coordinate of square center.
    :param center_y: y coordinate of square center.
    :param side_length: length of the square's sides.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param border_width: width of the lines, in pixels.
    :param tilt_angle: rotation of the square. Defaults to zero.
    """
    arcade.draw_rectangle_outline(center_x, center_y, side_length, side_length, color, border_width, tilt_angle)


def square_filled(center_x: float, center_y: float, side_length: float, color, tilt_angle: float = 0):
    """
    Draw a filled-in square.

    :param center_x: x coordinate of square center.
    :param center_y: y coordinate of square center.
    :param side_length: length of the square's sides.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param tilt_angle: rotation of the square. Defaults to zero.
    """
    arcade.draw_rectangle_filled(center_x, center_y, side_length, side_length, color, tilt_angle)


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
    arcade.draw_arc_outline(center_x, center_y, radius * 2, radius * 2, color, start_angle, end_angle,
                            border_width, tilt_angle, num_segments)


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
            color = colorsysplus.increment_hue(color, rainbowness)
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
    arcade.draw_line(0, 0, center_x, horizon_line.y, road_side_lines.color, road_side_lines.line_width)
    arcade.draw_line(window_width, 0, center_x, horizon_line.y, road_side_lines.color, road_side_lines.line_width)

    # Drawing the horizon
    horizontal_line(0, window_width, horizon_line.y, horizon_line.color, horizon_line.line_width)
