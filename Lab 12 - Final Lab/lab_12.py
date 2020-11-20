# Importing libraries
from arcade import key
from arcade import run
import grid_window_12 as grid
import draw_on_grid_12 as draw


def get_not_a_compatible_enemy_step_line(enemy_step):
    line: str = f"Error: {enemy_step} is not a compatible enemy step"
    return line


# Defining classes
class Window(draw.Window):
    """
    Class for this lab's window.
    """
    def get_not_a_compatible_phase_id_line(self):
        line: str = f"Error: {self.phase_id} is not a compatible phase id"
        return line

    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color):
        # Making the new window and setting its background color
        super().__init__(tile_size, amount_of_tile_columns, amount_of_tile_rows, title, background_color)
        self.drawables: list = self.drawables
        self.player = None
        self.enemy_list: list = []
        self.starting_tiles = None
        self.grid_tiles = None
        self.phase_id = None
        self.possible_enemy_steps: list = []
        self.time_between_enemy_steps = None
        self.time_until_next_enemy_step = None

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
        self.drawables: list = [self.margins, self.player] + self.enemy_list

    def on_update(self, delta_time: float):
        if self.phase_id == 0:
            if self.player.has_moved:
                self.player.has_moved = False
                self.phase_id = 1
                self.time_until_next_enemy_step = self.time_between_enemy_steps
        elif self.phase_id == 1:
            self.time_until_next_enemy_step -= delta_time
            if self.time_until_next_enemy_step <= 0:
                self.update_possible_enemy_steps()
                current_enemy_step: list = self.determine_current_enemy_step()
                self.execute_enemy_step(current_enemy_step)
                self.possible_enemy_steps.remove(current_enemy_step)
                if len(self.possible_enemy_steps) == 0:
                    self.time_until_next_enemy_step = None
                    self.reset_enemy_step_attributes()
                    self.phase_id = 0
                else:
                    self.time_until_next_enemy_step = self.time_between_enemy_steps
        else:
            print(self.get_not_a_compatible_phase_id_line())
            exit()

    def create_enemy_list(self):
        for current_row_number in range(self.amount_of_tile_rows):
            for current_column_number in range(self.amount_of_tile_columns):
                current_starting_tile_id = self.starting_tiles[current_row_number][current_column_number]
                if current_starting_tile_id == 1:
                    current_enemy = FistsPerson()
                    current_enemy.window = self
                    current_enemy.tile_x = current_column_number
                    current_enemy.tile_y = current_row_number
                    current_enemy.set_position_from_tile_and_offset()
                    current_enemy.set_size_from_tile_ratio()
                    self.enemy_list.append(current_enemy)

    def update_grid_tile_array(self):
        self.grid_tiles: list = [[None] * self.amount_of_tile_columns for _ in range(self.amount_of_tile_rows)]
        for current_enemy in self.enemy_list:
            self.grid_tiles[current_enemy.tile_y][current_enemy.tile_x] = current_enemy
        self.grid_tiles[self.player.tile_y][self.player.tile_x] = self.player

    def update_possible_enemy_steps(self):
        self.possible_enemy_steps = []
        for current_enemy in self.enemy_list:
            if current_enemy.can_move and not current_enemy.has_moved:
                self.possible_enemy_steps.append([current_enemy, 0])

    def determine_current_enemy_step(self):
        current_enemy_step = self.possible_enemy_steps[0]
        return current_enemy_step

    def execute_enemy_step(self, enemy_step: list):
        if enemy_step[1] == 0:
            movement_direction = enemy_step[0].determine_movement_direction()
            enemy_step[0].move(movement_direction)
        else:
            print(get_not_a_compatible_enemy_step_line(enemy_step))
            exit()

    def reset_enemy_step_attributes(self):
        for current_enemy in self.enemy_list:
            if current_enemy.can_move:
                current_enemy.has_moved = False

    def on_key_press(self, pressed_key: int, modifiers: int):
        if self.player.can_move is None:
            print(self.player.get_movement_not_set_line())
            exit()
        elif self.player.can_move and not self.player.has_moved and self.phase_id == 0:
            if pressed_key == key.W:
                self.player.move(0)
            elif pressed_key == key.S:
                self.player.move(1)
            elif pressed_key == key.A:
                self.player.move(2)
            elif pressed_key == key.D:
                self.player.move(3)


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

    def get_movement_not_set_line(self):
        line: str = f"Error: Entity {self}'s ability to move isn't set"
        return line

    def __init__(self):
        super().__init__()
        self.tile_x = None
        self.tile_y = None
        self.tile_x_offset_ratio: float = self.TILE_X_OFFSET_RATIO
        self.tile_y_offset_ratio: float = self.TILE_Y_OFFSET_RATIO
        self.size_tile_ratio: float = self.SIZE_TILE_RATIO
        self.line_width: float = self.LINE_WIDTH
        self.tilt_angle: float = self.TILT_ANGLE
        self.can_move = None
        self.has_moved: bool = False

    def draw(self):
        draw.square_outline(self.x, self.y, self.size, self.color, self.line_width, self.tilt_angle)

    def move(self, direction_id: int):
        if direction_id == 2:
            resulting_tile_x = self.tile_x - 1
        elif direction_id == 3:
            resulting_tile_x = self.tile_x + 1
        else:
            resulting_tile_x = self.tile_x
        if direction_id == 0:
            resulting_tile_y = self.tile_y + 1
        elif direction_id == 1:
            resulting_tile_y = self.tile_y - 1
        else:
            resulting_tile_y = self.tile_y
        if 0 <= resulting_tile_x < self.window.amount_of_tile_columns \
                and 0 <= resulting_tile_y < self.window.amount_of_tile_rows:
            self.tile_x = resulting_tile_x
            self.tile_y = resulting_tile_y
            self.set_position_from_tile_and_offset()
            self.window.update_grid_tile_array()
            self.has_moved: bool = True


class Player(Entity):
    COLOR = (255, 255, 255)
    CAN_MOVE: bool = True

    def __init__(self):
        super().__init__()
        self.color = self.COLOR
        self.can_move: bool = self.CAN_MOVE

    def on_draw(self):
        self.draw()


class Enemy(Entity):
    COLOR = (255, 0, 0)

    def __init__(self):
        super().__init__()
        self.color = self.COLOR

    def determine_movement_direction(self):
        player = self.window.player
        if player.tile_x + player.tile_y > self.tile_x + self.tile_y:
            if player.tile_x - player.tile_y > self.tile_x - self.tile_y:
                movement_direction = 3
            else:
                movement_direction = 0
        else:
            if player.tile_x - player.tile_y > self.tile_x - self.tile_y:
                movement_direction = 1
            else:
                movement_direction = 2
        return movement_direction


class FistsPerson(Enemy):
    CAN_MOVE: bool = True

    def __init__(self):
        super().__init__()
        self.can_move = self.CAN_MOVE

    def on_draw(self):
        self.draw()


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
    window.starting_tiles = [[0] * window.amount_of_tile_columns for _ in range(window.amount_of_tile_rows)]
    window.starting_tiles[6][6] = 1
    window.create_enemy_list()
    window.update_grid_tile_array()
    window.update_drawables()
    window.phase_id = 0
    window.time_between_enemy_steps = .25

    # Running the program until the window closes
    run()


# Running main function
if __name__ == "__main__":
    main()
