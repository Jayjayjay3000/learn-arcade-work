# Importing libraries
import arcade
import numpyplus_11 as npp
import lab_11_part_0 as part_0


# Defining classes
class Window(part_0.Window):
    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color):
        super().__init__(tile_size, amount_of_tile_columns, amount_of_tile_rows, title, background_color)

    def on_mouse_press(self, mouse_x: int, mouse_y: int, mouse_button: int, modifiers: int):
        super().on_mouse_press(mouse_x, mouse_y, mouse_button, modifiers)
        if mouse_button == arcade.MOUSE_BUTTON_LEFT:
            print()
            selected_tile_amount = npp.sum_meta_list(self.selected_tiles)
            if selected_tile_amount == 1:
                print(f"Total of {selected_tile_amount} cell is selected.")
            else:
                print(f"Total of {selected_tile_amount} cells are selected.")
            for current_row_number in range(self.amount_of_tile_rows):
                current_row = self.selected_tiles[current_row_number]
                selected_tile_amount = npp.sum_list(current_row)
                if selected_tile_amount == 1:
                    print(f"Row {current_row_number} has {selected_tile_amount} cell selected.")
                else:
                    print(f"Row {current_row_number} has {selected_tile_amount} cells selected.")
                    if selected_tile_amount > 1:
                        continuous_block_lengths = npp.get_streaks_in_list(current_row, 1)
                        for current_continuous_block_length in continuous_block_lengths:
                            print(f"There are {current_continuous_block_length} continuous blocks selected "
                                  f"on row {current_row_number}.")
            for current_column_number in range(self.amount_of_tile_columns):
                current_column = npp.get_lateral_sub_list(self.selected_tiles, current_column_number)
                selected_tile_amount = npp.sum_list(current_column)
                if selected_tile_amount == 1:
                    print(f"Column {current_column_number} has {selected_tile_amount} cell selected.")
                else:
                    print(f"Column {current_column_number} has {selected_tile_amount} cells selected.")


# Running main function
def main():
    # Making class constants
    margins: object = part_0.Margins()
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
