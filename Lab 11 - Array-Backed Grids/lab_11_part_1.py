# Importing libraries
import arcade
import draw_shapes_11 as draw


# Defining classes
class Window(draw.Window):
    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color, margins):
        # Creating class attributes
        self.tile_size: int = tile_size
        self.amount_of_tile_columns: int = amount_of_tile_columns
        self.amount_of_tile_rows: int = amount_of_tile_rows
        self.margins = margins

        # Creating class attributes from other attributes
        super().__init__(self.amount_of_tile_columns * self.tile_size, self.amount_of_tile_rows * self.tile_size,
                         title, background_color)
        self.selected_tiles = [[0 for _ in range(self.amount_of_tile_columns)] for _ in range(self.amount_of_tile_rows)]

        self.selected_tiles[1][1] = 1

    def on_draw(self):
        # Starting to render the window
        super().on_draw()

        # Drawing the objects in the drawables list
        self.draw_drawables()

    def on_update(self, delta_time: float):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.selected_tiles[(y - 1) // self.tile_size][x // self.tile_size] == 0:
                self.selected_tiles[(y - 1) // self.tile_size][x // self.tile_size] = 1
            elif self.selected_tiles[(y - 1) // self.tile_size][x // self.tile_size] == 1:
                self.selected_tiles[(y - 1) // self.tile_size][x // self.tile_size] = 0
            else:
                print("error")
                exit()
            self.update_drawables()

    def update_drawables(self):
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


class Drawable(draw.Able):
    def __init__(self):
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
    print(window.selected_tiles)


# Running main function
if __name__ == "__main__":
    main()
