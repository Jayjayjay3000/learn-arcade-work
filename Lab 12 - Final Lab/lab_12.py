# Importing libraries
from arcade import key
from arcade import run
import random as r
import numpyplus_12 as np
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

    def create_enemy_list(self):
        for current_row_number in range(self.amount_of_tile_rows):
            for current_column_number in range(self.amount_of_tile_columns):
                current_starting_tile_id = self.starting_tiles[current_row_number][current_column_number]
                if current_starting_tile_id == 1:
                    current_enemy = FistsPerson(current_column_number, current_row_number)
                    current_enemy.window = self
                    current_enemy.set_position_from_tile_and_offset()
                    current_enemy.set_size_from_tile_ratio()
                    self.enemy_list.append(current_enemy)

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
                execute_enemy_step(current_enemy_step)
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
        closest_enemy_steps: list = []
        closest_enemy_distance_to_player = None
        for current_enemy_step in self.possible_enemy_steps:
            current_enemy_distance_to_player = current_enemy_step[0].get_tile_distance_to_player()
            if closest_enemy_distance_to_player is None \
                    or current_enemy_distance_to_player < closest_enemy_distance_to_player:
                closest_enemy_steps: list = [current_enemy_step]
                closest_enemy_distance_to_player = current_enemy_distance_to_player
            elif current_enemy_distance_to_player == closest_enemy_distance_to_player:
                closest_enemy_steps.append(current_enemy_step)

        chosen_enemy_step = np.random_element_from_list(closest_enemy_steps)
        return chosen_enemy_step

    def is_tile_empty(self, tile_x: int, tile_y: int):
        if 0 <= tile_x < self.amount_of_tile_columns and 0 <= tile_y < self.amount_of_tile_rows \
                and self.grid_tiles[tile_y][tile_x] is None:
            return True
        else:
            return False

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

    def __init__(self, starting_tile_x: int, starting_tile_y: int):
        super().__init__()
        self.tile_x: int = starting_tile_x
        self.tile_x_offset_ratio: float = self.TILE_X_OFFSET_RATIO
        self.tile_y: int = starting_tile_y
        self.tile_y_offset_ratio: float = self.TILE_Y_OFFSET_RATIO
        self.size_tile_ratio: float = self.SIZE_TILE_RATIO
        self.line_width: float = self.LINE_WIDTH
        self.tilt_angle: float = self.TILT_ANGLE
        self.max_health = None
        self.current_health = None
        self.can_move = None
        self.has_moved: bool = False
        self.can_jab = None

    def draw(self):
        draw.square_outline(self.x, self.y, self.size, self.color, self.line_width, self.tilt_angle)

    def full_heal(self):
        self.current_health = self.max_health

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

        if self.window.is_tile_empty(resulting_tile_x, resulting_tile_y):
            self.tile_x = resulting_tile_x
            self.tile_y = resulting_tile_y
            self.set_position_from_tile_and_offset()
            if self == self.window.player:
                self.health_bar.update_position()
            self.window.update_grid_tile_array()

        self.has_moved: bool = True


class Player(Entity):
    COLOR = (255, 255, 255)
    CAN_MOVE: bool = True
    CAN_JAB: bool = False

    def __init__(self, starting_tile_x: int, starting_tile_y: int, starting_max_health: int):
        super().__init__(starting_tile_x, starting_tile_y)
        self.color = self.COLOR
        self.max_health = starting_max_health
        self.full_heal()
        self.health_bar = HealthBar(self)
        self.can_move: bool = self.CAN_MOVE
        self.can_jab: bool = self.CAN_JAB

    def on_draw(self):
        self.draw()
        self.health_bar.on_draw()


class Enemy(Entity):
    COLOR = (255, 0, 0)

    def __init__(self, starting_tile_x: int, starting_tile_y: int):
        super().__init__(starting_tile_x, starting_tile_y)
        self.color = self.COLOR

    def get_tile_distance_to_player(self):
        player = self.window.player
        distance = np.distance_of_two_points((player.tile_x, player.tile_y), (self.tile_x, self.tile_y))
        return distance

    def determine_movement_direction(self):
        player = self.window.player
        is_surrounding_tile_empty: list \
            = [self.window.is_tile_empty(self.tile_x, self.tile_y + 1),
               self.window.is_tile_empty(self.tile_x, self.tile_y - 1),
               self.window.is_tile_empty(self.tile_x - 1, self.tile_y),
               self.window.is_tile_empty(self.tile_x + 1, self.tile_y)]

        if np.greater_than_or_randomly_equal_to(player.tile_x, self.tile_x):
            if np.greater_than_or_randomly_equal_to(player.tile_y, self.tile_y):
                if np.greater_than_or_randomly_equal_to(player.tile_x - player.tile_y, self.tile_x - self.tile_y):
                    movement_direction_priority = [3, 0, 1, 2]
                else:
                    movement_direction_priority = [0, 3, 2, 1]
            else:
                if np.greater_than_or_randomly_equal_to(player.tile_x + player.tile_y, self.tile_x + self.tile_y):
                    movement_direction_priority = [3, 1, 0, 2]
                else:
                    movement_direction_priority = [1, 3, 2, 0]
        else:
            if np.greater_than_or_randomly_equal_to(player.tile_y, self.tile_y):
                if np.greater_than_or_randomly_equal_to(player.tile_x + player.tile_y, self.tile_x + self.tile_y):
                    movement_direction_priority = [0, 2, 3, 1]
                else:
                    movement_direction_priority = [2, 0, 1, 3]
            else:
                if np.greater_than_or_randomly_equal_to(player.tile_x - player.tile_y, self.tile_x - self.tile_y):
                    movement_direction_priority = [1, 2, 3, 0]
                else:
                    movement_direction_priority = [2, 1, 0, 3]

        for current_movement_direction_id in movement_direction_priority:
            if is_surrounding_tile_empty[current_movement_direction_id]:
                movement_direction_id = current_movement_direction_id
                break
        else:
            movement_direction_id = r.randrange(0, 4)

        return movement_direction_id


