# Importing libraries
import arcade
import draw_shapes_05 as draw


# Defining functions
def get_use_white(row: int, column: int, pattern_id: int = 0):
    """
    Determines whether or not to have the color of the square be white depending on the row, column, and pattern ID.

    :param row: row number the square is on.
    :param column: column number the square is on.
    :param pattern_id: number determining which pattern the section will use.
        0 = all white, 1 = white vertical stripes, 2 = white horizontal stripes, and 3 = white dots.
    :return: whether or not the color of the square should be white.
    """
    # Setting the default use white value
    use_white = None

    # Changing the use white value depending on the pattern ID
    if pattern_id == 0:
        use_white = True
    elif pattern_id == 1:
        use_white = not column % 2
    elif pattern_id == 2:
        use_white = not row % 2
    elif pattern_id == 3:
        use_white = not (row % 2 or column % 2)

    # Printing an error message if the pattern ID isn't compatible
    else:
        print("Not an available pattern ID")
        quit()

    # Returning the use white value
    return use_white


def get_quadrant_range(row: int, quadrant_id: int = 0, use_center_line: bool = True):
    """
    Determines the range of the row depending on the row's number, quadrant ID,
    and whether or not to include the central diagonal line.

    :param row: number of the row.
    :param quadrant_id: number determining which quadrant to have the ranges be in.
        0 = the whole section, 1 = the upper-right quadrant, 2 = the upper-left quadrant, etc.
    :param use_center_line: whether or not to include the central diagonal line.
        This is unimportant for quadrant_id = 0.
    :return: range of the row.
    """
    # Setting the default range values
    start_range, end_range = None, None

    # Changing the range values depending on quadrant ID
    if quadrant_id == 0 or quadrant_id == 2 or quadrant_id == 3:
        start_range = 0
        if quadrant_id == 2:
            # Changing the range values depending on whether or not to include the central diagonal line
            if use_center_line:
                end_range = row + 1
            else:
                end_range = row
        elif quadrant_id == 3:
            # Changing the range values depending on whether or not to include the central diagonal line
            if use_center_line:
                end_range = 30 - row
            else:
                end_range = 29 - row
    if quadrant_id == 0 or quadrant_id == 1 or quadrant_id == 4:
        end_range = 30
        if quadrant_id == 1:
            # Changing the range values depending on whether or not to include the central diagonal line
            if use_center_line:
                start_range = 29 - row
            else:
                start_range = 30 - row
        elif quadrant_id == 4:
            # Changing the range values depending on whether or not to include the central diagonal line
            if use_center_line:
                start_range = row
            else:
                start_range = row + 1

    # Printing an error message if the quadrant ID isn't compatible
    elif not (quadrant_id == 2 or quadrant_id == 3):
        print("Not an available quadrant ID")
        quit()

    # Returning the range values
    return start_range, end_range


def draw_section_outlines():
    """
    Draws all the section outlines.
    """
    for section_row in range(2):
        # Drawing a row of section outlines
        for section_column in range(4):
            # Drawing a section outline
            draw.square_outline(section_column * 300 + 150, section_row * 300 + 150, 300, arcade.color.BLACK)


def draw_section(start_x: int, start_y: int, pattern_id: int = 0, quadrant_id: int = 0, use_center_line: bool = True):
    """
    Draws a section depending on the starting x and y, the pattern ID, the quadrant ID,
    and whether or not to include the central diagonal line.

    :param start_x: x position of the lower left corner of the section.
    :param start_y: y position of the lower left corner of the section.
    :param pattern_id: number determining which pattern the section will use.
        0 = all white, 1 = white vertical stripes, 2 = white horizontal stripes, and 3 = white dots.
    :param quadrant_id: number determining which quadrant to have the ranges be in.
        0 = the whole section, 1 = the upper-right quadrant, 2 = the upper-left quadrant, etc.
    :param use_center_line: whether or not to include the central diagonal line.
        This is unimportant for quadrant_id = 0.
    """
    for row in range(30):
        # Setting where the next row of squares will start and end
        start_range, end_range = get_quadrant_range(row, quadrant_id, use_center_line)

        # Drawing a row of squares
        for column in range(start_range, end_range):
            # Setting the x position of the square depending on the column the square is in,
            # as well as the starting x position
            x: int = column * 10 + start_x + 5

            # Setting the y position of the square depending on the row the square is in,
            # as well as the starting y position
            y: int = row * 10 + start_y + 5

            # Setting the color of the square depending on the row and column the square is in,
            # as well as the pattern ID
            if get_use_white(row, column, pattern_id):
                color = arcade.color.WHITE
            else:
                color = arcade.color.BLACK

            # Drawing the square
            draw.square_filled(x, y, 5, color)


# Defining main function
def main():
    """
    Main function of lab 5
    """

    # --- Making window ---

    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    # --- Rendering window ---

    arcade.start_render()

    # Drawing the outlines of the sections
    draw_section_outlines()

    # Drawing the sections
    draw_section(0, 0)
    draw_section(300, 0, 1)
    draw_section(600, 0, 2)
    draw_section(900, 0, 3)
    draw_section(0, 300, 0, 4, False)
    draw_section(300, 300, 0, 3, True)
    draw_section(600, 300, 0, 2, True)
    draw_section(900, 300, 0, 1, True)

    arcade.finish_render()

    # --- Running until window closes ---

    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
