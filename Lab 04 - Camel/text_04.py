# Making constants
INPUT_LINE = ">> "
THE_END_LINE = "The End"


# Defining functions
def print_lines(lines: list):
    """
    Prints a list of strings rather than a single string.

    :param lines: list of lines to print.
    """
    for current_line in range(len(lines)):
        print(lines[current_line])


def print_full_line(size: int):
    """
    Prints a line

    :param size: length of the line
    """
    line: str = "-" * size
    print(line)