class FistsPerson(Enemy):
    CAN_MOVE: bool = True
    CAN_JAB: bool = True
    MAX_HEALTH: int = 1

    def __init__(self, starting_tile_x: int, starting_tile_y: int):
        super().__init__(starting_tile_x, starting_tile_y)
        self.max_health: int = self.MAX_HEALTH
        self.full_heal()
        self.can_move: bool = self.CAN_MOVE
        self.can_jab: bool = self.CAN_JAB

    def on_draw(self):
        self.draw()


class HealthBar(Drawable):
    TILE_X_OFFSET_RATIO: float = 1/2
    TILE_Y_OFFSET_RATIO: float = 7/8
    COLOR = (0, 255, 0)
    EMPTY_COLOR = (96, 32, 32)
    WIDTH: float = 2

    def __init__(self, entity):
        super().__init__()
        self.tile_x = None
        self.tile_x_offset_ratio: float = self.TILE_X_OFFSET_RATIO
        self.tile_y = None
        self.tile_y_offset_ratio: float = self.TILE_Y_OFFSET_RATIO
        self.size_tile_ratio = None
        self.color = self.COLOR
        self.empty_color = self.EMPTY_COLOR
        self.line_width: float = self.WIDTH
        self.segment_distance = None
        self.segment_distance_ratio = None
        self.entity = entity

    def update_position(self):
        self.tile_x: int = self.entity.tile_x
        self.tile_y: int = self.entity.tile_y
        self.set_position_from_tile_and_offset()

    def set_segment_distance_ratio_from_max_health(self):
        total_segment_amount: int = self.entity.max_health
        self.segment_distance_ratio = 1 / (total_segment_amount + 1)

    def set_size_tile_ratio_from_segment_distance_ratio(self):
        self.size_tile_ratio = self.segment_distance_ratio * 2 / 3

    def set_segment_distance_from_ratio(self):
        self.segment_distance = self.segment_distance_ratio * self.window.tile_size

    def draw(self):
        total_segment_amount: int = self.entity.max_health
        for current_segment_number in range(total_segment_amount):
            current_segment_x = \
                self.x + self.segment_distance * (current_segment_number - (total_segment_amount - 1) / 2)
            if self.entity.current_health > current_segment_number:
                current_segment_color = self.color
            else:
                current_segment_color = self.empty_color
            draw.cl_horizontal_line(current_segment_x, self.size, self.y, current_segment_color, self.line_width)

    def on_draw(self):
        self.draw()


# Defining functions
def execute_enemy_step(enemy_step: list):
    if enemy_step[1] == 0:
        movement_direction_id = enemy_step[0].determine_movement_direction()
        enemy_step[0].move(movement_direction_id)
    else:
        print(get_not_a_compatible_enemy_step_line(enemy_step))
        exit()


# Running main function
def main():
    # Making class constants
    margins: object = Margins()
    margins.color = (128, 128, 128)
    margins.line_width = 2
    player = Player(1, 1, 3)

    # Making class constants for the window
    window = Window(48, 8, 8, "Test", (0, 0, 0))
    window.margins = margins
    window.margins.window = window
    window.player = player
    window.player.window = window
    window.player.set_size_from_tile_ratio()
    window.player.health_bar.window = window
    window.player.health_bar.set_segment_distance_ratio_from_max_health()
    window.player.health_bar.set_segment_distance_from_ratio()
    window.player.health_bar.set_size_tile_ratio_from_segment_distance_ratio()
    window.player.health_bar.set_size_from_tile_ratio()
    window.starting_tiles = [[0] * window.amount_of_tile_columns for _ in range(window.amount_of_tile_rows)]
    window.starting_tiles[6][6] = 1
    window.starting_tiles[0][7] = 1
    window.create_enemy_list()
    window.update_drawables()
    window.time_between_enemy_steps = .2

    # Initially updating variables
    window.player.set_position_from_tile_and_offset()
    window.player.health_bar.update_position()
    window.update_grid_tile_array()
    window.phase_id = 0

    # Running the program until the window closes
    run()


# Running main function
if __name__ == "__main__":
    main()
