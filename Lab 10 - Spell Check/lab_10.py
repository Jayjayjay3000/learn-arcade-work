# Importing libraries
import re

# Making constants
DICTIONARY_FILE_NAME: str = "dictionary.txt"
KEY_WORD = ""
IS_CASE_SENSITIVE: bool = False


# Defining functions
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def get_list_from_file(file_name):
    file = open(file_name)
    file_list: list = []

    for current_line in file:
        current_line: str = current_line.strip()
        file_list.append(current_line)

    file.close()

    return file_list


def linear_search_through_list(key, searching_list: list, case_insensitive: bool = False):
    if case_insensitive:
        for current_list_index in range(len(searching_list)):
            if searching_list[current_list_index].lower() == key.lower():
                return True, current_list_index
    else:
        for current_list_index in range(len(searching_list)):
            if searching_list[current_list_index] == key:
                return True, current_list_index
    return False, None


def binary_search_through_list(key, searching_list: list, case_insensitive: bool = False):
    lower_bound: int = 0
    upper_bound: int = len(searching_list) - 1
    if case_insensitive:
        while lower_bound <= upper_bound:
            current_list_index: int = (lower_bound + upper_bound) // 2
            if searching_list[current_list_index].lower() < key.lower():
                lower_bound = current_list_index + 1
            elif searching_list[current_list_index].lower() > key.lower():
                upper_bound = current_list_index - 1
            else:
                return True, current_list_index
    else:
        while lower_bound <= upper_bound:
            current_list_index: int = (lower_bound + upper_bound) // 2
            if searching_list[current_list_index] < key:
                lower_bound = current_list_index + 1
            elif searching_list[current_list_index] > key:
                upper_bound = current_list_index - 1
            else:
                return True, current_list_index
    return False, None


# Defining main function
def main():
    # Making variables
    dictionary_list: list = get_list_from_file(DICTIONARY_FILE_NAME)
    is_in_list, list_number = binary_search_through_list(KEY_WORD, dictionary_list, not IS_CASE_SENSITIVE)

    if is_in_list:
        print(f"{KEY_WORD} is a word.")
        print(f"It is the {list_number + 1}th word in the dictionary.")
    else:
        print(f"{KEY_WORD} is not a word.")


# Running main function
if __name__ == "__main__":
    main()

"""
I'd like to mention that according to the dictionary text file, "Huh" and "Yuck" are words, but "Hi" is not.

Also, "Abhor" is the 69th word in the text file.
"""
