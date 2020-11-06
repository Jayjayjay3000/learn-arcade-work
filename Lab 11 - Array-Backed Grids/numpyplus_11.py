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


def sum_list(list_to_sum: list):
    list_sum: float = 0
    for element in list_to_sum:
        list_sum += element
    return list_sum


def sum_meta_list(meta_list: list):
    meta_list_sum: float = 0
    for sub_list in meta_list:
        meta_list_sum += sum_list(sub_list)
    return meta_list_sum


def get_lateral_sub_list(meta_list: list, common_index_number: int):
    lateral_sub_list = []
    for sub_list in meta_list:
        lateral_sub_list.append(sub_list[common_index_number])
    return lateral_sub_list


def get_streaks_in_list(list_to_get_streaks: list, streak_item, streak_minimum: int = 3):
    streak_length = 0
    streak_lengths_list = []
    for element in list_to_get_streaks:
        if element == streak_item:
            streak_length += 1
        else:
            if streak_length >= streak_minimum:
                streak_lengths_list.append(streak_length)
            streak_length = 0
    if streak_length >= streak_minimum:
        streak_lengths_list.append(streak_length)
    return streak_lengths_list
