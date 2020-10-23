# Importing libraries
import arcade
import draw_shapes_08 as draw


class Window(draw.Window):
    def __init__(self, width, height, title, background_color, player_list):
        super().__init__(width, height, title, background_color)
        self.player_list = player_list
        self.player = player_list[0]

    def on_draw(self):
        super().on_draw()
        self.player_list.draw()
        arcade.draw_line(0, 0, self.width, self.height, (255, 255, 255), 1)
        arcade.draw_line(self.width, 0, 0, self.height, (255, 255, 255), 1)
        arcade.draw_point(self.player.center_x, self.player.bottom, (255, 255, 255), 5)
        arcade.draw_point(self.player.center_x, self.player.top, (255, 255, 255), 5)
        arcade.draw_point(self.player.left, self.player.center_y, (255, 255, 255), 5)
        arcade.draw_point(self.player.right, self.player.center_y, (255, 255, 255), 5)

    def update(self, delta_time: float):
        self.player.update()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.A:
            self.player.change_x -= self.player.movement_speed
        elif key == arcade.key.D:
            self.player.change_x += self.player.movement_speed
        elif key == arcade.key.W:
            self.player.change_y += self.player.movement_speed
        elif key == arcade.key.S:
            self.player.change_y -= self.player.movement_speed

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.A:
            self.player.change_x += self.player.movement_speed
        elif key == arcade.key.D:
            self.player.change_x -= self.player.movement_speed
        elif key == arcade.key.W:
            self.player.change_y -= self.player.movement_speed
        elif key == arcade.key.S:
            self.player.change_y += self.player.movement_speed


class Player(arcade.Sprite):
    def __init__(self, filename=None, scale: float = 1,
                 image_x_offset_ratio: float = 0, image_y_offset_ratio: float = 0):
        super().__init__(filename, scale)
        self.window = None
        self.image_x_offset_ratio: float = image_x_offset_ratio
        self.image_x_offset: float = 0
        self.image_y_offset_ratio: float = image_y_offset_ratio
        self.image_y_offset: float = 0
        self.set_image_position_offset_from_ratio()
        self.image_center_x_ratio: float = 0
        self.image_center_x: float = 0
        self.image_center_y_ratio: float = 0
        self.image_center_y: float = 0
        self.movement_speed = None

    def set_image_x_offset_from_ratio(self):
        self.image_x_offset: float = self.image_x_offset_ratio * self.width

    def set_image_y_offset_from_ratio(self):
        self.image_y_offset: float = self.image_y_offset_ratio * self.height

    def set_image_position_offset_from_ratio(self):
        self.set_image_x_offset_from_ratio()
        self.set_image_y_offset_from_ratio()

    def set_image_center_x_from_ratio(self):
        self.image_center_x: float = self.image_center_x_ratio * self.window.width

    def set_image_center_y_from_ratio(self):
        self.image_center_y: float = self.image_center_y_ratio * self.window.height

    def set_image_center_position_from_ratio(self):
        self.set_image_center_x_from_ratio()
        self.set_image_center_y_from_ratio()

    def set_center_x_from_offset(self):
        self.center_x = self.image_center_x + self.image_x_offset

    def set_center_y_from_offset(self):
        self.center_y = self.image_center_y + self.image_y_offset

    def set_center_position_from_offset(self):
        self.set_center_x_from_offset()
        self.set_center_y_from_offset()

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


# Defining main function
def main():
    # Making class constants
    player_list = arcade.SpriteList()
    player = Player("mouse_08.png", 1/2, 0, 1/4)
    player_list.append(player)
    player.image_center_x_ratio = 1/2
    player.image_center_y_ratio = 1/2
    player.movement_speed = 2

    # Making class constants for the window
    window = Window(512, 512, "Test", (64, 64, 64), player_list)
    window.player.window = window
    window.player.set_image_center_position_from_ratio()
    window.player.set_center_position_from_offset()

    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
