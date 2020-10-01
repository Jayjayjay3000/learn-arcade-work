# Making constants
INPUT_LINE = ">> "


# Defining functions
def print_lines(lines: list):
    """
    Prints a list of strings rather than a single string.

    :param lines: list of lines to print.
    """
    for current_line in range(len(lines)):
        print(lines[current_line])
