# Importing libraries
import grid_window_11 as grid
import draw_shapes_11 as draw


# Defining classes
class Window(grid.Window, draw.Window):
    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color, margins):
        """
        Constructs a new window as well as set the window's background color.

        :param tile_size:
        :param amount_of_tile_columns:
        :param amount_of_tile_rows:
        :param title: Title (appears in title bar)
        :param background_color: List of 3 or 4 bytes in RGB/RGBA format.
        :param margins:
        """
        super().__init__(tile_size, amount_of_tile_columns, amount_of_tile_rows, title, background_color, margins)


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
        self.x: float = (self.tile_x + self.tile_x_offset_ratio) * self.window.tile_size

    def set_y_from_tile_and_offset(self):
        self.y: float = (self.tile_y + self.tile_y_offset_ratio) * self.window.tile_size

    def set_position_from_tile_and_offset(self):
        self.set_x_from_tile_and_offset()
        self.set_y_from_tile_and_offset()

    def set_size_from_tile_ratio(self):
        self.size: float = self.size_tile_ratio * self.window.tile_size
