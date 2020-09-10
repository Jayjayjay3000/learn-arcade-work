# --- Initiating the code ---

# Importing libraries
import arcade

# Making general constants
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512
BACKGROUND_COLOR = (0, 0, 0)
MODE_1_TITLE = "Nitro Noir"
# MODE_2_TITLE = "Nitro Nimbus"
THIN_LINE_WIDTH = 1/2
LINE_COLOR = (255, 255, 255)
DARK_LINE_COLOR = (64, 64, 64)
CURVE_RENDERING = 1024

# Making specific constants
# ASK_MODE_LINE_3 = "Which mode do you want to select?"
# ASK_MODE_LINE_4 = "(Type \"A\" or \"B\", otherwise it won't work)"
NUMBER_OF_ROAD_LINES = 128
ROAD_LINE_STARTING_Y_RATIO = 1/20
ROAD_LINE_STARTING_WIDTH = 2
ROAD_LINE_WIDTH_DECREASE_RATIO = 1/6
ROAD_LINE_FREQUENCY = 1/3
HORIZON_Y_RATIO = 1/2
MOON_X_RATIO = 4/5
MOON_Y_RATIO = 7/8
MOON_TILT = 16
MOON_RADIUS_RATIO = 1/32
MOON_PHASE_RATIO = 3/5
MOON_LINE_WIDTH = 2

# Making constants from other constants
# ASK_MODE_LINE_1 = "Mode A = " + MODE_1_TITLE
# ASK_MODE_LINE_2 = "Mode B = " + MODE_2_TITLE
ROAD_LINE_STARTING_LENGTH_RATIO = 1 - (ROAD_LINE_STARTING_Y_RATIO / HORIZON_Y_RATIO)
ROAD_LINE_STARTING_Y = ROAD_LINE_STARTING_Y_RATIO * WINDOW_HEIGHT
ROAD_LINE_STARTING_LENGTH = ROAD_LINE_STARTING_LENGTH_RATIO * WINDOW_WIDTH
HORIZON_Y = HORIZON_Y_RATIO * WINDOW_HEIGHT
MOON_X = MOON_X_RATIO * WINDOW_WIDTH
MOON_Y = MOON_Y_RATIO * WINDOW_HEIGHT
MOON_RADIUS = MOON_RADIUS_RATIO * WINDOW_HEIGHT
MOON_DIAMETER = MOON_RADIUS * 2

# Making variables
# mode = 0
# mode_name = "Selecting Mode"

# Making variables from constants
road_line_y = ROAD_LINE_STARTING_Y
road_line_length = ROAD_LINE_STARTING_LENGTH
road_line_width = ROAD_LINE_STARTING_WIDTH


# Making functions
def draw_horizontal_line(start_x: float, end_x: float, y: float, color, line_width: float = 1):
    arcade.draw_line(start_x, y, end_x, y, color, line_width)


def draw_cl_horizontal_line(center_x: float, length: float, y: float, color, line_width: float = 1):
    arcade.draw_line(center_x - length / 2, y, center_x + length / 2, y, color, line_width)


def draw_circle_arc_outline(center_x: float, center_y: float, radius: float,
                            color, start_angle: float, end_angle: float,
                            border_width: float = 1, tilt_angle: float = 0, num_segments: int = 128):
    arcade.draw_arc_outline(center_x, center_y, radius * 2, radius * 2,
                            color, start_angle, end_angle, border_width, tilt_angle, num_segments)


def draw_moon_outline(center_x: float, center_y: float, radius: float, phase_ratio: float,
                      color, border_width: float = 1, tilt_angle: float = 0, num_segments: int = 128):
    diameter = radius * 2
    phase = phase_ratio * diameter
    draw_circle_arc_outline(center_x, center_y, radius,
                            color, -90, 90, border_width, -tilt_angle, num_segments)
    arcade.draw_arc_outline(center_x, center_y, phase, diameter,
                            color, -90, 90, border_width, -tilt_angle, num_segments)


# --- Selecting modes (Currently unused) ---

# Asking the user which mode they want
# print(ASK_MODE_LINE_1)
# print(ASK_MODE_LINE_2)
# print(ASK_MODE_LINE_3)
# print(ASK_MODE_LINE_4)
# response = input()

# Setting the mode to what they said
# if response.lower() == "a":
#     mode = 1
mode_name = MODE_1_TITLE
# elif response.lower() == "b":
#     mode = 2
#     mode_name = MODE_2_TITLE

# --- Making the window ---

arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, mode_name, False, True)
arcade.set_background_color(BACKGROUND_COLOR)

# --- Rendering window ---

arcade.start_render()

# Drawing road lines
for i in range(NUMBER_OF_ROAD_LINES):
    draw_cl_horizontal_line(WINDOW_WIDTH / 2, road_line_length, road_line_y, LINE_COLOR, road_line_width)
    road_line_length = road_line_length * (1 - ROAD_LINE_FREQUENCY)
    road_line_y = HORIZON_Y * ROAD_LINE_FREQUENCY + road_line_y * (1 - ROAD_LINE_FREQUENCY)
    road_line_width = road_line_width * (1 - ROAD_LINE_WIDTH_DECREASE_RATIO)

# Drawing horizon and road-side lines
draw_horizontal_line(0, WINDOW_WIDTH, HORIZON_Y, LINE_COLOR, THIN_LINE_WIDTH)
arcade.draw_line(0, 0, WINDOW_WIDTH / 2, HORIZON_Y, DARK_LINE_COLOR, THIN_LINE_WIDTH)
arcade.draw_line(WINDOW_WIDTH, 0, WINDOW_WIDTH / 2, HORIZON_Y, DARK_LINE_COLOR, THIN_LINE_WIDTH)

# Drawing moon
draw_moon_outline(MOON_X, MOON_Y, MOON_RADIUS, MOON_PHASE_RATIO,
                  LINE_COLOR, MOON_LINE_WIDTH, MOON_TILT, CURVE_RENDERING)

arcade.finish_render()

# --- Running until window closes ---

arcade.run()
