"""
Line A: This line of code is rewritten from https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number,
    in the third example of the first answer in the page.
"""

# Importing libraries
from numpy import *
import random as r


# Defining functions
def is_prime(testing_number: int):
    """
    Determines whether a number is prime or not.

    :param testing_number: number you want to know whether it is prime or not.
    :return: whether or not the number is prime. Returns None if the number is less than 2.
    """
    # Returning none if the number is less than 2
    if testing_number < 2:
        return None

    # Checking if the number is odd or 2
    elif testing_number % 2 == 1 or testing_number == 2:
        # Looping through all odd divisors greater than 1 and less than the number's square root
        for current_divisor in range(3, int(sqrt(testing_number)) + 1, 2):
            # Checking if the number is divisible by the current divisor
            if (testing_number % current_divisor) == 0:
                break

        # Returning true if there is no divisor the number is divisible by
        else:
            return True

    # Returning false
    return False


def distance_of_two_points(point_a: tuple, point_b: tuple):
    x_difference: float = point_b[0] - point_a[0]
    y_difference: float = point_b[1] - point_a[1]
    distance: float = sqrt(x_difference ** 2 + y_difference ** 2)
    return distance


def greater_than_or_randomly_equal_to(a: float, b: float):
    if a > b:
        return True
    elif a < b:
        return False
    elif r.randrange(0, 2) == 0:
        return True
    else:
        return False


def less_than_or_randomly_equal_to(a: float, b: float):
    if a < b:
        return True
    elif a > b:
        return False
    elif r.randrange(0, 2) == 0:
        return True
    else:
        return False


def sum_digits(summing_number: int, base: int = 10):
    """
    Calculates the sum of a number's digits.

    :param summing_number: number you want to sum the digits of.
    :param base: base you want number to be in when summing digits.
    :return: sum of number's digits.
    """
    # Making digit sum variable to prepare for summing the number's digits
    digit_sum: int = 0

    # Summing the number's digits
    while summing_number:
        # Adding a digit to the digit sum
        digit_sum, summing_number = digit_sum + summing_number % base, summing_number // base  # *** A ***

    # Returning the digit sum
    return digit_sum


def random_element_from_list(list_to_get_element: list):
    random_index = r.randrange(0, len(list_to_get_element))
    random_element = list_to_get_element[random_index]
    return random_element


def linear_search_through_list(key_element, searching_list: list):
    """
    Searches through a list one element at a time to find a specific item.

    :param key_element: item you are looking for.
    :param searching_list: list you are looking through.
    :return: whether the item is in the list or not, and if it is, the location of the item within the list.
    """
    # Checking the entire list for the specified item
    for current_list_index in range(len(searching_list)):
        # Checking if the current list item is the specified item
        if searching_list[current_list_index] == key_element:
            # Returning that the item was found
            return True, current_list_index

    # Returning that the item was not found
    return False, None


def sort_list(list_to_sort: list):
    """


    :param list_to_sort:
    :return:
    """
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_index in range(1, len(list_to_sort)):

        # Get the value of the element to insert
        key_element = list_to_sort[key_index]

        # Scan from right to the left (start of list)
        scanning_index = key_index - 1

        # Loop each element, moving them up until
        # we reach the position the
        while scanning_index >= 0 and greater_than_or_randomly_equal_to(list_to_sort[scanning_index], key_element):
            list_to_sort[scanning_index + 1] = list_to_sort[scanning_index]
            scanning_index = scanning_index - 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        list_to_sort[scanning_index + 1] = key_element

    return list_to_sort


def sort_meta_list_by_element_of_sub_list(meta_list: list, key_sub_index: int = 0):
    """


    :param key_sub_index:
    :param meta_list:
    :return:
    """
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_index in range(1, len(meta_list)):

        # Get the value of the element to insert
        key_sub_list = meta_list[key_index]
        key_sub_element = key_sub_list[key_sub_index]

        # Scan from right to the left (start of list)
        scanning_index = key_index - 1

        # Loop each element, moving them up until
        # we reach the position the
        while scanning_index >= 0 \
                and greater_than_or_randomly_equal_to(meta_list[scanning_index][key_sub_index], key_sub_element):
            meta_list[scanning_index + 1] = meta_list[scanning_index]
            scanning_index = scanning_index - 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        meta_list[scanning_index + 1] = key_sub_list

    return meta_list


def sum_list(list_to_sum: list):
    """
    Calculates the sum of a list of numbers.

    :param list_to_sum: list you want to sum the elements of.
    :return: sum of the list of numbers.
    """
    # Making list sum variable to prepare for summing the list's elements
    list_sum: float = 0

    # Summing the elements of the list
    for element in list_to_sum:
        # Adding an element to the list sum
        list_sum += element

    # Returning the list sum
    return list_sum


def sum_meta_list(meta_list: list):
    """
    Calculates the sum of a list of lists of numbers.

    :param meta_list: list of lists you want to sum the sub-elements of.
    :return: sum of the list of lists of numbers.
    """
    # Making meta-list sum variable to prepare for summing the meta-list's elements
    meta_list_sum: float = 0

    # Summing the sub-elements of the meta-list
    for sub_list in meta_list:
        # Adding a sub-list sum to the meta-list sum
        meta_list_sum += sum_list(sub_list)

    # Returning the meta-list sum
    return meta_list_sum


def get_lateral_sub_list(meta_list: list, common_index_number: int):
    """
    Makes a list that contains every element of a specified index number in a list of lists.

    :param meta_list: list of lists you want to make a lateral sub-list of.
    :param common_index_number: common index number every element of the lateral sub-list is from.
    :return: lateral sub-list of the list of lists.
    """
    # Making lateral sub-list variable
    lateral_sub_list = []

    # Putting elements in the lateral sub-list
    for sub_list in meta_list:
        # Putting an element in the lateral sub-list
        lateral_sub_list.append(sub_list[common_index_number])

    # Returning the lateral sub-list
    return lateral_sub_list


def get_streaks_in_list(list_to_get_streaks: list, streak_item, streak_minimum: int = 1):
    """
    Makes a list containing streak lengths of a specific item in a list.

    :param list_to_get_streaks: list you want to make a list containing item streak lengths of.
    :param streak_item: specific item you want to find streaks of.
    :param streak_minimum: minimum length a streak can be.
    :return: list containing streak lengths of a specific item in a list.
    """
    # Making variables to prepare for
    streak_length = 0
    streak_lengths_list = []

    # Calculating streak lengths and appending them to the streak length list
    for element in list_to_get_streaks + [None]:
        # Checking if the element is a part of a streak
        if element == streak_item:
            streak_length += 1
        else:
            # Appending the streak length to the streak length list if it's at least the minimum length
            if streak_length >= streak_minimum:
                streak_lengths_list.append(streak_length)

            # Resetting the streak length to 0
            streak_length = 0

    # Returning the streak length list
    return streak_lengths_list
