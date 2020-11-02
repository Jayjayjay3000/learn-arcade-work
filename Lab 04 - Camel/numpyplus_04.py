# Importing libraries
import numpy as np


# Defining functions
def is_prime(number: int):
    """
    Determines whether a number is prime or not.

    :param number: number you want to know whether it is prime or not.
    :return: whether or not the number is prime. Returns None if the number is less than 2.
    """
    if number > 2:
        for divisor in range(3, int(np.sqrt(number)) + 1, 2):
            if (number % divisor) == 0:
                return False
    elif number == 2:
        return True
    else:
        return None
    return True


def sum_digits(number: int, base: int = 10):
    """
    Calculates the sum of a number's digits.

    :param number: number you want to sum the digits of.
    :param base: base you want number to be in when summing digits.
    :return: sum of number's digits.
    """
    digit_sum: int = 0
    while number:
        digit_sum, number = digit_sum + number % base, number // base
    return digit_sum
