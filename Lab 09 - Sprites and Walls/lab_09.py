# Importing libraries
import arcade
import draw_shapes_09 as draw


class Window(draw.Window):
    def __init__(self, width, height, title, background_color, player_list, wall_list):
        super().__init__(width, height, title, background_color)
        self.player_list = player_list
        self.player = player_list[0]
        self.wall_list = wall_list
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list)
        self.a_is_pressed = False
        self.d_is_pressed = False
        self.w_is_pressed = False
        self.s_is_pressed = False

    def on_draw(self):
        super().on_draw()
        self.player_list.draw()
        self.wall_list.draw()

    def update(self, delta_time: float):
        if self.a_is_pressed ^ self.d_is_pressed:
            if self.a_is_pressed:
                self.player.change_x = -self.player.movement_speed
            else:
                self.player.change_x = self.player.movement_speed
        else:
            self.player.change_x = 0
        if self.w_is_pressed ^ self.s_is_pressed:
            if self.w_is_pressed:
                self.player.change_y = self.player.movement_speed
            else:
                self.player.change_y = -self.player.movement_speed
        else:
            self.player.change_y = 0
        self.physics_engine.update()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.A:
            self.a_is_pressed = True
        elif key == arcade.key.D:
            self.d_is_pressed = True
        elif key == arcade.key.W:
            self.w_is_pressed = True
        elif key == arcade.key.S:
            self.s_is_pressed = True

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.A:
            self.a_is_pressed = False
        elif key == arcade.key.D:
            self.d_is_pressed = False
        elif key == arcade.key.W:
            self.w_is_pressed = False
        elif key == arcade.key.S:
            self.s_is_pressed = False


class Sprite(arcade.Sprite):
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


class Wall(Sprite):
    def __init__(self, filename=None, scale: float = 1):
        super().__init__(filename, scale)


class Player(Sprite):
    def __init__(self, filename=None, scale: float = 1,
                 image_x_offset_ratio: float = 0, image_y_offset_ratio: float = 0):
        super().__init__(filename, scale, image_x_offset_ratio, image_y_offset_ratio)
        self.movement_speed = None


# Defining main function
def main():
    # Making class constants
    player_list = arcade.SpriteList()
    player = Player("mouse_09.png", 1/2, 0, 1/4)
    player.image_center_x_ratio = 1/4
    player.image_center_y_ratio = 1/4
    player.movement_speed = 2
    player_list.append(player)
    wall_list = arcade.SpriteList()
    first_wall = Wall("center_wall_09.png", 1/2)
    first_wall.image_center_x_ratio = 1/2
    first_wall.image_center_y_ratio = 1/2
    wall_list.append(first_wall)

    # Making class constants for the window
    window = Window(512, 512, "Test", (64, 64, 64), player_list, wall_list)
    window.player.window = window
    window.player.set_image_center_position_from_ratio()
    window.player.set_center_position_from_offset()
    for current_wall_row in range(2):
        for current_wall_x in range(0, window.width + 1, int(first_wall.width)):
            current_wall = Wall("side_wall_09.png", 1/2)
            current_wall.image_center_x = current_wall_x
            current_wall.image_center_y = current_wall_row * window.height
            window.wall_list.append(current_wall)
    for current_wall_column in range(2):
        for current_wall_y in range(1, window.height, int(first_wall.width)):
            current_wall = Wall("side_wall_09.png", 1/2)
            current_wall.image_center_x = current_wall_column * window.width
            current_wall.image_center_y = current_wall_y
            window.wall_list.append(current_wall)
    for current_wall in window.wall_list:
        current_wall.window = window
        if current_wall == first_wall:
            current_wall.set_image_center_position_from_ratio()
        current_wall.set_center_position_from_offset()

    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
