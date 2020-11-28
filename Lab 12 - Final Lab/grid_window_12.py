# Importing libraries
from window_12 import *
import draw_shapes_12 as draw


# Defining classes
class Window(Window):
    """
    Class for windows with grids.
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
        :param top_margin_width_ratio:
        :param bottom_margin_width_ratio:
        :param left_margin_width_ratio:
        :param right_margin_width_ratio:
        """
        # Creating class attributes
        self.tile_size: int = tile_size
        self.amount_of_tile_columns: int = amount_of_tile_columns
        self.amount_of_tile_rows: int = amount_of_tile_rows
        self.top_margin_width_ratio: float = top_margin_width_ratio
        self.top_margin_width = 0
        self.bottom_margin_width_ratio: float = bottom_margin_width_ratio
        self.bottom_margin_width = 0
        self.left_margin_width_ratio: float = left_margin_width_ratio
        self.left_margin_width = 0
        self.right_margin_width_ratio: float = right_margin_width_ratio
        self.right_margin_width = 0
        self.get_margin_widths_from_ratios()
        self.grid_lines = None

        # Creating class attributes from other attributes
        window_width = self.amount_of_tile_columns * self.tile_size + self.left_margin_width + self.right_margin_width
        window_height = self.amount_of_tile_rows * self.tile_size + self.top_margin_width + self.bottom_margin_width
        super().__init__(window_width, window_height, title, background_color)

    def get_margin_widths_from_ratios(self):
        self.top_margin_width: int = int(self.top_margin_width_ratio * self.tile_size)
        self.bottom_margin_width: int = int(self.bottom_margin_width_ratio * self.tile_size)
        self.left_margin_width: int = int(self.left_margin_width_ratio * self.tile_size)
        self.right_margin_width: int = int(self.right_margin_width_ratio * self.tile_size)


class Lines(draw.Able):
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
        window = self.window
        top_line_number = window.amount_of_tile_rows
        if window.top_margin_width != 0:
            top_line_number += 1
        bottom_line_number = 1
        if window.bottom_margin_width != 0:
            bottom_line_number -= 1
        for current_line_number in range(bottom_line_number, top_line_number):
            # Drawing a horizontal grid line
            draw.horizontal_line(window.left_margin_width, window.width - window.right_margin_width,
                                 current_line_number * window.tile_size + window.bottom_margin_width,
                                 self.full_color, self.line_width)
        left_line_number = 1
        if window.left_margin_width != 0:
            left_line_number -= 1
        right_line_number = window.amount_of_tile_columns
        if window.right_margin_width != 0:
            right_line_number += 1
        for current_line_number in range(left_line_number, right_line_number):
            # Drawing a vertical grid line
            draw.vertical_line(current_line_number * window.tile_size + window.left_margin_width,
                               window.bottom_margin_width, window.height - window.top_margin_width,
                               self.full_color, self.line_width)

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        pass
