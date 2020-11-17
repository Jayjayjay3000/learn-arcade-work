# Importing libraries
import arcade
import window_09 as w


# Defining classes
class Window(w.Window):
    """
    Class for this lab's window.
    """
    def __init__(self, width, height, title, background_color, player_list, wall_list):
        """
        Constructs a new window and creates some additional attributes.

        :param width: Window width
        :param height: Window height
        :param title: Title (appears in title bar)
        :param background_color: List of 3 or 4 bytes in RGB/RGBA format.
        :param player_list: List containing the player sprite.
        :param wall_list: List containing all the wall sprites.
        """
        # Making the window and setting its background color
        super().__init__(width, height, title, background_color)

        # Creating additional class attributes
        self.player_list = player_list
        self.player = player_list[0]
        self.wall_list = wall_list
        self.a_is_pressed = False
        self.d_is_pressed = False
        self.w_is_pressed = False
        self.s_is_pressed = False

        # Creating class attributes from other attributes
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.wall_list)

    def on_draw(self):
        """
        The window's on draw method.
        """
        # Starting to render the window
        super().on_draw()

        # Drawing the player
        self.player_list.draw()

        # Drawing the walls
        self.wall_list.draw()

    def on_update(self, delta_time: float):
        """
        The window's on update method.

        :param delta_time: Time interval since the last time the function was called in seconds.
        """
        # Checking if either the a or d buttons are pressed, but not both
        if self.a_is_pressed ^ self.d_is_pressed:
            if self.a_is_pressed:
                # Setting the player's horizontal velocity to the left direction
                self.player.change_x = -self.player.movement_speed
            else:
                # Setting the player's horizontal velocity to the right direction
                self.player.change_x = self.player.movement_speed
        else:
            # Setting the player's horizontal velocity to 0
            self.player.change_x = 0

        # Checking if either the w or s buttons are pressed, but not both
        if self.w_is_pressed ^ self.s_is_pressed:
            if self.w_is_pressed:
                # Setting the player's vertical velocity to the up direction
                self.player.change_y = self.player.movement_speed
            else:
                # Setting the player's vertical velocity to the down direction
                self.player.change_y = -self.player.movement_speed
        else:
            # Setting the player's vertical velocity to 0
            self.player.change_y = 0

        # Updating the physics engine
        self.physics_engine.update()

    def on_key_press(self, key: int, modifiers: int):
        """
        Checks which key has been pressed and sets the respective attribute to true.

        :param key: Key that was hit
        :param modifiers: Bitwise 'and' of all modifiers (shift, ctrl, num lock) pressed during this event.
        """
        if key == arcade.key.A:
            self.a_is_pressed = True
        elif key == arcade.key.D:
            self.d_is_pressed = True
        elif key == arcade.key.W:
            self.w_is_pressed = True
        elif key == arcade.key.S:
            self.s_is_pressed = True

    def on_key_release(self, key: int, modifiers: int):
        """
        Checks which key has been released and sets the respective attribute to false.

        :param key: Key that was released
        :param modifiers: Bitwise 'and' of all modifiers (shift, ctrl, num lock) pressed during this event.
        """
        if key == arcade.key.A:
            self.a_is_pressed = False
        elif key == arcade.key.D:
            self.d_is_pressed = False
        elif key == arcade.key.W:
            self.w_is_pressed = False
        elif key == arcade.key.S:
            self.s_is_pressed = False


