# Importing libraries
from arcade import key
from arcade import run
import random as r
import numpyplus_12 as np
import grid_window_12 as grid
import draw_on_grid_12 as draw


# Defining get text functions
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
                 ui_height_tile_ratio: float, title: str, background_color):
        # Making the new window and setting its background color
        super().__init__(tile_size, amount_of_tile_columns, amount_of_tile_rows, title, background_color,
                         0, ui_height_tile_ratio)
        self.drawables: list = self.drawables
        self.starting_tiles = None
        self.grid_tiles = None
        self.phase_id = None
        self.player = None
        self.movement_step_bar = None
        self.attack_step_bar = None
        self.enemy_list: list = []
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
        self.drawables: list = [self.grid_lines, self.movement_step_bar, self.attack_step_bar] + self.enemy_list
        if self.player.current_health > 0:
            self.drawables.append(self.player)

    def on_update(self, delta_time: float):
        if self.phase_id == 0:
            if self.player.can_move is None or self.player.can_shoot is None:
                if self.player.can_move is None:
                    print(self.player.get_ability_to_move_not_set_line)
                if self.player.can_shoot is None:
                    print(self.player.get_ability_to_shoot_not_set_line)
                exit()
            if (self.player.has_moved or not self.player.can_move) \
                    and (self.player.has_shot or not self.player.can_shoot):
                self.reset_enemy_step_attributes()
                self.phase_id: int = 1
                self.time_until_next_enemy_step: float = self.time_between_enemy_steps

        elif self.phase_id == 1:
            self.time_until_next_enemy_step -= delta_time
            if self.time_until_next_enemy_step <= 0:
                self.update_possible_enemy_steps()
                current_chosen_enemy_step: list = self.determine_current_enemy_step()
                execute_enemy_step(current_chosen_enemy_step)
                self.possible_enemy_steps.remove(current_chosen_enemy_step)
                if len(self.possible_enemy_steps) == 0 and self.phase_id != -1:
                    self.time_until_next_enemy_step = None
                    self.player.reset_step_attributes()
                    self.phase_id: int = 0
                else:
                    self.time_until_next_enemy_step: float = self.time_between_enemy_steps

        elif self.phase_id != -1:
            print(self.get_not_a_compatible_phase_id_line())
            exit()

    def update_grid_tile_array(self):
        self.grid_tiles: list = [[None] * self.amount_of_tile_columns for _ in range(self.amount_of_tile_rows)]
        for current_enemy in self.enemy_list:
            self.grid_tiles[current_enemy.tile_y][current_enemy.tile_x]: object = current_enemy
        self.grid_tiles[self.player.tile_y][self.player.tile_x]: object = self.player

    def get_entity(self, tile_x: int, tile_y: int):
        if 0 <= tile_x < self.amount_of_tile_columns and 0 <= tile_y < self.amount_of_tile_rows:
            entity: object = self.grid_tiles[tile_y][tile_x]
        else:
            entity: str = "OoB"
        return entity

    def is_tile_empty(self, tile_x: int, tile_y: int):
        if self.get_entity(tile_x, tile_y) is None:
            return True
        else:
            return False

    def create_enemy_list(self):
        for current_row_number in range(self.amount_of_tile_rows):
            for current_column_number in range(self.amount_of_tile_columns):
                current_starting_tile_id: int = self.starting_tiles[current_row_number][current_column_number]
                if current_starting_tile_id == 1:
                    current_enemy = FistsPerson(current_column_number, current_row_number)
                    current_enemy.window = self
                    current_enemy.set_position_from_tile_and_offset()
                    current_enemy.set_size_from_tile_ratio()
                    self.enemy_list.append(current_enemy)

    def update_possible_enemy_steps(self):
        self.possible_enemy_steps: list = []
        for current_enemy in self.enemy_list:
            if self.player.can_move is None or self.player.can_shoot is None:
                if self.player.can_move is None:
                    print(self.player.get_ability_to_move_not_set_line)
                if self.player.can_shoot is None:
                    print(self.player.get_ability_to_shoot_not_set_line)
                exit()

            if current_enemy.can_move and not current_enemy.has_moved:
                self.possible_enemy_steps.append([current_enemy, 0])
            if current_enemy.can_shoot and not current_enemy.has_shot:
                self.possible_enemy_steps.append([current_enemy, 1])

    def determine_current_enemy_step(self):
        closest_enemy_steps: list = []
        closest_enemy_distance_to_player = None
        for current_enemy_step in self.possible_enemy_steps:
            current_enemy_distance_to_player: float = current_enemy_step[0].get_tile_distance_to_player()
            if closest_enemy_distance_to_player is None \
                    or current_enemy_distance_to_player < closest_enemy_distance_to_player:
                closest_enemy_steps: list = [current_enemy_step]
                closest_enemy_distance_to_player = current_enemy_distance_to_player
            elif current_enemy_distance_to_player == closest_enemy_distance_to_player:
                closest_enemy_steps.append(current_enemy_step)

        chosen_enemy_step: list = np.random_element_from_list(closest_enemy_steps)
        return chosen_enemy_step

    def reset_enemy_step_attributes(self):
        for current_enemy in self.enemy_list:
            current_enemy.reset_step_attributes()

    def on_key_press(self, pressed_key: int, modifiers: int):
        if modifiers == modifiers:
            if self.player.can_move is None:
                print(self.player.get_ability_to_move_not_set_line())
                exit()
            elif self.player.can_move and not self.player.has_moved:
                if pressed_key == key.W:
                    self.player.move(0)
                elif pressed_key == key.S:
                    self.player.move(1)
                elif pressed_key == key.A:
                    self.player.move(2)
                elif pressed_key == key.D:
                    self.player.move(3)

    def on_game_over(self):
        self.phase_id = -1
        for current_drawable in self.drawables:
            current_drawable.on_game_over()


