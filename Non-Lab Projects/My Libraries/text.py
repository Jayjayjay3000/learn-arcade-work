# Importing libraries
import time

# Making constants
INPUT_LINE = ">> "
THE_END_LINE = "The End"


# Defining functions
def print_lines(lines: list):
    """
    Prints a list of strings rather than a single string.

    :param lines: list of lines to print.
    """
    for current_line in lines:
        # Printing the current line
        print(current_line)


def input_with_prompt(prompt: str):
    print(prompt)
    response: str = input(INPUT_LINE)
    return response


def print_slow(line: str, print_time: float, ends_with_return: bool = True):
    """
    Prints a string over a given time.

    :param line: line to print.
    :param print_time: time it will take to print the line.
    :param ends_with_return: whether the line will end in a return or not.
    """
    # Printing the string over time
    for character in line:
        # Printing the current character
        print(character, end="")

        # Waiting to print the next character
        time.sleep(print_time / len(line))

    # Checking if line should end with return
    if ends_with_return:
        print()


def print_slow_ellipsis(print_time: float = 3, length: int = 3, ends_with_return: bool = True):
    """
    Prints an ellipsis over a given time.

    :param print_time:
    :param length:
    :param ends_with_return:
    """
    ellipsis_line: str = "." * length
    print_slow(ellipsis_line, print_time, ends_with_return)


def print_full_line(length: int):
    """
    Prints a line

    :param length: length of the line
    """
    line: str = "-" * length
    print(line)


def get_amount_of_spaces(line: str):
    amount = 0
    for character in line:
        if character.isspace():
            amount += 1
    return amount
