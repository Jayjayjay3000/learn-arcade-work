# Importing libraries
import random
import numpyplus_04 as npp
import text_04 as text

# Making constants
FULL_LINE_SIZE: int = 75
EXPOSITION_LINE_1: str = "You have stolen a magical deck of cards."
EXPOSITION_LINE_2: str = "You are using the magical cards to power your warping space ship"
EXPOSITION_LINE_3: str = "so you can outrun (out-warp?) the furious space magicians you stole from."
PLAYER_STARTING_POSITION: int = 1
HAND_SIZE: int = 4
CARD_NAMES: list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Joker"]
USE_WHICH_CARD_FIRST_LINE: str = "Which card should you use first?"
USE_WHICH_CARD_LINE: str = "Which card should you use next?"
PROMPT_LINE_E: str = "E. Exit the game"
NOT_AN_OPTION_LINE: str = "Input a letter from A to E in order to use a card."
EXIT_LINE: str = "Suddenly, a giant space kraken rips your space ship in two, killing you instantly."
HIGHEST_NUMBER_CARD_NUMBER: int = 10
JACK_NUMBER: int = 11
JACK_PUSH_BACK_POWER: int = 12
QUEEN_NUMBER: int = 12
QUEEN_UPGRADE_POWER: int = 5
KING_NUMBER: int = 13
KING_USED_LINE: str = "You set your space ship into overdrive!!"
DOUBLE_KING_POWER: int = 20
JOKER_NUMBER: int = 14
JOKER_USED_LINE: str = "The engine starts glowing weird colors!"
DOUBLE_JOKER_BACKFIRE: int = 3
NOT_A_CARD_LINE_1: str = "upon inserting the card into the engine,"
NOT_A_CARD_LINE_2: str = "the engine malfunctions and the ship blows up, killing you instantly."
DRAWING_HAND_LINE: str = "You draw a new hand."
MAGICIAN_STARTING_POSITION: int = -20
MAGICIAN_STARTING_VELOCITY: int = 4
MAGICIAN_VELOCITY_INCREASE_FREQUENCY: int = 4
GAME_OVER_LINE_1: str = "The magicians caught up!"
GAME_OVER_LINE_2: str = "They board your space ship and eject you into space, killing you instantly."
CONGRATULATIONS_SCORE: int = 200

# Making constants from other constants
JACK_USED_LINE: str = f"You warp the magicians {JACK_PUSH_BACK_POWER} light-years backward!"
QUEEN_USED_LINE: str = f"All your cards' values increased by {QUEEN_UPGRADE_POWER}!"
DOUBLE_KING_USED_LINE: str = f"You warp {DOUBLE_KING_POWER} light-years forward!!"
DOUBLE_JOKER_USED_LINE: str = f"You warp {DOUBLE_JOKER_BACKFIRE} light-years backward!"
CONGRATULATIONS_SCORE_LINE: str = f"You went over {CONGRATULATIONS_SCORE} light-years! Congratulations!"
EXPOSITION_LINES: list = [EXPOSITION_LINE_1, EXPOSITION_LINE_2, EXPOSITION_LINE_3]
EXIT_LINES: list = [EXIT_LINE, text.THE_END_LINE]
NOT_A_CARD_LINES: list = [NOT_A_CARD_LINE_1, NOT_A_CARD_LINE_2, text.THE_END_LINE]
GAME_OVER_LINES: list = [GAME_OVER_LINE_1, GAME_OVER_LINE_2, text.THE_END_LINE]


# Defining get text functions
def get_turn_info_line(player_position: int, magician_position: int):
    """
    Gets the beginning of turn information text.

    :param player_position: position of player in light-years.
    :param magician_position: position of magicians in light-years.
    :return: line of text that says the position of the player and the distance between the player and the magicians.
    """
    line = f"You're on light-year {player_position}, " \
           f"with the magicians {player_position - magician_position} light-years behind."
    return line


def get_prompt_lines(hand_names: list):
    """
    Gets the "pick a card to use" prompt text.

    :param hand_names: names of the cards in your hand.
    :return: lines of text that say the various options you have during "pick a card to use" prompt.
    """
    line_a: str = f"A. {hand_names[0]}"
    line_b: str = f"B. {hand_names[1]}"
    line_c: str = f"C. {hand_names[2]}"
    line_d: str = f"D. {hand_names[3]}"
    lines = [line_a, line_b, line_c, line_d, PROMPT_LINE_E]
    return lines


def get_number_card_used_line(card_number: int):
    """
    Gets the number card used text.

    :param card_number: value of card you just used.
    :return: line of text that says how many light-years the number card you used moved you forward.
    """
    if card_number == 1:
        line = f"You warp {card_number} light-year forward."
    else:
        line = f"You warp {card_number} light-years forward."
    return line