class Drawable(draw.Able):
    INITIAL_TRANSPARENCY: int = 255
    TRANSPARENCY_DECREASE_ON_GAME_OVER_RATIO: float = 1/2

    def __init__(self):
        super().__init__()
        self.transparency: int = self.INITIAL_TRANSPARENCY

    def on_game_over(self):
        self.transparency: int = int(self.transparency * self.TRANSPARENCY_DECREASE_ON_GAME_OVER_RATIO)
        self.set_full_color_from_color_and_transparency()


class GridLines(grid.Lines, Drawable):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.draw()


class UICounter(Drawable):
    def __init__(self):
        super().__init__()
        self.empty_color = None
        self.empty_full_color = None

    def set_empty_full_color_from_empty_color_and_transparency(self):
        self.empty_full_color = tuple([current_element for current_element in self.empty_color] + [self.transparency])

    def on_game_over(self):
        super().on_game_over()
        self.set_empty_full_color_from_empty_color_and_transparency()


class StepBar(UICounter):
    Y_UI_RATIO = 1/2
    SIZE_RATIO = 1/4
    WIDTH = 2

    def __init__(self):
        super().__init__()
        self.y_ui_ratio = self.Y_UI_RATIO
        self.y = None
        self.size_ratio = self.SIZE_RATIO
        self.line_width = self.WIDTH

    def set_y_from_ui_ratio(self):
        self.y = self.y_ui_ratio * self.window.bottom_margin_width


class MovementStepBar(StepBar):
    X_RATIO = 1/6
    COLOR = (0, 255, 255)
    EMPTY_COLOR = (0, 64, 64)

    def __init__(self):
        super().__init__()
        self.x_ratio = self.X_RATIO
        self.color = self.COLOR
        self.empty_color = self.EMPTY_COLOR
        self.set_full_color_from_color_and_transparency()
        self.set_empty_full_color_from_empty_color_and_transparency()

    def draw(self):
        if self.window.player.can_move:
            if not self.window.player.has_moved:
                current_color = self.full_color
            else:
                current_color = self.empty_full_color
            draw.cl_horizontal_line(self.x, self.size, self.y, current_color, self.line_width)

    def on_draw(self):
        self.draw()


class AttackStepBar(StepBar):
    X_RATIO = 1/2
    COLOR = (255, 255, 0)
    EMPTY_COLOR = (64, 64, 0)

    def __init__(self):
        super().__init__()
        self.x_ratio = self.X_RATIO
        self.color = self.COLOR
        self.empty_color = self.EMPTY_COLOR
        self.set_full_color_from_color_and_transparency()
        self.set_empty_full_color_from_empty_color_and_transparency()

    def draw(self):
        if self.window.player.can_shoot:
            if not self.window.player.has_shot:
                current_color = self.full_color
            else:
                current_color = self.empty_full_color
            draw.cl_horizontal_line(self.x, self.size, self.y, current_color, self.line_width)

    def on_draw(self):
        self.draw()


