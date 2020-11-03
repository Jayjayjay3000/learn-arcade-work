# Importing libraries
import arcade
import draw_shapes_11 as draw


# Defining classes
class Window(draw.Window):
    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color, margin_color, margin_width: float = 1):
        # Creating class attributes
        self.tile_size: int = tile_size
        self.amount_of_tile_columns: int = amount_of_tile_columns
        self.amount_of_tile_rows: int = amount_of_tile_rows
        self.margin_color = margin_color
        self.margin_width: float = margin_width

        # Creating class attributes from other attributes
        super().__init__(self.amount_of_tile_columns * self.tile_size, self.amount_of_tile_rows * self.tile_size,
                         title, background_color)
        self.grid = [[0 for _ in range(self.amount_of_tile_columns)] for _ in range(self.amount_of_tile_rows)]

        self.grid[1][1] = 1

    def on_draw(self):
        super().on_draw()
        for current_line_number in range(1, self.amount_of_tile_columns):
            draw.vertical_line(current_line_number * self.tile_size, 0, self.height,
                               self.margin_color, self.margin_width)
        for current_line_number in range(1, self.amount_of_tile_rows):
            draw.horizontal_line(0, self.width, current_line_number * self.tile_size,
                                 self.margin_color, self.margin_width)
        for current_column_number in range(self.amount_of_tile_columns):
            for current_row_number in range(self.amount_of_tile_rows):
                draw.square_outline((current_column_number + 1/2) * self.tile_size, (current_row_number + 1/2) * self.tile_size,
                                    self.tile_size / 3, (255, 255, 255), 1, 45)

    def on_update(self, delta_time: float):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass


# Running main function
def main():
    window = Window(48, 8, 8, "Test", (0, 0, 0), (128, 128, 128), 2)
    arcade.run()
    print(window.grid)


# Running main function
if __name__ == "__main__":
    main()
