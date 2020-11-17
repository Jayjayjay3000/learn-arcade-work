# Importing libraries
import grid_window as grid
from draw_shapes import *


# Defining classes
class Window(grid.Window, Window):
    """
    Class for windows with grids you can draw on.
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
        super().__init__(tile_size, amount_of_tile_columns, amount_of_tile_rows, title, background_color)


class Able(Able):
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
        self.x: float = (self.tile_x + self.tile_x_offset_ratio) * self.window.tile_size

    def set_y_from_tile_and_offset(self):
        """
        Sets this drawable's y-position depending on the tile it's on and it's tile offset.
        """
        self.y: float = (self.tile_y + self.tile_y_offset_ratio) * self.window.tile_size

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
