# Importing libraries
import window_12 as w
import draw_shapes_12 as draw

# Making constants
NULL_DIRECTION = -1
UP_DIRECTION = 0
DOWN_DIRECTION = 1
LEFT_DIRECTION = 2
RIGHT_DIRECTION = 3


# Defining get text functions
def get_not_a_compatible_direction_id_line(direction_id: int):
    line: str = f"Error: {direction_id} is not a compatible direction id"
    return line


# Defining classes
class Window(w.Window):
    """
    Class for windows with grids.
    """
    def __init__(self, tile_size: int, amount_of_tile_columns: int, amount_of_tile_rows: int,
                 title: str, background_color, top_margin_width_ratio: float = 0, bottom_margin_width_ratio: float = 0,
                 left_margin_width_ratio: float = 0, right_margin_width_ratio: float = 0):
        """
        Constructs a new window as well as set the window's background color.

        :param tile_size: size of a grid tile.
        :param amount_of_tile_columns: amount of grid tiles wide the window is.
        :param amount_of_tile_rows: amount of grid tiles tall the window is.
        :param title: Title (appears in title bar)
        :param background_color: List of 3 or 4 bytes in RGB/RGBA format.
        :param top_margin_width_ratio:
        :param bottom_margin_width_ratio:
        :param left_margin_width_ratio:
        :param right_margin_width_ratio:
        """
        # Creating class attributes
        self.tile_size: int = tile_size
        self.amount_of_tile_columns: int = amount_of_tile_columns
        self.amount_of_tile_rows: int = amount_of_tile_rows
        self.top_margin_width_ratio: float = top_margin_width_ratio
        self.top_margin_width = 0
        self.bottom_margin_width_ratio: float = bottom_margin_width_ratio
        self.bottom_margin_width = 0
        self.left_margin_width_ratio: float = left_margin_width_ratio
        self.left_margin_width = 0
        self.right_margin_width_ratio: float = right_margin_width_ratio
        self.right_margin_width = 0
        self.get_margin_widths_from_ratios()
        self.mouse_tile_x = None
        self.mouse_tile_y = None
        self.out_of_bounds_id = None
        self.mouse_on_grid = False
        self.grid_lines = None

        # Creating class attributes from other attributes
        window_width = self.amount_of_tile_columns * self.tile_size + self.left_margin_width + self.right_margin_width
        window_height = self.amount_of_tile_rows * self.tile_size + self.top_margin_width + self.bottom_margin_width
        super().__init__(window_width, window_height, title, background_color)

    def get_margin_widths_from_ratios(self):
        self.top_margin_width: int = int(self.top_margin_width_ratio * self.tile_size)
        self.bottom_margin_width: int = int(self.bottom_margin_width_ratio * self.tile_size)
        self.left_margin_width: int = int(self.left_margin_width_ratio * self.tile_size)
        self.right_margin_width: int = int(self.right_margin_width_ratio * self.tile_size)

    def get_tile_position_from_position(self, x: float, y: float):
        if self.left_margin_width <= x < self.width - self.right_margin_width:
            tile_x: int = int((x - self.left_margin_width) // self.tile_size)
        else:
            tile_x: str = self.out_of_bounds_id
        if self.bottom_margin_width <= (y - 1) < self.height - self.top_margin_width:
            tile_y: int = int((y - self.bottom_margin_width - 1) // self.tile_size)
        else:
            tile_y: str = self.out_of_bounds_id

        return tile_x, tile_y

    def update_mouse_tile_position(self):
        """

        """
        mouse_tile_x, mouse_tile_y = self.get_tile_position_from_position(self.mouse_x, self.mouse_y)
        self.mouse_tile_x = mouse_tile_x
        self.mouse_tile_y = mouse_tile_y

    def on_mouse_motion(self, mouse_x: float, mouse_y: float, mouse_dx: float, mouse_dy: float):
        """


        :param mouse_x:
        :param mouse_y:
        :param mouse_dx:
        :param mouse_dy:
        """
        super().on_mouse_motion(mouse_x, mouse_y, mouse_dx, mouse_dy)
        self.update_mouse_tile_position()
        if self.mouse_tile_x == self.out_of_bounds_id or self.mouse_tile_y == self.out_of_bounds_id:
            self.mouse_on_grid = False
        else:
            self.mouse_on_grid = True

    def on_mouse_enter(self, mouse_x: int, mouse_y: int):
        """


        :param mouse_x:
        :param mouse_y:
        """
        # [...]
        super().on_mouse_enter(mouse_x, mouse_y)
        self.update_mouse_tile_position()
        self.mouse_on_grid = True

    def on_mouse_leave(self, mouse_x: int, mouse_y: int):
        """


        :param mouse_x:
        :param mouse_y:
        """
        # [...]
        super().on_mouse_leave(mouse_x, mouse_y)
        self.update_mouse_tile_position()
        self.mouse_on_grid = False

    def on_mouse_press(self, mouse_x: float, mouse_y: float, mouse_button: int, modifiers: int):
        """


        :param mouse_x:
        :param mouse_y:
        :param mouse_button:
        :param modifiers:
        """
        super().on_mouse_press(mouse_x, mouse_y, mouse_button, modifiers)
        self.update_mouse_tile_position()


class Lines(draw.Able):
    """
    Class for drawable grid lines.
    """
    def __init__(self):
        """
        Creates class attributes.
        """
        super().__init__()

    def draw(self):
        """
        Draws grid lines between the grid tiles.
        """
        window = self.window
        top_line_number = window.amount_of_tile_rows
        if window.top_margin_width != 0:
            top_line_number += 1
        bottom_line_number = 1
        if window.bottom_margin_width != 0:
            bottom_line_number -= 1
        for current_line_number in range(bottom_line_number, top_line_number):
            # Drawing a horizontal grid line
            draw.horizontal_line(window.left_margin_width, window.width - window.right_margin_width,
                                 current_line_number * window.tile_size + window.bottom_margin_width,
                                 self.full_color, self.line_width)
        left_line_number = 1
        if window.left_margin_width != 0:
            left_line_number -= 1
        right_line_number = window.amount_of_tile_columns
        if window.right_margin_width != 0:
            right_line_number += 1
        for current_line_number in range(left_line_number, right_line_number):
            # Drawing a vertical grid line
            draw.vertical_line(current_line_number * window.tile_size + window.left_margin_width,
                               window.bottom_margin_width, window.height - window.top_margin_width,
                               self.full_color, self.line_width)

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        pass


def get_coordinates_from_direction_id(direction_id: int):
    """


    :param direction_id:
    :return:
    """
    if direction_id == LEFT_DIRECTION:
        x: int = -1
    elif direction_id == RIGHT_DIRECTION:
        x: int = 1
    else:
        x: int = 0

    if direction_id == UP_DIRECTION:
        y: int = 1
    elif direction_id == DOWN_DIRECTION:
        y: int = -1
    else:
        y: int = 0

    if x == 0 and y == 0 and direction_id != NULL_DIRECTION:
        print(get_not_a_compatible_direction_id_line(direction_id))
        exit()

    return x, y
