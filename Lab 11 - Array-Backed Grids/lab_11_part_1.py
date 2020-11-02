# Importing libraries
import arcade
import draw_shapes_11 as draw


# Defining classes
class Window(draw.Window):
    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color):
        self.tile_size = tile_size
        self.amount_of_tile_columns = amount_of_tile_columns
        self.amount_of_tile_rows = amount_of_tile_rows
        super().__init__(self.amount_of_tile_columns * self.tile_size, self.amount_of_tile_rows * self.tile_size,
                         title, background_color)

    def on_draw(self):
        super().on_draw()

    def on_update(self, delta_time: float):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass


# Running main function
def main():
    window = Window(64, 8, 8, "Test", (0, 0, 0))
    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
