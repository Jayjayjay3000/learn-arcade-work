# Importing libraries
from lab_11_part_0 import *


# Defining classes
class Window(Window):
    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color):
        super().__init__(tile_size, amount_of_tile_columns, amount_of_tile_rows, title, background_color)

    def on_mouse_press(self, mouse_x: int, mouse_y: int, mouse_button: int, modifiers: int):
        if mouse_button == MOUSE_BUTTON_LEFT:
            mouse_tile_x: int = mouse_x // self.tile_size
            mouse_tile_y: int = (mouse_y - 1) // self.tile_size
            for selection_y_offset in range(-1, 2):
                if selection_y_offset == 0:
                    for selection_x_offset in range(-1, 2):
                        self.change_tile(mouse_tile_x + selection_x_offset, mouse_tile_y + selection_y_offset)
                else:
                    self.change_tile(mouse_tile_x, mouse_tile_y + selection_y_offset)
            self.update_drawables()


# Running main function
def main():
    # Making class constants
    margins: object = Margins()
    margins.color = (128, 128, 128)
    margins.line_width = 2

    # Making class constants for the window
    window = Window(48, 8, 8, "Test", (0, 0, 0))
    window.margins = margins
    window.margins.window = window

    # Initially updating variables
    window.update_drawables()

    # Running the program until the window closes
    run()


# Running main function
if __name__ == "__main__":
    main()
