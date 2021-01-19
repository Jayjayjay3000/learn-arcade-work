# Importing libraries
import numpy as np
from arcade import draw_line as line, \
    draw_rectangle_outline as rectangle_outline, \
    draw_rectangle_filled as rectangle_filled, \
    draw_arc_outline as arc_outline
import window_12 as w


# Defining classes
class Window(w.Window):
    """
    Class for windows you can draw on.
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
        # Making the new window and setting its background color
        super().__init__(width, height, title, background_color, fullscreen, resizable, update_rate, antialiasing)

        # Creating additional class attributes
        self.drawables: list = []

    def draw_drawables(self):
        """
        Draws the objects in the drawables list by calling their on draw methods.
        """
        # Looping through all objects in drawables and drawing them
        for current_drawable in self.drawables:
            current_drawable.on_draw()

    def update_drawables(self):
        """
        Updates the drawables list.
        """
        pass

    def on_initial_draw(self):
        """
        >> Remember to ask Craven on how to draw something only once using the window class <<
        """
        pass


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
        self.transparency = None
        self.full_color = None
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

    def set_full_color_from_color_and_transparency(self):
        self.full_color = tuple([current_element for current_element in self.color] + [self.transparency])

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
    line(start_x, y, end_x, y, color, line_width)


def cl_horizontal_line(center_x: float, length: float, y: float, color, line_width: float = 1):
    """
    Draw a horizontal line by specifying center point and length.

    :param center_x: x position of line center point.
    :param length: length of line.
    :param y: y position of line starting and ending points.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param line_width: Width of the line in pixels.
    """
    line(center_x - length / 2, y, center_x + length / 2, y, color, line_width)


def vertical_line(x: float, start_y: float, end_y: float, color, line_width: float = 1):
    """
    Draw a horizontal line. Good for saving space by cutting out a parameter.

    :param x: x position of line starting and ending points.
    :param start_y: x position of line starting point.
    :param end_y: y position of line ending point.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param line_width: Width of the line in pixels.
    """
    line(x, start_y, x, end_y, color, line_width)


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
    line(center_x - length_x / 2, center_y - length_y / 2, center_x + length_x / 2, center_y + length_y / 2, color,
         line_width)


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
    rectangle_outline(center_x, center_y, side_length, side_length, color, border_width, tilt_angle)


def square_filled(center_x: float, center_y: float, side_length: float, color, tilt_angle: float = 0):
    """
    Draw a filled-in square.

    :param center_x: x coordinate of square center.
    :param center_y: y coordinate of square center.
    :param side_length: length of the square's sides.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param tilt_angle: rotation of the square. Defaults to zero.
    """
    rectangle_filled(center_x, center_y, side_length, side_length, color, tilt_angle)


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
    arc_outline(center_x, center_y, radius * 2, radius * 2, color, start_angle, end_angle,
                border_width, tilt_angle, num_segments)
