# Importing libraries
import arcade
import draw_shapes_05 as draw


# Defining classes
class Window(draw.Window):
    """
    Class for this lab's window.
    """
    def __init__(self):
        """
        Constructs the window and sets its background color.
        """
        super().__init__(1200, 600, "Lab 05 - Loopy Lab", arcade.color.AIR_FORCE_BLUE)

    def on_draw(self):
        """
        The window's on draw method.
        """
        # Starting to render the window.
        super().on_draw()

        # Drawing the objects in the drawables list.
        self.draw_drawables()

        # Drawing the outlines of the sections
        draw_section_outlines()


class Section(draw.Able):
    """
    Class for sections of this lab.
    """
    def __init__(self, start_x: int = 0, start_y: int = 0,
                 pattern_id: int = 0, quadrant_id: int = 0, use_center_line: bool = True):
        """
        Creates class attributes.

        :param start_x: x position of the lower left corner of the section.
        :param start_y: y position of the lower left corner of the section.
        :param pattern_id: number determining which pattern the section will use.
            0 = all white, 1 = white vertical stripes, 2 = white horizontal stripes, and 3 = white dots.
        :param quadrant_id: number determining which quadrant to have the ranges be in.
            0 = the whole section, 1 = the upper-right quadrant, 2 = the upper-left quadrant, etc.
        :param use_center_line: whether or not to include the central diagonal line.
            This is unimportant for quadrant_id = 0.
        """
        super().__init__()
        self.x: int = start_x
        self.y: int = start_y
        self.pattern_id: int = pattern_id
        self.quadrant_id: int = quadrant_id
        self.use_center_line: bool = use_center_line

    def get_use_white(self, row: int, column: int):
        """
        Determines whether or not to have the color of the square be white depending on the row, column, and pattern ID.

        :param row: row number the square is on.
        :param column: column number the square is on.
        :return: whether or not the color of the square should be white.
        """
        # Setting the default use white value
        use_white = None

        # Changing the use white value depending on the pattern ID
        if self.pattern_id == 0:
            use_white = True
        elif self.pattern_id == 1:
            use_white = not column % 2
        elif self.pattern_id == 2:
            use_white = not row % 2
        elif self.pattern_id == 3:
            use_white = not (row % 2 or column % 2)

        # Printing an error message if the pattern ID isn't compatible
        else:
            print("Not an available pattern ID")
            quit()

        # Returning the use white value
        return use_white

    def get_quadrant_range(self, row: int):
        """
        Determines the range of the row depending on the row's number, quadrant ID,
        and whether or not to include the central diagonal line.

        :param row: number of the row.
        :return: range of the row.
        """
        # Setting the default range values
        start_range, end_range = None, None

        # Changing the range values depending on quadrant ID
        if self.quadrant_id == 0 or self.quadrant_id == 2 or self.quadrant_id == 3:
            start_range = 0
            if self.quadrant_id == 2 or self.quadrant_id == 3:
                if self.quadrant_id == 2:
                    end_range = row
                elif self.quadrant_id == 3:
                    end_range = 29 - row

                # Changing the range values depending on whether or not to include the central diagonal line
                if self.use_center_line:
                    end_range += 1
        if self.quadrant_id == 0 or self.quadrant_id == 1 or self.quadrant_id == 4:
            end_range = 30
            if self.quadrant_id == 1 or self.quadrant_id == 4:
                if self.quadrant_id == 1:
                    start_range = 30 - row
                elif self.quadrant_id == 4:
                    start_range = row + 1

                # Changing the range values depending on whether or not to include the central diagonal line
                if self.use_center_line:
                    start_range -= 1

        # Printing an error message if the quadrant ID isn't compatible
        elif not (self.quadrant_id == 2 or self.quadrant_id == 3):
            print("Not an available quadrant ID")
            quit()

        # Returning the range values
        return start_range, end_range

    def draw(self):
        """
        Draws a section.
        """
        for row in range(30):
            # Setting where the next row of squares will start and end
            start_range, end_range = self.get_quadrant_range(row)

            # Drawing a row of squares
            for column in range(start_range, end_range):
                # Setting the x position of the square depending on the column the square is in,
                # as well as the starting x position
                current_x: int = column * 10 + self.x + 5

                # Setting the y position of the square depending on the row the square is in,
                # as well as the starting y position
                current_y: int = row * 10 + self.y + 5

                # Setting the color of the square depending on the row and column the square is in,
                # as well as the pattern ID
                if self.get_use_white(row, column):
                    color = arcade.color.WHITE
                else:
                    color = arcade.color.BLACK

                # Drawing the square
                draw.square_filled(current_x, current_y, 5, color)

    def on_draw(self):
        """
        This drawable's on draw method.
        """
        self.draw()


# Defining functions
def draw_section_outlines():
    """
    Draws all the section outlines.
    """
    for section_row in range(2):
        # Drawing a row of section outlines
        for section_column in range(4):
            # Drawing a section outline
            draw.square_outline(section_column * 300 + 150, section_row * 300 + 150, 300, arcade.color.BLACK)


# Defining main function
def main():
    """
    Main function of lab 5
    """
    # Making class constants for the sections
    section_1 = Section()
    section_2 = Section(300, 0, 1)
    section_3 = Section(600, 0, 2)
    section_4 = Section(900, 0, 3)
    section_5 = Section(0, 300, 0, 4, False)
    section_6 = Section(300, 300, 0, 3)
    section_7 = Section(600, 300, 0, 2)
    section_8 = Section(900, 300, 0, 1)

    # Making class constants for the window
    window: object = Window()
    window.drawables = [section_1, section_2, section_3, section_4, section_5, section_6, section_7, section_8]

    # Running the program until the window closes
    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
