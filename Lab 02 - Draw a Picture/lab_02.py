# --- Initiating the code ---

# Importing libraries
import arcade
import numpy as np
import colorsys
import colorsysplus


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


def draw_road_lines(center_x: float, start_length: float, start_y: float, end_length: float, end_y: float,
                    amount: int, frequency: float, color,
                    start_width: float = 1, end_width: float = 1, width_decrease_ratio: float = 1/6,
                    rainbowness: float = 0):
    length = start_length
    y = start_y
    width = start_width
    for i in range(amount):
        draw_cl_horizontal_line(center_x, length, y, color, width)
        length = end_length * frequency + length * (1 - frequency)
        y = end_y * frequency + y * (1 - frequency)
        width = end_width * frequency + width * (1 - width_decrease_ratio)
        if rainbowness:
            color = increment_hue(color, rainbowness)


def draw_road(window_width: int, center_x: float, start_length: float, start_y: float, horizon_y: float,
              road_line_amount: int, road_line_frequency: float, road_color, road_side_color, horizon_color,
              road_line_start_width: float = 1, road_line_end_width: float = 1,
              road_side_width: float = 1/2, horizon_width: float = 1, road_line_width_decrease_ratio: float = 1/6,
              road_rainbowness: float = 0):
    # Drawing road lines
    draw_road_lines(center_x, start_length, start_y, 0, horizon_y, road_line_amount, road_line_frequency, road_color,
                    road_line_start_width, road_line_end_width, road_line_width_decrease_ratio, road_rainbowness)

    # Drawing horizon and road-side lines
    arcade.draw_line(0, 0, center_x, horizon_y, road_side_color, road_side_width)
    arcade.draw_line(window_width, 0, center_x, horizon_y, road_side_color, road_side_width)
    draw_horizontal_line(0, window_width, horizon_y, horizon_color, horizon_width)


def main():
    # Making general constants
    window_width = 512
    window_height = 512
    background_color = (0, 0, 0)
    mode_1_title = "Nitro Noir"
    mode_2_title = "Nitro Nimbus"
    thin_line_width = 1/2
    light_line_color = (255, 255, 255)
    curve_rendering = 1024

    # Making specific constants
    ask_mode_line_3 = "Which mode do you want to select?"
    ask_mode_line_4 = "(Type \"A\" or \"B\", otherwise it won't work)"
    not_a_mode_line = "See? I told you it wouldn't work."
    road_line_amount = 128
    road_line_starting_y_ratio = 1/20
    road_line_starting_width = 2
    road_line_width_decrease_ratio = 1/6
    mode_2_road_line_starting_color = (255, 0, 0)
    mode_2_road_line_hue_increment = 1 / np.pi ** 2
    road_line_frequency = 1/3
    mode_1_road_side_line_color = (64, 64, 64)
    horizon_y_ratio = 1/2
    mode_2_horizon_line_width = 1
    moon_x_ratio = 4/5
    moon_y_ratio = 7/8
    moon_tilt = 16
    moon_radius_ratio = 1/32
    moon_phase_ratio = 3/5
    moon_line_width = 2
    mode_2_moon_line_color = (0, 255, 255)

    # Making constants from other constants
    ask_mode_line_1 = "Mode A = " + mode_1_title
    ask_mode_line_2 = "Mode B = " + mode_2_title
    road_line_starting_length_ratio = 1 - (road_line_starting_y_ratio / horizon_y_ratio)
    road_line_starting_y = road_line_starting_y_ratio * window_height
    road_line_starting_length = road_line_starting_length_ratio * window_width
    horizon_y = horizon_y_ratio * window_height
    moon_x = moon_x_ratio * window_width
    moon_y = moon_y_ratio * window_height
    moon_radius = moon_radius_ratio * window_height

    # Making variables
    mode_name = "Selecting Mode"
    road_line_color = None
    road_line_hue_increment = None
    horizon_line_width = None
    road_side_line_color = None
    moon_line_color = None

    # --- Selecting modes ---

    # Asking the user which mode they want
    print(ask_mode_line_1)
    print(ask_mode_line_2)
    print(ask_mode_line_3)
    print(ask_mode_line_4)
    response = input()

    # Setting the mode to what they said
    if response.lower() == "a":
        mode_name = mode_1_title
        road_line_color = light_line_color
        road_line_hue_increment = 0
        road_side_line_color = mode_1_road_side_line_color
        horizon_line_width = thin_line_width
        moon_line_color = light_line_color
    elif response.lower() == "b":
        mode_name = mode_2_title
        road_line_color = mode_2_road_line_starting_color
        road_line_hue_increment = mode_2_road_line_hue_increment
        road_side_line_color = light_line_color
        horizon_line_width = mode_2_horizon_line_width
        moon_line_color = mode_2_moon_line_color
    else:
        print(not_a_mode_line)
        quit()

    # --- Making the window ---

    arcade.open_window(window_width, window_height, mode_name)
    arcade.set_background_color(background_color)

    # --- Rendering window ---

    arcade.start_render()

    # Drawing road
    draw_road(window_width, window_width / 2, road_line_starting_length, road_line_starting_y, horizon_y,
              road_line_amount, road_line_frequency, road_line_color, road_side_line_color, light_line_color,
              road_line_starting_width, 0, thin_line_width, horizon_line_width, road_line_width_decrease_ratio,
              road_line_hue_increment)

    # Drawing moon
    draw_moon_outline(moon_x, moon_y, moon_radius, moon_phase_ratio,
                      moon_line_color, moon_line_width, moon_tilt, curve_rendering)

    arcade.finish_render()

    # --- Running until window closes ---

    arcade.run()


if __name__ == "__main__":
    main()
