# Importing libraries
import arcade
import draw_shapes_05 as draw


class Window(draw.Window):
    def __init__(self, section_list: list):
        super().__init__(1200, 600, "Lab 05 - Loopy Lab", arcade.color.AIR_FORCE_BLUE)
        self.sections = section_list

    def on_draw(self):
        super().on_draw()
        # Drawing the outlines of the sections
        draw_section_outlines()

        # Drawing the sections
        for current_section in self.sections:
            current_section.draw()


class Section(draw.Able):
    def __init__(self, start_x: int = 0, start_y: int = 0,
                 pattern_id: int = 0, quadrant_id: int = 0, use_center_line: bool = True):
        super().__init__()
        self.x = start_x
        self.y = start_y
        self.pattern_id = pattern_id
        self.quadrant_id = quadrant_id
        self.use_center_line = use_center_line

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
    section_1 = Section()
    section_2 = Section(300, 0, 1)
    section_3 = Section(600, 0, 2)
    section_4 = Section(900, 0, 3)
    section_5 = Section(0, 300, 0, 4, False)
    section_6 = Section(300, 300, 0, 3)
    section_7 = Section(600, 300, 0, 2)
    section_8 = Section(900, 300, 0, 1)
    section_list = [section_1, section_2, section_3, section_4, section_5, section_6, section_7, section_8]

    # --- Making window ---

    window: object = Window(section_list)

    # --- Running until window closes ---

    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
