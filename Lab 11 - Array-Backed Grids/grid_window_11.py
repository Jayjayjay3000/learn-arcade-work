# Importing libraries
import window_11 as window
import draw_shapes_11 as draw


# Defining classes
class Window(window.W):
    """
    Class for windows with grids.
    """
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
        # Creating class attributes
        self.tile_size: int = tile_size
        self.amount_of_tile_columns: int = amount_of_tile_columns
        self.amount_of_tile_rows: int = amount_of_tile_rows
        self.margins = margins

        # Creating class attributes from other attributes
        super().__init__(self.amount_of_tile_columns * self.tile_size, self.amount_of_tile_rows * self.tile_size,
                         title, background_color)


class Margins(draw.Able):
    def __init__(self):
        super().__init__()

    def draw(self):
        for current_line_number in range(1, self.window.amount_of_tile_columns):
            draw.vertical_line(current_line_number * self.window.tile_size, 0, self.window.height,
                               self.color, self.line_width)
        for current_line_number in range(1, self.window.amount_of_tile_rows):
            draw.horizontal_line(0, self.window.width, current_line_number * self.window.tile_size,
                                 self.color, self.line_width)

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        pass
