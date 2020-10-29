# Importing libraries
import re
import text_10 as text

# Making constants
SEARCH_MODE_0_TITLE: str = "Selecting Search Mode"
SEARCH_MODE_1_TITLE: str = "Linear Search"
SEARCH_MODE_2_TITLE: str = "Binary Search"
ASK_SEARCH_MODE_LINE_3: str = "Which mode do you want to select?"
ASK_SEARCH_MODE_LINE_4: str = "(Type \"A\" or \"B\", otherwise it won't work)"
NOT_A_MODE_LINE: str = "See? I told you it wouldn't work."
DICTIONARY_FILE_NAME: str = "dictionary.txt"
ALICE_IN_WONDERLAND_FILE_NAME: str = "AliceInWonderLand200.txt"
IS_CASE_SENSITIVE: bool = False

# Making constants from other constants
ASK_SEARCH_MODE_LINE_1: str = f"Mode A = {SEARCH_MODE_1_TITLE}"
ASK_SEARCH_MODE_LINE_2: str = f"Mode B = {SEARCH_MODE_2_TITLE}"
ASK_SEARCH_MODE_LINES: list \
    = [ASK_SEARCH_MODE_LINE_1, ASK_SEARCH_MODE_LINE_2, ASK_SEARCH_MODE_LINE_3, ASK_SEARCH_MODE_LINE_4]


# Defining get text functions
def get_word_not_in_dictionary_line(word):
    """
    Gets the word not found in dictionary file text.

    :param word: word that was not in dictionary file.
    :return: line of text that says the word was unable to be found in the specified dictionary text file.
    """
    line = f"The word \"{word}\" is not in the dictionary file."
    return line


# Defining functions
def get_word_list_from_line(line):
    """
    Gets a list of all the words in a line.

    :param line: line you want to split into a list of words.
    :return: list of all words in the line.
    """
    word_list = re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
    return word_list


def get_line_list_from_file(file_name):
    """
    Gets a list of all the lines in a file.

    :param file_name: name of the file you want to split into a list of lines.
    :return: list of all lines in the file.
    """
    # Making a list for the file
    file_line_list: list = []

    # Opening the file
    file = open(file_name)

    # Appending to the file list all of the lines in said file
    for current_line in file:
        current_line: str = current_line.strip()
        file_line_list.append(current_line)

    # Closing the file
    file.close()

    # Returning the list of lines
    return file_line_list


def get_word_list_from_file(file_name):
    """
    Gets a list of all the words in a file.

    :param file_name: name of the file you want to split into a list of words.
    :return: list of all words in the file.
    """
    # Making a list for the file
    file_word_list: list = []

    # Opening the file
    file = open(file_name)

    # Appending to the file list all of the words in said file
    for current_line in file:
        line_word_list = get_word_list_from_line(current_line)
        for current_word in line_word_list:
            file_word_list.append(current_word)

    # Closing the file
    file.close()

    # Returning the list of words
    return file_word_list


def linear_search_through_list(key, searching_list: list, case_insensitive: bool = False):
    """
    Searches through a list one element at a time to find a specific item.

    :param key: item you are looking for.
    :param searching_list: list you are looking through.
    :param case_insensitive: whether the search is case insensitive or not.
    :return: whether the item is in the list or not, and if it is, the location of the item within the list.
    """
    # Checking whether to do have the search be case sensitive or not
    if case_insensitive:
        # Checking the entire list for the specified item
        for current_list_index in range(len(searching_list)):
            # Checking if the current list item is the specified item
            if searching_list[current_list_index].lower() == key.lower():
                # Returning that the item was found
                return True, current_list_index
    else:
        # Checking the entire list for the specified item
        for current_list_index in range(len(searching_list)):
            # Checking if the current list item is the specified item
            if searching_list[current_list_index] == key:
                # Returning that the item was found
                return True, current_list_index

    # Returning that the item was not found
    return False, None


def binary_search_through_list(key, searching_list: list, is_case_insensitive: bool = False):
    """
    Searches through a list by checking where it could be to find a specific item.

    :param key: item you are looking for.
    :param searching_list: list you are looking through.
    :param is_case_insensitive: whether the search is case insensitive or not.
    :return: whether the item is in the list or not, and if it is, the location of the item within the list.
    """
    # Making variables to prepare search
    lower_bound: int = 0
    upper_bound: int = len(searching_list) - 1

    # Checking whether to do have the search be case sensitive or not
    if is_case_insensitive:
        # Checking the entire list for the specified item
        while lower_bound <= upper_bound:
            # Setting current index variable according to where the item can be
            current_list_index: int = (lower_bound + upper_bound) // 2

            # Checking where the specified item is in relation to the current index
            if searching_list[current_list_index].lower() < key.lower():
                # Moving the lower bound higher
                lower_bound = current_list_index + 1
            elif searching_list[current_list_index].lower() > key.lower():
                # Moving the upper bound lower
                upper_bound = current_list_index - 1
            else:
                # Returning that the item was found
                return True, current_list_index
    else:
        # Checking the entire list for the specified item
        while lower_bound <= upper_bound:
            # Setting current index variable according to where the item can be
            current_list_index: int = (lower_bound + upper_bound) // 2

            # Checking where the specified item is in relation to the current index
            if searching_list[current_list_index] < key:
                # Moving the lower bound higher
                lower_bound = current_list_index + 1
            elif searching_list[current_list_index] > key:
                # Moving the upper bound lower
                upper_bound = current_list_index - 1
            else:
                # Returning that the item was found
                return True, current_list_index

    # Returning that the item was not found
    return False, None


# Defining main function
def main():
    """
    Main function of lab 10
    """
    # Making variables
    dictionary_list: list = get_line_list_from_file(DICTIONARY_FILE_NAME)
    alice_in_wonderland_word_list: list = get_word_list_from_file(ALICE_IN_WONDERLAND_FILE_NAME)

    # Asking the user which searching mode they would want
    text.print_lines(ASK_SEARCH_MODE_LINES)
    response: str = input(text.INPUT_LINE)

    # Searching for words not in the dictionary depending on what mode they requested
    if response.lower() == "a":
        # Do a linear search of words not in the dictionary
        for current_word in alice_in_wonderland_word_list:
            # Checking to see if the current word is in the dictionary
            if not linear_search_through_list(current_word, dictionary_list, not IS_CASE_SENSITIVE)[0]:
                # Printing that the current word is not in the dictionary
                print(get_word_not_in_dictionary_line(current_word))
    elif response.lower() == "b":
        # Do a binary search of words not in the dictionary
        for current_word in alice_in_wonderland_word_list:
            # Checking to see if the current word is in the dictionary
            if not binary_search_through_list(current_word, dictionary_list, not IS_CASE_SENSITIVE)[0]:
                # Printing that the current word is not in the dictionary
                print(get_word_not_in_dictionary_line(current_word))
    else:
        print(NOT_A_MODE_LINE)


# Running main function
if __name__ == "__main__":
    main()

"""
I'd like to mention that according to the dictionary text file, "Huh" and "Yuck" are words, but "Hi" is not.

Also, "Abhor" is the 69th word in the text file. Just thought you would like to know.
"""
