# Importing libraries
from arcade import key
from arcade import run
import grid_window_12 as grid
import draw_on_grid_12 as draw


# Defining classes
class Window(draw.Window):
    """
    Class for this lab's window.
    """
    NOT_A_TILE_ID_LINE: str = "Error: This tile has an incompatible tile id"

    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color):
        # Making the new window and setting its background color
        super().__init__(tile_size, amount_of_tile_columns, amount_of_tile_rows, title, background_color)
        self.drawables: list = self.drawables
        self.player = None

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
        self.drawables: list = [self.margins, self.player]

    def on_key_press(self, pressed_key: int, modifiers: int):
        if self.player.can_move:
            if pressed_key == key.W:
                self.player.move_up()
            elif pressed_key == key.S:
                self.player.move_down()
            elif pressed_key == key.A:
                self.player.move_left()
            elif pressed_key == key.D:
                self.player.move_right()


class Drawable(draw.Able):
    def __init__(self):
        super().__init__()


class Margins(grid.Margins):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.draw()


class Entity(Drawable):
    TILE_X_OFFSET_RATIO: float = 1/2
    TILE_Y_OFFSET_RATIO: float = 1/2
    SIZE_TILE_RATIO: float = 1/3
    LINE_WIDTH: float = 1
    TILT_ANGLE: float = 45

    def __init__(self):
        super().__init__()
        self.tile_x_offset_ratio: float = self.TILE_X_OFFSET_RATIO
        self.tile_y_offset_ratio: float = self.TILE_Y_OFFSET_RATIO
        self.size_tile_ratio: float = self.SIZE_TILE_RATIO
        self.line_width: float = self.LINE_WIDTH
        self.tilt_angle: float = self.TILT_ANGLE
        self.can_move: bool = False

    def draw(self):
        draw.square_outline(self.x, self.y, self.size, self.color, self.line_width, self.tilt_angle)

    def move_up(self):
        if self.tile_y + 1 < self.window.amount_of_tile_rows:
            self.tile_y += 1
            self.set_y_from_tile_and_offset()

    def move_down(self):
        if self.tile_y - 1 >= 0:
            self.tile_y -= 1
            self.set_y_from_tile_and_offset()

    def move_left(self):
        if self.tile_x - 1 >= 0:
            self.tile_x -= 1
            self.set_x_from_tile_and_offset()

    def move_right(self):
        if self.tile_x + 1 < self.window.amount_of_tile_columns:
            self.tile_x += 1
            self.set_x_from_tile_and_offset()


class Player(Entity):
    COLOR = (255, 255, 255)

    def __init__(self):
        super().__init__()
        self.color = self.COLOR
        self.can_move = True

    def on_draw(self):
        self.draw()


class Enemy(Entity):
    COLOR = (255, 0, 0)

    def __init__(self):
        super().__init__()
        self.color = self.COLOR


# Running main function
def main():
    # Making class constants
    margins: object = Margins()
    margins.color = (128, 128, 128)
    margins.line_width = 2
    player = Player()
    player.tile_x = 1
    player.tile_y = 1

    # Making class constants for the window
    window = Window(48, 8, 8, "Test", (0, 0, 0))
    window.margins = margins
    window.margins.window = window
    window.player = player
    window.player.window = window
    window.player.set_position_from_tile_and_offset()
    window.player.set_size_from_tile_ratio()
    window.update_drawables()

    # Running the program until the window closes
    run()


# Running main function
if __name__ == "__main__":
    main()
