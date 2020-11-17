# Importing libraries
import arcade
import grid_window_12 as grid
import draw_on_grid_12 as grid_draw


# Defining classes
class Window(grid_draw.Window):
    """
    Class for this lab's window.
    """
    NOT_A_TILE_ID_LINE: str = "Error: This tile has an incompatible tile id"

    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color):
        # Making the new window and setting its background color
        super().__init__(tile_size, amount_of_tile_columns, amount_of_tile_rows, title, background_color)

        # Creating additional class attributes
        self.selected_tiles = [[0 for _ in range(self.amount_of_tile_columns)] for _ in range(self.amount_of_tile_rows)]

    def on_draw(self):
        """

        """
        # Starting to render the window
        super().on_draw()

        # Drawing the objects in the drawables list
        self.draw_drawables()

    def update_drawables(self):
        """
        Updates the drawables list.
        """
        self.drawables = [self.margins]
        for current_drawable in self.drawables:
            current_drawable.window = self


class Drawable(grid_draw.Able):
    def __init__(self):
        super().__init__()


class Margins(grid.Margins):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.draw()


# Running main function
def main():
    # Making class constants
    margins: object = Margins()
    margins.color = (128, 128, 128)
    margins.line_width = 2

    # Making class constants for the window
    window = Window(48, 8, 8, "Test", (0, 0, 0))
    window.margins = margins
    window.update_drawables()

    # Running the program until the window closes
    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
