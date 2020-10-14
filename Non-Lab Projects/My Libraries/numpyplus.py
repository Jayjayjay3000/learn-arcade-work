# Defining functions
def is_prime(number: int):
    if number >= 2:
        for divisor in range(2, number):
            if not (number % divisor):
                return False
    else:
        return False
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