class Sprite(arcade.Sprite):
    """
    Class for this lab's sprites.
    """
    def __init__(self, filename=None, scale: float = 1,
                 image_x_offset_ratio: float = 0, image_y_offset_ratio: float = 0):
        """
        Creates class attributes.

        :param filename: Filename of an image that represents the sprite.
        :param scale: Scale the image up or down. Scale of 1.0 is none.
        :param image_x_offset_ratio:
            amount of offset for the image center in the x direction in respect to sprite width.
        :param image_y_offset_ratio:
            amount of offset for the image center in the y direction in respect to sprite height.
        """
        # Creating class attributes
        super().__init__(filename, scale)
        self.window = None
        self.image_center_x_ratio: float = 0
        self.image_center_x: float = 0
        self.image_x_offset_ratio: float = image_x_offset_ratio
        self.image_x_offset: float = 0
        self.image_center_y_ratio: float = 0
        self.image_center_y: float = 0
        self.image_y_offset_ratio: float = image_y_offset_ratio
        self.image_y_offset: float = 0

        # Creating class attributes from other attributes
        self.set_image_position_offset_from_ratio()

    def set_image_center_position_from_ratio(self):
        """
        Sets the sprite's image center position
        depending on its ratio to the width and height of the window it's drawn on.
        """
        self.image_center_x: float = self.image_center_x_ratio * self.window.width
        self.image_center_y: float = self.image_center_y_ratio * self.window.height

    def set_image_position_offset_from_ratio(self):
        """
        Sets the sprite's image center offset depending on its ratio to its width and height.
        """
        self.image_x_offset: float = self.image_x_offset_ratio * self.width
        self.image_y_offset: float = self.image_y_offset_ratio * self.height

    def set_center_position_from_offset(self):
        """
        Sets the sprite's center position depending on its image center position and offset.
        """
        self.center_x: float = self.image_center_x + self.image_x_offset
        self.center_y: float = self.image_center_y + self.image_y_offset


class Wall(Sprite):
    """
    Class for this lab's walls.
    """
    def __init__(self, filename=None, scale: float = 1):
        """
        Creates class attributes.

        :param filename: Filename of an image that represents the sprite.
        :param scale: Scale the image up or down. Scale of 1.0 is none.
        """
        super().__init__(filename, scale)


class Player(Sprite):
    """
    Class for this lab's player.
    """
    def __init__(self, filename=None, scale: float = 1,
                 image_x_offset_ratio: float = 0, image_y_offset_ratio: float = 0):
        """
        Creates class attributes.

        :param filename: Filename of an image that represents the sprite.
        :param scale: Scale the image up or down. Scale of 1.0 is none.
        :param image_x_offset_ratio:
            amount of offset for the image center in the x direction in respect to sprite width.
        :param image_y_offset_ratio:
            amount of offset for the image center in the y direction in respect to sprite height.
        """
        super().__init__(filename, scale, image_x_offset_ratio, image_y_offset_ratio)
        self.movement_speed = None


# Defining main function
def main():
    """
    Main function of lab 9.
    """
    # Making class constants
    player_list = arcade.SpriteList()
    player = Player("mouse_09.png", 1/2, 0, 1/4)
    player.image_center_x_ratio = 1/4
    player.image_center_y_ratio = 1/4
    player.movement_speed = 2
    player_list.append(player)
    wall_list = arcade.SpriteList()
    central_wall = Wall("center_wall_09.png", 1/2)
    central_wall.image_center_x_ratio = 1/2
    central_wall.image_center_y_ratio = 1/2
    wall_list.append(central_wall)

    # Making class constants for the window
    lab_window = Window(512, 512, "Test", (64, 64, 64), player_list, wall_list)
    lab_window.player.window = lab_window
    lab_window.player.set_image_center_position_from_ratio()
    lab_window.player.set_center_position_from_offset()
    for current_wall_row in range(2):
        # Creating a row of walls and appending each wall to the wall list
        for current_wall_x in range(0, lab_window.width + 1, int(central_wall.width)):
            current_wall = Wall("side_wall_09.png", 1/2)
            current_wall.image_center_x = current_wall_x
            current_wall.image_center_y = current_wall_row * lab_window.height
            lab_window.wall_list.append(current_wall)
    for current_wall_column in range(2):
        # Creating a column of walls and appending each wall to the wall list
        for current_wall_y in range(1, lab_window.height, int(central_wall.width)):
            current_wall = Wall("side_wall_09.png", 1/2)
            current_wall.image_center_x = current_wall_column * lab_window.width
            current_wall.image_center_y = current_wall_y
            lab_window.wall_list.append(current_wall)
    for current_wall in lab_window.wall_list:
        # Making class constants for each of the walls in the wall list
        current_wall.window = lab_window
        if current_wall == central_wall:
            current_wall.set_image_center_position_from_ratio()
        current_wall.set_center_position_from_offset()

    # Running the program until the window closes
    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