class Entity(Drawable):
    TILE_X_OFFSET_RATIO: float = 1/2
    TILE_Y_OFFSET_RATIO: float = 1/2
    SIZE_TILE_RATIO: float = 1/3
    LINE_WIDTH: float = 1
    TILT_ANGLE: float = 45

    def get_no_on_death_command_line(self):
        line: str = f"Error: Entity {self} has no command on death"
        return line

    def get_ability_to_move_not_set_line(self):
        line: str = f"Error: Entity {self}'s ability to move isn't set"
        return line

    def get_ability_to_jab_not_set_line(self):
        line: str = f"Error: Entity {self}'s ability to jab isn't set"
        return line

    def get_ability_to_shoot_not_set_line(self):
        line: str = f"Error: Entity {self}'s ability to shoot isn't set"
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
        self.can_shoot = None
        self.has_shot: bool = False

    def draw(self):
        draw.square_outline(self.x, self.y, self.size, self.full_color, self.line_width, self.tilt_angle)

    def full_heal(self):
        self.current_health: int = self.max_health

    def damage(self, damage_amount):
        self.current_health -= damage_amount
        if self.current_health <= 0:
            self.die()

    def die(self):
        self.current_health: int = 0
        self.can_move: bool = False
        self.can_jab: bool = False
        self.can_shoot: bool = False
        self.window.update_drawables()
        if self == self.window.player:
            self.window.on_game_over()
        else:
            print(self.get_no_on_death_command_line())
            quit()

    def move(self, direction_id: int):
        if direction_id == 2:
            resulting_tile_x: int = self.tile_x - 1
        elif direction_id == 3:
            resulting_tile_x: int = self.tile_x + 1
        else:
            resulting_tile_x: int = self.tile_x

        if direction_id == 0:
            resulting_tile_y: int = self.tile_y + 1
        elif direction_id == 1:
            resulting_tile_y: int = self.tile_y - 1
        else:
            resulting_tile_y: int = self.tile_y

        if self.window.is_tile_empty(resulting_tile_x, resulting_tile_y):
            self.tile_x: int = resulting_tile_x
            self.tile_y: int = resulting_tile_y
            self.set_position_from_tile_and_offset()
            if self == self.window.player:
                self.health_bar.update_position()
            self.window.update_grid_tile_array()

        elif self.can_jab is None:
            print(self.get_ability_to_jab_not_set_line())
            exit()

        elif self.can_jab:
            jabbed_entity = self.window.get_entity(resulting_tile_x, resulting_tile_y)
            jabbed_entity.damage(1)

        self.has_moved: bool = True

    def reset_step_attributes(self):
        if self.can_move is None or self.can_shoot is None:
            if self.can_move is None:
                print(self.player.get_ability_to_move_not_set_line)
            if self.can_shoot is None:
                print(self.player.get_ability_to_shoot_not_set_line)
            exit()

        if self.can_move:
            self.has_moved = False
        if self.can_shoot:
            self.has_shot = False


class Player(Entity):
    COLOR = (255, 255, 255)
    CAN_INITIALLY_MOVE: bool = True
    CAN_INITIALLY_JAB: bool = False
    CAN_INITIALLY_SHOOT: bool = False

    def __init__(self, starting_tile_x: int, starting_tile_y: int, starting_max_health: int):
        super().__init__(starting_tile_x, starting_tile_y)
        self.color = self.COLOR
        self.set_full_color_from_color_and_transparency()
        self.max_health: int = starting_max_health
        self.full_heal()
        self.health_bar = HealthBar(self)
        self.can_move: bool = self.CAN_INITIALLY_MOVE
        self.can_jab: bool = self.CAN_INITIALLY_JAB
        self.can_shoot: bool = self.CAN_INITIALLY_SHOOT

    def on_draw(self):
        self.draw()
        self.health_bar.on_draw()


class Enemy(Entity):
    COLOR = (255, 0, 0)

    def __init__(self, starting_tile_x: int, starting_tile_y: int):
        super().__init__(starting_tile_x, starting_tile_y)
        self.color = self.COLOR
        self.set_full_color_from_color_and_transparency()

    def get_tile_distance_to_player(self):
        player = self.window.player
        distance: float = np.distance_of_two_points((player.tile_x, player.tile_y), (self.tile_x, self.tile_y))
        return distance

    def determine_movement_direction(self):
        player = self.window.player
        surrounding_entities: list \
            = [self.window.get_entity(self.tile_x, self.tile_y + 1),
               self.window.get_entity(self.tile_x, self.tile_y - 1),
               self.window.get_entity(self.tile_x - 1, self.tile_y),
               self.window.get_entity(self.tile_x + 1, self.tile_y)]

        if self.can_jab:
            movement_direction_priority: list = [0, 1, 2, 3]
            for current_movement_direction_id in movement_direction_priority:
                if surrounding_entities[current_movement_direction_id] == player:
                    movement_direction_id: int = current_movement_direction_id
                    return movement_direction_id

        if np.greater_than_or_randomly_equal_to(player.tile_x, self.tile_x):
            if np.greater_than_or_randomly_equal_to(player.tile_y, self.tile_y):
                if np.greater_than_or_randomly_equal_to(player.tile_x - player.tile_y, self.tile_x - self.tile_y):
                    movement_direction_priority: list = [3, 0, 1, 2]
                else:
                    movement_direction_priority: list = [0, 3, 2, 1]
            else:
                if np.greater_than_or_randomly_equal_to(player.tile_x + player.tile_y, self.tile_x + self.tile_y):
                    movement_direction_priority: list = [3, 1, 0, 2]
                else:
                    movement_direction_priority: list = [1, 3, 2, 0]
        else:
            if np.greater_than_or_randomly_equal_to(player.tile_y, self.tile_y):
                if np.greater_than_or_randomly_equal_to(player.tile_x + player.tile_y, self.tile_x + self.tile_y):
                    movement_direction_priority: list = [0, 2, 3, 1]
                else:
                    movement_direction_priority: list = [2, 0, 1, 3]
            else:
                if np.greater_than_or_randomly_equal_to(player.tile_x - player.tile_y, self.tile_x - self.tile_y):
                    movement_direction_priority: list = [1, 2, 3, 0]
                else:
                    movement_direction_priority: list = [2, 1, 0, 3]

        for current_movement_direction_id in movement_direction_priority:
            if surrounding_entities[current_movement_direction_id] is None:
                movement_direction_id: int = current_movement_direction_id
                break
        else:
            movement_direction_id: int = r.randrange(0, 4)

        return movement_direction_id


