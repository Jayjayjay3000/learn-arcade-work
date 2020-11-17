# Importing libraries
from window_12 import *
import draw_shapes_12 as draw


# Defining classes
class Window(Window):
    """
    Class for windows with grids.
    """
    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color):
        """
        Constructs a new window as well as set the window's background color.

        :param tile_size: size of a grid tile.
        :param amount_of_tile_columns: amount of grid tiles wide the window is.
        :param amount_of_tile_rows: amount of grid tiles tall the window is.
        :param title: Title (appears in title bar)
        :param background_color: List of 3 or 4 bytes in RGB/RGBA format.
        """
        # Creating class attributes
        self.tile_size: int = tile_size
        self.amount_of_tile_columns: int = amount_of_tile_columns
        self.amount_of_tile_rows: int = amount_of_tile_rows
        self.margins = None

        # Creating class attributes from other attributes
        super().__init__(self.amount_of_tile_columns * self.tile_size, self.amount_of_tile_rows * self.tile_size,
                         title, background_color)


class Margins(draw.Able):
    """
    Class for drawable grid lines.
    """
    def __init__(self):
        """
        Creates class attributes.
        """
        super().__init__()

    def draw(self):
        """
        Draws grid lines between the grid tiles.
        """
        for current_line_number in range(1, self.window.amount_of_tile_columns):
            # Drawing a vertical grid line
            draw.vertical_line(current_line_number * self.window.tile_size, 0, self.window.height,
                               self.color, self.line_width)
        for current_line_number in range(1, self.window.amount_of_tile_rows):
            # Drawing a horizontal grid line
            draw.horizontal_line(0, self.window.width, current_line_number * self.window.tile_size,
                                 self.color, self.line_width)

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        pass
