# Importing libraries
import arcade
import draw_shapes_11 as draw
import grid_window_11 as grid
import draw_on_grid_11 as grid_draw


# Defining classes
class Window(grid_draw.Window):
    NOT_A_TILE_ID_LINE: str = "Error: This tile has an incompatible tile id"

    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color, margins):
        # Making the new window and setting its background color
        super().__init__(tile_size, amount_of_tile_columns, amount_of_tile_rows, title, background_color, margins)

        # Creating additional class attributes
        self.selected_tiles = [[0 for _ in range(self.amount_of_tile_columns)] for _ in range(self.amount_of_tile_rows)]

    def on_draw(self):
        # Starting to render the window
        super().on_draw()

        # Drawing the objects in the drawables list
        self.draw_drawables()

    def on_mouse_press(self, mouse_x: int, mouse_y: int, mouse_button: int, modifiers: int):
        if mouse_button == arcade.MOUSE_BUTTON_LEFT:
            mouse_tile_x = mouse_x // self.tile_size
            mouse_tile_y = (mouse_y - 1) // self.tile_size
            self.change_tile(mouse_tile_x, mouse_tile_y)
            self.update_drawables()

    def change_tile(self, tile_x, tile_y):
        if 0 <= tile_x < self.amount_of_tile_columns and 0 <= tile_y < self.amount_of_tile_rows:
            if self.selected_tiles[tile_y][tile_x] == 0:
                self.selected_tiles[tile_y][tile_x] = 1
            elif self.selected_tiles[tile_y][tile_x] == 1:
                self.selected_tiles[tile_y][tile_x] = 0
            else:
                print(self.NOT_A_TILE_ID_LINE)
                exit()

    def update_drawables(self):
        """
        Updates the drawables list.
        """
        cell_selection_list: list = []
        for current_row in range(self.amount_of_tile_rows):
            for current_column in range(self.amount_of_tile_columns):
                if self.selected_tiles[current_row][current_column] == 1:
                    cell_selection: object = CellSelection()
                    cell_selection.tile_x = current_column
                    cell_selection.tile_y = current_row
                    cell_selection_list.append(cell_selection)
        self.drawables = cell_selection_list + [self.margins]
        for current_drawable in self.drawables:
            current_drawable.window = self
            if current_drawable != self.margins:
                current_drawable.set_position_from_tile_and_offset()
                current_drawable.set_size_from_tile_ratio()


class Drawable(grid_draw.Able):
    def __init__(self):
        super().__init__()


class Margins(grid.Margins):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.draw()


class CellSelection(Drawable):
    TILE_X_OFFSET_RATIO = 1/2
    TILE_Y_OFFSET_RATIO = 1/2
    SIZE_TILE_RATIO = 1/3
    COLOR = (255, 255, 255)
    LINE_WIDTH = 1
    TILT_ANGLE = 45

    def __init__(self):
        super().__init__()
        self.tile_x_offset_ratio = self.TILE_X_OFFSET_RATIO
        self.tile_y_offset_ratio = self.TILE_Y_OFFSET_RATIO
        self.size_tile_ratio = self.SIZE_TILE_RATIO
        self.color = self.COLOR
        self.line_width = self.LINE_WIDTH
        self.tilt_angle = self.TILT_ANGLE

    def draw(self):
        draw.square_outline(self.x, self.y, self.size, self.color, self.line_width, self.tilt_angle)

    def on_draw(self):
        self.draw()


# Running main function
def main():
    # Making class constants
    margins: object = Margins()
    margins.color = (128, 128, 128)
    margins.line_width = 2

    # Making class constants for the window
    window = Window(48, 8, 8, "Test", (0, 0, 0), margins)
    window.update_drawables()

    # Running the program until the window closes
    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