class FistsPerson(Enemy):
    MAX_HEALTH: int = 1
    CAN_INITIALLY_MOVE: bool = True
    CAN_INITIALLY_JAB: bool = True
    CAN_INITIALLY_SHOOT: bool = False

    def __init__(self, starting_tile_x: int, starting_tile_y: int):
        super().__init__(starting_tile_x, starting_tile_y)
        self.max_health: int = self.MAX_HEALTH
        self.full_heal()
        self.can_move: bool = self.CAN_INITIALLY_MOVE
        self.can_jab: bool = self.CAN_INITIALLY_JAB
        self.can_shoot: bool = self.CAN_INITIALLY_SHOOT

    def on_draw(self):
        self.draw()


class HealthBar(UICounter):
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
        self.set_full_color_from_color_and_transparency()
        self.set_empty_full_color_from_empty_color_and_transparency()
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
        self.segment_distance_ratio: float = 1 / (total_segment_amount + 1)

    def set_segment_distance_from_ratio(self):
        self.segment_distance: float = self.segment_distance_ratio * self.window.tile_size

    def set_size_tile_ratio_from_segment_distance_ratio(self):
        self.size_tile_ratio: float = self.segment_distance_ratio * 2 / 3

    def draw(self):
        total_segment_amount: int = self.entity.max_health
        for current_segment_number in range(total_segment_amount):
            current_segment_offset: float = \
                self.segment_distance * (current_segment_number - (total_segment_amount - 1) / 2)
            current_segment_x: float = self.x + current_segment_offset
            if self.entity.current_health > current_segment_number:
                current_segment_color = self.full_color
            else:
                current_segment_color = self.empty_full_color
            draw.cl_horizontal_line(current_segment_x, self.size, self.y, current_segment_color, self.line_width)

    def on_draw(self):
        self.draw()


# Defining functions
def execute_enemy_step(enemy_step: list):
    if enemy_step[1] == 0:
        movement_direction_id: int = enemy_step[0].determine_movement_direction()
        enemy_step[0].move(movement_direction_id)
    else:
        print(get_not_a_compatible_enemy_step_line(enemy_step))
        exit()


# Running main function
def main():
    # Making class constants
    grid_lines = GridLines()
    grid_lines.color = (128, 128, 128)
    grid_lines.transparency = 255
    grid_lines.set_full_color_from_color_and_transparency()
    grid_lines.line_width = 2
    movement_step_bar = MovementStepBar()
    attack_step_bar = AttackStepBar()
    player = Player(1, 1, 3)

    # Making class constants for the window
    window = Window(48, 8, 8, 2/3, "Test", (0, 0, 0))
    window.grid_lines = grid_lines
    window.grid_lines.window = window
    window.starting_tiles = [[0] * window.amount_of_tile_columns for _ in range(window.amount_of_tile_rows)]
    window.starting_tiles[6][6] = 1
    window.starting_tiles[0][7] = 1
    window.player = player
    window.player.window = window
    window.player.set_size_from_tile_ratio()
    window.player.health_bar.window = window
    window.player.health_bar.set_segment_distance_ratio_from_max_health()
    window.player.health_bar.set_segment_distance_from_ratio()
    window.player.health_bar.set_size_tile_ratio_from_segment_distance_ratio()
    window.player.health_bar.set_size_from_tile_ratio()
    window.movement_step_bar = movement_step_bar
    window.movement_step_bar.window = window
    window.movement_step_bar.set_x_from_ratio()
    window.movement_step_bar.set_y_from_ui_ratio()
    window.movement_step_bar.set_size_from_ratio()
    window.attack_step_bar = attack_step_bar
    window.attack_step_bar.window = window
    window.attack_step_bar.set_x_from_ratio()
    window.attack_step_bar.set_y_from_ui_ratio()
    window.attack_step_bar.set_size_from_ratio()
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
