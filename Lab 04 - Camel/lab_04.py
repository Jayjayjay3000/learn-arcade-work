# Importing libraries
import random


def is_prime(number: int):
    if number >= 2:
        for divisor in range(2, number):
            if not (number % divisor):
                return False
    else:
        return False
    return True


def sum_digits(number: int):
    result = 0
    while number:
        result, number = result + number % 10, number // 10
    return result


def draw_card(hand_numbers: list, player_position: int):
    new_card_number = ((sum_digits(player_position) - 1) % 14) + 1
    hand_numbers.append(new_card_number)
    return hand_numbers


def get_hand_names(hand_numbers: list):
    card_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Joker"]
    hand_names = []
    for naming_number in range(len(hand_numbers)):
        hand_names.append(card_names[hand_numbers[naming_number] - 1])
    return hand_names


def draw_hand(card_amount: int):
    hand_numbers = []
    for drawing_number in range(card_amount):
        hand_numbers.append(random.randrange(1, 15))
    hand_names = get_hand_names(hand_numbers)
    return hand_numbers, hand_names


def upgrade_hand(hand_numbers: list, upgrade_amount: int):
    for upgrading_number in range(len(hand_numbers)):
        hand_numbers[upgrading_number] += upgrade_amount
        if hand_numbers[upgrading_number] > 14:
            hand_numbers[upgrading_number] = 14
    return hand_numbers


def use_card(using_card_number: int, player_position: int, magician_position: int, hand_numbers: list,
             jack_power: int, queen_power: int, double_king_power: int, joker_backfire: int,
             using_king: bool = False, using_joker: bool = False):
    if using_card_number < 11:
        player_position += using_card_number
        if using_card_number == 1:
            print(f"You warp {using_card_number} light-year forward.")
        else:
            print(f"You warp {using_card_number} light-years forward.")
    elif using_card_number == 11:
        magician_position -= jack_power
        player_position += 1
        print(f"You warp the magicians {jack_power} light-years backward!")
    elif using_card_number == 12:
        hand_numbers = upgrade_hand(hand_numbers, queen_power)
        print(f"All your cards' values increased by {queen_power}!")
    elif using_card_number == 13:
        if using_king:
            player_position += double_king_power
            print(f"You warp {double_king_power} light-years forward!!")
        else:
            print("You set your space ship into overdrive!!")
            player_position, magician_position, hand_numbers \
                = use_entire_hand(player_position, magician_position, hand_numbers,
                                  jack_power, queen_power, double_king_power, joker_backfire, True, using_joker)
    elif using_card_number == 14:
        if using_joker:
            player_position -= joker_backfire
            print(f"You warp {joker_backfire} light-years backward!")
        else:
            print("The engine starts glowing weird colors!")
            meta_using_card_number = random.randrange(1, 15)
            player_position, magician_position, hand_numbers \
                = use_card(meta_using_card_number, player_position, magician_position, hand_numbers,
                           jack_power, queen_power, double_king_power, joker_backfire, using_king, True)
    else:
        print("upon inserting the card into the engine,")
        print("the engine malfunctions and the ship blows up, killing you instantly.")
        print("The End")
        quit()

    return player_position, magician_position, hand_numbers


def use_entire_hand(player_position: int, magician_position: int, hand_numbers: list,
                    jack_power: int, queen_power: int, double_king_power: int, joker_backfire: int,
                    using_king: bool = True, using_joker: bool = False):
    for playing_number in range(len(hand_numbers)):
        using_card_number = hand_numbers[0]
        hand_numbers.pop(0)
        player_position, magician_position, hand_numbers \
            = use_card(using_card_number, player_position, magician_position, hand_numbers,
                       jack_power, queen_power, double_king_power, joker_backfire, using_king, using_joker)

    return player_position, magician_position, hand_numbers


# Defining main function
def main():
    # Making constants
    full_line = "-" * 75
    exposition_line_1 = "You have stolen a magical deck of cards."
    exposition_line_2 = "You are using the magical cards to power your warping space ship"
    exposition_line_3 = "so you can outrun (out-warp?) the furious space magicians you stole from."
    exposition_question = "Which card should you use first?"
    prompt_line_e = "E. Exit the game"
    input_line = ">> "
    not_a_card_line = "Input a letter from A to E in order to use a card."
    exit_line_1 = "Suddenly, a giant space kraken rips your space ship in two, killing you instantly."
    exit_line_2 = "The End"
    dead = False
    turn = 0
    player_position = 1
    magician_position = -20
    magician_velocity = 4
    card_amount = 4
    jack_push_back_power = 12
    queen_upgrade_power = 5
    double_king_power = 20
    joker_backfire = 3

    # Making constants from other constants
    hand_numbers, hand_names = draw_hand(card_amount)

    # Making variables
    using_card_number = None
    prompt_line_a = f"A. {hand_names[0]}"
    prompt_line_b = f"B. {hand_names[1]}"
    prompt_line_c = f"C. {hand_names[2]}"
    prompt_line_d = f"D. {hand_names[3]}"

    # Giving an exposition on what the heck's happening to the player
    print(full_line)
    print(exposition_line_1)
    print(exposition_line_2)
    print(exposition_line_3)
    print(full_line)
    print(exposition_question)

    # Start game
    while not dead:
        print()
        print(prompt_line_a)
        print(prompt_line_b)
        print(prompt_line_c)
        print(prompt_line_d)
        print(prompt_line_e)
        print()
        selection = input(input_line)
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
            print(exit_line_1)
            print(exit_line_2)
            quit()
        else:
            print(not_a_card_line)
            continue

        player_position, magician_position, hand_numbers \
            = use_card(using_card_number, player_position, magician_position, hand_numbers,
                       jack_push_back_power, queen_upgrade_power, double_king_power, joker_backfire)

        if turn % 4 == 0:
            magician_velocity += 1
        magician_position += magician_velocity
        if magician_position >= player_position:
            print()
            print("The magicians caught up!")
            print("They board your space ship and eject you into space, killing you instantly.")
            print("The End")
            print()
            print(f"Score = {player_position}")
            if player_position >= 200:
                print()
                print("You went over 200 light-years! Congratulations!")
            quit()

        turn += 1
        print(full_line)
        print(f"You're on light-year {player_position}, "
              f"with the magicians {player_position - magician_position} light-years behind.")

        if len(hand_numbers) == 0:
            hand_numbers, hand_names = draw_hand(card_amount)
            print("You draw a new hand.")
        else:
            hand_numbers = draw_card(hand_numbers, player_position)
            hand_names = get_hand_names(hand_numbers)
            if hand_numbers[-1] == 8:
                print(f"You draw an {hand_names[-1]}.")
            elif hand_numbers[-1] > 10:
                print(f"You draw a {hand_names[-1]}!")
            else:
                print(f"You draw a {hand_names[-1]}.")

        print("Which card should you use next?")
        prompt_line_a = f"A. {hand_names[0]}"
        prompt_line_b = f"B. {hand_names[1]}"
        prompt_line_c = f"C. {hand_names[2]}"
        prompt_line_d = f"D. {hand_names[3]}"


# Running main function
if __name__ == "__main__":
    main()