def get_drawing_card_line(card_number: int, card_name: str):
    """
    Gets the card drawn text.

    :param card_number: value of card you drew.
    :param card_name: name of card you drew.
    :return: line of text that says what card you have drawn.
    """
    if card_number == 8:
        line = f"You draw an {card_name}."
    elif card_number > HIGHEST_NUMBER_CARD_NUMBER:
        line = f"You draw a {card_name}!"
    else:
        line = f"You draw a {card_name}."
    return line


def get_score_line(player_position: int):
    """
    Gets the game over score text.

    :param player_position: position of player in light-years.
    :return: line of text that says the score you got.
    """
    line = f"Score = {player_position}"
    return line


# Defining other functions
def draw_card(hand_numbers: list, player_position: int):
    """
    Adds a new card to your hand, depending on the position of the player.

    :param hand_numbers: old values of the cards in your hand.
    :param player_position: position of player in light-years.
    :return: new values for the cards in your hand, including card drawn.
    """
    # Setting the drawn card's value
    new_card_number: int = ((npp.sum_digits(player_position) - 1) % len(CARD_NAMES)) + 1

    # Adding the card value to the hand values
    hand_numbers.append(new_card_number)

    # Returning the new hand values
    return hand_numbers


def draw_hand():
    """
    Replaces your hand with randomly selected new cards.

    :return: values of the cards in your new hand.
    """
    # Making a new hand
    hand_numbers: list = []

    # Adding random card values to said hand until it's full
    for drawing_number in range(HAND_SIZE):
        hand_numbers.append(random.randrange(1, len(CARD_NAMES) + 1))

    # Returning the new hand values
    return hand_numbers


def get_hand_names(hand_numbers: list):
    """
    Makes new names for the cards in your hand based on their values.

    :param hand_numbers: values of the cards in your hand.
    :return: new names for the cards in your hand.
    """
    # Making an empty list of hand names
    hand_names: list = []

    # Adding card names corresponding to their respective values to said list of hand names
    for naming_number in range(len(hand_numbers)):
        hand_names.append(CARD_NAMES[hand_numbers[naming_number] - 1])

    # Returning the new hand names
    return hand_names


def upgrade_hand(hand_numbers: list, upgrade_amount: int):
    """
    Increases the value of each of the cards in your hand.

    :param hand_numbers: old values of the cards in your hand.
    :param upgrade_amount: amount each card value will get increased.
    :return: new, increased values of the cards in your hand.
    """
    # Increasing each of the card values in the hand
    for upgrading_number in range(len(hand_numbers)):
        # Increasing the current card's value
        hand_numbers[upgrading_number] += upgrade_amount

        # Keeping the current card's value from being bigger than the highest valued card possible
        if hand_numbers[upgrading_number] > len(CARD_NAMES):
            hand_numbers[upgrading_number]: int = len(CARD_NAMES)

    # Returning the new hand values
    return hand_numbers


def use_card(using_card_number: int, player_position: int, magician_position: int, hand_numbers: list,
             using_king: bool = False, using_joker: bool = False):
    """
    Gets the results of using a card.

    :param using_card_number: value of the currently used card.
    :param player_position: old position of player in light-years.
    :param magician_position: old position of magicians in light-years.
    :param hand_numbers: old values of the cards in your hand.
    :param using_king: whether or not this card being used is the byproduct of a king.
    :param using_joker: whether or not this card being used is the byproduct of a joker.
    :return: new positions for the player and magicians, as well as new values for the cards in your hand.
    """
    # Checking if the card is a number card
    if using_card_number <= HIGHEST_NUMBER_CARD_NUMBER:
        player_position += using_card_number
        print(get_number_card_used_line(using_card_number))

    # Checking if the card is a jack
    elif using_card_number == JACK_NUMBER:
        magician_position -= JACK_PUSH_BACK_POWER
        player_position += 1
        print(JACK_USED_LINE)

    # Checking if the card is a queen
    elif using_card_number == QUEEN_NUMBER:
        hand_numbers: list = upgrade_hand(hand_numbers, QUEEN_UPGRADE_POWER)
        print(QUEEN_USED_LINE)

    # Checking if the card is a king
    elif using_card_number == KING_NUMBER:
        # Checking if a king is already being used
        if using_king:
            player_position += DOUBLE_KING_POWER
            print(DOUBLE_KING_USED_LINE)
        else:
            print(KING_USED_LINE)
            player_position, magician_position, hand_numbers \
                = use_entire_hand(player_position, magician_position, hand_numbers, True, using_joker)

    # Checking if the card is a joker
    elif using_card_number == JOKER_NUMBER:
        # Checking if a joker is already being used
        if using_joker:
            player_position -= DOUBLE_JOKER_BACKFIRE
            print(DOUBLE_JOKER_USED_LINE)
        else:
            print(JOKER_USED_LINE)
            meta_using_card_number: int = random.randrange(1, len(CARD_NAMES) + 1)
            player_position, magician_position, hand_numbers \
                = use_card(meta_using_card_number, player_position, magician_position, hand_numbers, using_king, True)

    # Stopping the program for not having a viable card
    else:
        text.print_lines(NOT_A_CARD_LINES)
        quit()

    # Returning the new player and magician positions, as well as the new hand values
    return player_position, magician_position, hand_numbers


