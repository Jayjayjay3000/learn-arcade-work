# Importing libraries
import arcade


def draw_section_outlines():
    for section_row in range(2):
        for section_column in range(4):
            arcade.draw_rectangle_outline(section_column * 300 + 150, section_row * 300 + 150,
                                          300, 300, arcade.color.BLACK, 1)


def draw_section_1(start_x: int, start_y: int):
    for row in range(30):
        for column in range(30):
            x = column * 10 + start_x
            y = row * 10 + start_y
            color = arcade.color.WHITE
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_2(start_x: int, start_y: int):
    for row in range(30):
        for column in range(30):
            x = column * 10 + start_x
            y = row * 10 + start_y
            if not column % 2:
                color = arcade.color.WHITE
            else:
                color = arcade.color.BLACK
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_3(start_x: int, start_y: int):
    for row in range(30):
        for column in range(30):
            x = column * 10 + start_x
            y = row * 10 + start_y
            if not row % 2:
                color = arcade.color.WHITE
            else:
                color = arcade.color.BLACK
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_4(start_x: int, start_y: int):
    for row in range(30):
        for column in range(30):
            x = column * 10 + start_x
            y = row * 10 + start_y
            if not row % 2 and not column % 2:
                color = arcade.color.WHITE
            else:
                color = arcade.color.BLACK
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_5(start_x: int, start_y: int):
    for row in range(30):
        for column in range(row + 1, 30):
            x = column * 10 + start_x
            y = row * 10 + start_y
            color = arcade.color.WHITE
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_6(start_x: int, start_y: int):
    for row in range(30):
        for column in range(30 - row):
            x = column * 10 + start_x
            y = row * 10 + start_y
            color = arcade.color.WHITE
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_7(start_x: int, start_y: int):
    for row in range(30):
        for column in range(row + 1):
            x = column * 10 + start_x
            y = row * 10 + start_y
            color = arcade.color.WHITE
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_8(start_x: int, start_y: int):
    for row in range(30):
        for column in range(29 - row, 30):
            x = column * 10 + start_x
            y = row * 10 + start_y
            color = arcade.color.WHITE
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1(5, 5)
    draw_section_2(305, 5)
    draw_section_3(605, 5)
    draw_section_4(905, 5)
    draw_section_5(5, 305)
    draw_section_6(305, 305)
    draw_section_7(605, 305)
    draw_section_8(905, 305)

    arcade.finish_render()

    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
