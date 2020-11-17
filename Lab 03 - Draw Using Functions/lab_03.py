# Importing libraries
from arcade import run
from numpy import pi
import draw_objects_03 as draw
import text_03 as text

# Making general constants
MODE_0_TITLE: str = "Selecting Mode"
MODE_1_TITLE: str = "Nitro Noir"
MODE_2_TITLE: str = "Nitro Nimbus"
ASK_MODE_LINE_3: str = "Which mode do you want to select?"
ASK_MODE_LINE_4: str = "(Type \"A\" or \"B\", otherwise it won't work)"
NOT_A_MODE_LINE: str = "See? I told you it wouldn't work."
THIN_LINE_WIDTH: float = 1/2
LIGHT_LINE_COLOR = (255, 255, 255)
ROAD_LINE_AMOUNT: int = 128
ROAD_LINE_FREQUENCY: float = 1/3
ROAD_LINE_WIDTH_DECREASE_RATIO: float = 1/6
MODE_2_ROAD_LINE_STARTING_COLOR = (255, 0, 0)
MODE_2_ROAD_LINE_HUE_INCREMENT: float = 1 / pi ** 2
MODE_1_ROAD_SIDE_LINE_COLOR = (64, 64, 64)
MODE_2_HORIZON_LINE_WIDTH: float = 1
MODE_2_MOON_LINE_COLOR = (0, 255, 255)

# Making constants from other constants
ASK_MODE_LINE_1: str = f"Mode A = {MODE_1_TITLE}"
ASK_MODE_LINE_2: str = f"Mode B = {MODE_2_TITLE}"
ASK_MODE_LINES: list = [ASK_MODE_LINE_1, ASK_MODE_LINE_2, ASK_MODE_LINE_3, ASK_MODE_LINE_4]


# Defining classes
class Window(draw.Window):
    """
    Class for this lab's window.
    """
    def __init__(self, width: int = 800, height: int = 600, title: str = "Default Mode", background_color=(0, 0, 0)):
        """
        Constructs the window and sets its background color.

        :param width: Window width
        :param height: Window height
        :param title: Title (appears in title bar)
        :param background_color: List of 3 or 4 bytes in RGB/RGBA format.
        """
        # Making the window and setting its background color
        super().__init__(width, height, title, background_color)

        # Creating additional class attributes
        self.starting_road_line = None
        self.road_line_hue_increment = None
        self.road_side_lines = None
        self.horizon_line = None

    def on_draw(self):
        """
        The window's on draw method.
        """
        # Starting to render the window
        super().on_draw()

        # Drawing the objects in the drawables list
        self.draw_drawables()

        # Drawing the road
        draw.road(self.starting_road_line, self.road_side_lines, self.horizon_line,
                  self.width, self.width / 2, ROAD_LINE_AMOUNT, ROAD_LINE_FREQUENCY,
                  0, ROAD_LINE_WIDTH_DECREASE_RATIO, self.road_line_hue_increment)


class Star(draw.Star):
    """
    Class for this lab's drawable stars.
    """
    def __init__(self):
        """
        Creates class attributes.
        """
        super().__init__()

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        self.draw()


class Moon(draw.Moon):
    """
    Class for this lab's drawable moon.
    """
    def __init__(self):
        """
        Creates class attributes.
        """
        super().__init__()

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        self.draw_outline()


# Defining main function
def main():
    """
    Main function of lab 3
    """

    # --- Initiating main function ---

    # Making class constants for the ground
    starting_road_line = draw.Able()
    starting_road_line.y_ratio = 1/20
    starting_road_line.line_width = 2
    road_side_lines: object = draw.Able()
    horizon_line = draw.Able()
    horizon_line.y_ratio = 1/2

    # Making class constants for the sky
    moon = Moon()
    moon.x_ratio = 4/5
    moon.y_ratio = 7/8
    moon.size_ratio = 1/16
    moon.line_width = 2
    moon.tilt_angle = 16
    moon.phase_ratio = 3/5
    dim_star = Star()
    dim_star.x_ratio = 1/7
    dim_star.y_ratio = 8/9
    dim_star.size = 6
    dim_star.line_width = 1/2
    dim_star.line_amount = 3
    star = Star()
    star.x_ratio = 3/4
    star.y_ratio = 3/5
    star.size = 7
    star.line_width = 1
    star.line_amount = 3
    bright_star = Star()
    bright_star.x_ratio = 1/3
    bright_star.y_ratio = 3/4
    bright_star.size = 8
    bright_star.line_width = 1
    bright_star.line_amount = 4

    # Making class constants from other constants
    starting_road_line.size_ratio = 1 - (starting_road_line.y_ratio / horizon_line.y_ratio)
    road_side_lines.line_width = THIN_LINE_WIDTH
    horizon_line.color = LIGHT_LINE_COLOR
    dim_star.color = LIGHT_LINE_COLOR
    star.color = LIGHT_LINE_COLOR
    bright_star.color = LIGHT_LINE_COLOR

    # Making variables
    mode_name: str = MODE_0_TITLE
    road_line_hue_increment = None
    starting_road_line.color = None
    road_side_lines.color = None
    horizon_line.line_width = None
    moon.color = None

    # --- Selecting mode ---

    # Asking the user which mode they would want
    text.print_lines(ASK_MODE_LINES)
    response: str = input(text.INPUT_LINE)

    # Setting the mode to what they requested and setting other variables respectively
    if response.lower() == "a":
        mode_name: str = MODE_1_TITLE
        road_line_hue_increment = 0
        starting_road_line.color = LIGHT_LINE_COLOR
        road_side_lines.color = MODE_1_ROAD_SIDE_LINE_COLOR
        horizon_line.line_width = THIN_LINE_WIDTH
        moon.color = LIGHT_LINE_COLOR
    elif response.lower() == "b":
        mode_name: str = MODE_2_TITLE
        road_line_hue_increment = MODE_2_ROAD_LINE_HUE_INCREMENT
        starting_road_line.color = MODE_2_ROAD_LINE_STARTING_COLOR
        road_side_lines.color = LIGHT_LINE_COLOR
        horizon_line.line_width = MODE_2_HORIZON_LINE_WIDTH
        moon.color = MODE_2_MOON_LINE_COLOR
    else:
        print(NOT_A_MODE_LINE)
        quit()

    # --- Making window ---

    # Making class constants for the window
    window: object = Window(512, 512, mode_name, (0, 0, 0))
    window.starting_road_line = starting_road_line
    window.starting_road_line.window = window
    window.starting_road_line.set_y_from_ratio()
    window.starting_road_line.set_size_from_ratio()
    window.road_line_hue_increment = road_line_hue_increment
    window.road_side_lines = road_side_lines
    window.road_side_lines.window = window
    window.horizon_line = horizon_line
    window.horizon_line.window = window
    window.horizon_line.set_y_from_ratio()
    window.drawables = [moon, dim_star, star, bright_star]
    for current_drawable in window.drawables:
        # Making class constants for each of the window's drawables
        current_drawable.window = window
        current_drawable.set_position_from_ratio()
        if current_drawable == moon:
            current_drawable.set_size_from_ratio(False)

    # --- Running until window closes ---

    run()


# Running main function
if __name__ == "__main__":
    main()
