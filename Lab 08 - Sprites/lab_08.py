# Importing libraries
import arcade
import draw_shapes_08 as draw

# Making constants
WINDOW_WIDTH: int = 512
WINDOW_HEIGHT: int = 512
WINDOW_TEXT: str = "Test"
BACKGROUND_COLOR = (64, 64, 64)
PLAYER_FILE_NAME: str = "mouse_08.png"
PLAYER_SCALE_RATIO: float = 1
PLAYER_IMAGE_X_OFFSET_RATIO: float = 0
PLAYER_IMAGE_Y_OFFSET_RATIO: float = 1/4
PLAYER_STARTING_X_RATIO: float = 1/2
PLAYER_STARTING_Y_RATIO: float = 1/2

# Making constants from other constants
PLAYER_STARTING_X = PLAYER_STARTING_X_RATIO * WINDOW_WIDTH
PLAYER_STARTING_Y = PLAYER_STARTING_Y_RATIO * WINDOW_HEIGHT


class Window(draw.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TEXT, BACKGROUND_COLOR)
        self.player_list = arcade.SpriteList()
        self.player = Player(self, PLAYER_FILE_NAME, PLAYER_SCALE_RATIO,
                             PLAYER_IMAGE_X_OFFSET_RATIO, PLAYER_IMAGE_Y_OFFSET_RATIO)
        self.player_list.append(self.player)

    def on_draw(self):
        super().on_draw()
        self.player_list.draw()
        arcade.draw_line(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, (255, 255, 255), 1)
        arcade.draw_line(WINDOW_WIDTH, 0, 0, WINDOW_HEIGHT, (255, 255, 255), 1)
        arcade.draw_point(self.player.center_x, self.player.bottom, (255, 255, 255), 5)
        arcade.draw_point(self.player.center_x, self.player.top, (255, 255, 255), 5)
        arcade.draw_point(self.player.left, self.player.center_y, (255, 255, 255), 5)
        arcade.draw_point(self.player.right, self.player.center_y, (255, 255, 255), 5)


class Player(arcade.Sprite):
    def __init__(self, window, filename=None, scale: float = 1,
                 image_x_offset_ratio: float = 0, image_y_offset_ratio: float = 0):
        super().__init__(filename, scale)
        self.window = window
        self.image_x_offset_ratio = image_x_offset_ratio
        self.image_x_offset = 0
        self.image_y_offset_ratio = image_y_offset_ratio
        self.image_y_offset = 0
        self.set_image_position_offset_from_ratio()
        self.image_center_x = 0
        self.image_center_y = 0

    def set_image_x_offset_from_ratio(self):
        self.image_x_offset = self.image_x_offset_ratio * self.window.width

    def set_image_y_offset_from_ratio(self):
        self.image_y_offset = self.image_y_offset_ratio * self.window.height

    def set_image_position_offset_from_ratio(self):
        self.set_image_x_offset_from_ratio()
        self.set_image_y_offset_from_ratio()


# Defining main function
def main():
    # Making class constants
    window = Window()

    # Making constants from window class constants
    window.player.image_center_x = PLAYER_STARTING_X_RATIO * window.width
    window.player.image_center_y = PLAYER_STARTING_Y_RATIO * window.height
    window.player.center_x = PLAYER_STARTING_X + self.player.image_x_offset
    window.player.center_y = PLAYER_STARTING_Y + self.player.image_y_offset

    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
