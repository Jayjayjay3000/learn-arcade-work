# Importing libraries
import grid_window_12 as grid
import draw_shapes_12 as draw


# Defining classes
class Window(grid.Window, draw.Window):
    """
    Class for windows with grids you can draw on.
    """
    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color, top_margin_width_ratio: float = 0, bottom_margin_width_ratio: float = 0,
                 left_margin_width_ratio: float = 0, right_margin_width_ratio: float = 0):
        """
        Constructs a new window as well as set the window's background color.

        :param tile_size: size of a grid tile.
        :param amount_of_tile_columns: amount of grid tiles wide the window is.
        :param amount_of_tile_rows: amount of grid tiles tall the window is.
        :param title: Title (appears in title bar)
        :param background_color: List of 3 or 4 bytes in RGB/RGBA format.
        """
        super().__init__(tile_size, amount_of_tile_columns, amount_of_tile_rows, title, background_color,
                         top_margin_width_ratio, bottom_margin_width_ratio,
                         left_margin_width_ratio, right_margin_width_ratio)


class Able(draw.Able):
    """
    Class for generic things you can draw on a grid.
    """
    def __init__(self):
        """
        Creates class attributes.
        """
        super().__init__()
        self.tile_x = None
        self.tile_x_offset_ratio = None
        self.tile_y = None
        self.tile_y_offset_ratio = None
        self.size_tile_ratio = None

    def set_x_from_tile_and_offset(self):
        """
        Sets this drawable's x-position depending on the tile it's on and it's tile offset.
        """
        window = self.window
        self.x: float = (self.tile_x + self.tile_x_offset_ratio) * window.tile_size + window.left_margin_width

    def set_y_from_tile_and_offset(self):
        """
        Sets this drawable's y-position depending on the tile it's on and it's tile offset.
        """
        window = self.window
        self.y: float = (self.tile_y + self.tile_y_offset_ratio) * window.tile_size + window.bottom_margin_width

    def set_position_from_tile_and_offset(self):
        """
        Sets this drawable's position depending on the tile it's on and it's tile offset.
        """
        self.set_x_from_tile_and_offset()
        self.set_y_from_tile_and_offset()

    def set_size_from_tile_ratio(self):
        """
        Sets this drawable's size depending on its ratio to the size of the grid tile it's drawn on.
        """
        self.size: float = self.size_tile_ratio * self.window.tile_size


# Defining functions
def line(start_x: float, start_y: float, end_x: float, end_y: float, color, line_width: float = 1):
    """
    Draw a line.

    :param float start_x: x position of line starting point.
    :param float start_y: y position of line starting point.
    :param float end_x: x position of line ending point.
    :param float end_y: y position of line ending point.
    :param Color color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param float line_width: Width of the line in pixels.
    """
    draw.line(start_x, start_y, end_x, end_y, color, line_width)


def cl_horizontal_line(center_x: float, length: float, y: float, color, line_width: float = 1):
    """
    Draw a horizontal line by specifying center point and length.

    :param center_x: x position of line center point.
    :param length: length of line.
    :param y: y position of line starting and ending points.
    :param color: color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
    :param line_width: Width of the line in pixels.
    """
    draw.cl_horizontal_line(center_x, length, y, color, line_width)


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
    draw.square_outline(center_x, center_y, side_length, color, border_width, tilt_angle)
