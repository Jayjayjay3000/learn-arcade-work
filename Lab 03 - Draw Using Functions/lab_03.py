# Importing libraries
import arcade
import numpy as np
import draw_shapes_03 as draw


# Defining classes
class Drawable:
    def __init__(self):
        self.x_ratio = None
        self.x = None
        self.y_ratio = None
        self.y = None
        self.size_ratio = None
        self.size = None
        self.color = None
        self.line_width = None
        self.tilt_angle = None


class Moon(Drawable):
    def __init__(self):
        super().__init__()
        self.phase_ratio = None


class Star(Drawable):
    def __init__(self):
        super().__init__()
        self.line_amount = None


# Defining main function
def main():

    # --- Initiating main function ---

    # Making general constants
    window_width = 512
    window_height = 512
    background_color = (0, 0, 0)
    mode_1_title = "Nitro Noir"
    mode_2_title = "Nitro Nimbus"
    ask_mode_line_3 = "Which mode do you want to select?"
    ask_mode_line_4 = "(Type \"A\" or \"B\", otherwise it won't work)"
    not_a_mode_line = "See? I told you it wouldn't work."
    thin_line_width = 1/2
    light_line_color = (255, 255, 255)
    curve_rendering = 1024
    road_line_amount = 128
    road_line_frequency = 1/3
    road_line_width_decrease_ratio = 1/6
    mode_2_road_line_starting_color = (255, 0, 0)
    mode_2_road_line_hue_increment = 1 / np.pi ** 2
    mode_1_road_side_line_color = (64, 64, 64)
    mode_2_horizon_line_width = 1
    mode_2_moon_line_color = (0, 255, 255)

    # Making class constants
    starting_road_line = Drawable()
    starting_road_line.y_ratio = 1/20
    starting_road_line.line_width = 2
    road_side_lines = Drawable()
    horizon_line = Drawable()
    horizon_line.y_ratio = 1/2
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

    # Making constants from other constants
    ask_mode_line_1 = f"Mode A = {mode_1_title}"
    ask_mode_line_2 = f"Mode B = {mode_2_title}"
    starting_road_line.y = starting_road_line.y_ratio * window_height
    starting_road_line.size_ratio = 1 - (starting_road_line.y_ratio / horizon_line.y_ratio)
    starting_road_line.size = starting_road_line.size_ratio * window_width
    road_side_lines.line_width = thin_line_width
    horizon_line.y = horizon_line.y_ratio * window_height
    horizon_line.color = light_line_color
    moon.x = moon.x_ratio * window_width
    moon.y = moon.y_ratio * window_height
    moon.size = moon.size_ratio * window_height
    dim_star.x = dim_star.x_ratio * window_width
    dim_star.y = dim_star.y_ratio * window_height
    dim_star.color = light_line_color
    star.x = star.x_ratio * window_width
    star.y = star.y_ratio * window_height
    star.color = light_line_color
    bright_star.x = bright_star.x_ratio * window_width
    bright_star.y = bright_star.y_ratio * window_width
    bright_star.color = light_line_color

    # Making variables
    mode_name = "Selecting Mode"
    road_line_hue_increment = None
    starting_road_line.color = None
    road_side_lines.color = None
    horizon_line.line_width = None
    moon.color = None

    # --- Selecting mode ---

    # Asking the user which mode they would want
    print(ask_mode_line_1)
    print(ask_mode_line_2)
    print(ask_mode_line_3)
    print(ask_mode_line_4)
    response = input(">> ")

    # Setting the mode to what they said and setting other variables respectively
    if response.lower() == "a":
        mode_name = mode_1_title
        road_line_hue_increment = 0
        starting_road_line.color = light_line_color
        road_side_lines.color = mode_1_road_side_line_color
        horizon_line.line_width = thin_line_width
        moon.color = light_line_color
    elif response.lower() == "b":
        mode_name = mode_2_title
        road_line_hue_increment = mode_2_road_line_hue_increment
        starting_road_line.color = mode_2_road_line_starting_color
        road_side_lines.color = light_line_color
        horizon_line.line_width = mode_2_horizon_line_width
        moon.color = mode_2_moon_line_color
    else:
        print(not_a_mode_line)
        quit()

    # --- Making window ---

    arcade.open_window(window_width, window_height, mode_name)
    arcade.set_background_color(background_color)

    # --- Rendering window ---

    arcade.start_render()

    # Drawing the road
    draw.road(starting_road_line, road_side_lines, horizon_line,
              window_width, window_width / 2, road_line_amount, road_line_frequency,
              0, road_line_width_decrease_ratio, road_line_hue_increment)

    # Drawing the moon
    draw.moon_outline(moon, curve_rendering)

    # Drawing the stars
    draw.star(dim_star)
    draw.star(star)
    draw.star(bright_star)

    arcade.finish_render()

    # --- Running until window closes ---

    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