def use_entire_hand(player_position: int, magician_position: int, hand_numbers: list,
                    using_king: bool = True, using_joker: bool = False):
    """
    Goes through every card in your hand and uses it.

    :param player_position: old position of player in light-years.
    :param magician_position: old position of magicians in light-years.
    :param hand_numbers: old values of the cards in your hand.
    :param using_king: whether or not these card being used is the byproduct of a king.
    :param using_joker: whether or not these card being used is the byproduct of a joker.
    :return: new positions for the player and magicians, as well as a new value of empty for the cards in your hand.
    """
    # Going through every card in the hand and using it
    for playing_number in range(len(hand_numbers)):
        # Storing the current card's value
        using_card_number: int = hand_numbers[0]

        # Removing the current card from the hand
        hand_numbers.pop(0)

        # Using the current card
        player_position, magician_position, hand_numbers \
            = use_card(using_card_number, player_position, magician_position, hand_numbers, using_king, using_joker)

    # Returning the new player and magician positions, as well as the new hand values
    return player_position, magician_position, hand_numbers


# Defining main function
def main():
    """
    Main function of lab 4
    """
    # Making variables
    turn: int = 0
    player_position: int = PLAYER_STARTING_POSITION
    using_card_number = None
    hand_numbers: list = draw_hand()
    hand_names: list = get_hand_names(hand_numbers)
    magician_position: int = MAGICIAN_STARTING_POSITION
    magician_velocity: int = MAGICIAN_STARTING_VELOCITY
    prompt_lines: list = get_prompt_lines(hand_names)

    # Giving an exposition on what the heck's happening to the player
    text.print_full_line(FULL_LINE_SIZE)
    text.print_lines(EXPOSITION_LINES)
    text.print_full_line(FULL_LINE_SIZE)
    print(USE_WHICH_CARD_FIRST_LINE)

    # Starting the game
    while True:
        # Asking player what card to use
        print()
        text.print_lines(prompt_lines)
        print()
        selection: str = input(text.INPUT_LINE)

        # Storing and removing the chosen card's value from the hand
        print()
        if selection.lower() == "a":
            using_card_number = hand_numbers[0]
            hand_numbers.pop(0)
        elif selection.lower() == "b":
            using_card_number = hand_numbers[1]
            hand_numbers.pop(1)
        elif selection.lower() == "c":
            using_card_number = hand_numbers[2]
            hand_numbers.pop(2)
        elif selection.lower() == "d":
            using_card_number = hand_numbers[3]
            hand_numbers.pop(3)
        elif selection.lower() == "e":
            text.print_lines(EXIT_LINES)
            quit()
        else:
            print(NOT_AN_OPTION_LINE)
            continue

        # Using the chosen card
        player_position, magician_position, hand_numbers \
            = use_card(using_card_number, player_position, magician_position, hand_numbers)

        # Moving the magicians forward
        if turn % MAGICIAN_VELOCITY_INCREASE_FREQUENCY == 0:
            magician_velocity += 1
        magician_position += magician_velocity

        # Checking if the magicians have caught up to the player
        if magician_position >= player_position:
            print()
            text.print_lines(GAME_OVER_LINES)
            print()
            print(get_score_line(player_position))
            if player_position >= CONGRATULATIONS_SCORE:
                print()
                print(CONGRATULATIONS_SCORE_LINE)
            quit()

        # Starting a new turn
        turn += 1
        text.print_full_line(FULL_LINE_SIZE)

        # Printing information about the player and the magicians
        print(get_turn_info_line(player_position, magician_position))

        # Drawing cards to get back to the original amount
        if not hand_numbers:
            hand_numbers = draw_hand()
            hand_names: list = get_hand_names(hand_numbers)
            print(DRAWING_HAND_LINE)
        else:
            hand_numbers: list = draw_card(hand_numbers, player_position)
            hand_names: list = get_hand_names(hand_numbers)
            print(get_drawing_card_line(hand_numbers[-1], hand_names[-1]))

        # Changing variable to prepare for the next prompt
        print()
        prompt_lines: list = get_prompt_lines(hand_names)


# Running main function
if __name__ == "__main__":
    main()
