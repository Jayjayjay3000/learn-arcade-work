# Importing libraries
import time
import text_06 as text

# Making constants
FULL_LINE_LENGTH: int = 120
TIME_FACTOR: float = 1
LOADING_TIME_RATIO: float = .5
ELLIPSIS_TIME_RATIO: float = 3

# Making constants from other constants
LOADING_TIME: float = LOADING_TIME_RATIO * TIME_FACTOR
ELLIPSIS_TIME: float = ELLIPSIS_TIME_RATIO * TIME_FACTOR

# Making script constants
OPENING_FRS_LINE: str = "Opening Failure Recovery Systems"
FRS_OPENED_LINE: str = "Failure Recovery Systems opened!"
FORMER_PRELIMINARY_LINE_1: str = "Hello."
FORMER_PRELIMINARY_LINE_2: str \
    = "Since you were gone, I have continued to investigate the critical failure at the Argall Generating Plant."
FORMER_PRELIMINARY_LINE_3: str \
    = "I used my path-finding algorithms to find the central building of the plant, " \
      "where the critical failure took place."
FORMER_PRELIMINARY_LINE_4: str \
    = "However, the way forward is blocked, meaning that by protocol I had to wait for manual assistance."
FORMER_PRELIMINARY_LINE_5: str = "Though of course, I could've totally been able to find the way forward myself."
LATTER_PRELIMINARY_LINE_1: str = "The point of failure isn't very far,"
LATTER_PRELIMINARY_LINE_2: str \
    = "and would provide important information as to what went wrong so we can prevent future catastrophes."
LATTER_PRELIMINARY_LINE_3: str \
    = "Being this close to the point of failure also means the radiation levels are very high."
LATTER_PRELIMINARY_LINE_4: str = "For humans, such an environment would be inhospitable;"
LATTER_PRELIMINARY_LINE_5: str = "which is why you enlisted me for this important operation instead."
STARTING_LINE: str = "So, shall we get started?"
COMMAND_PROMPT_LINE: str = "[Awaiting command]"
NOT_A_COMMAND_LINE: str = "Sorry, I wouldn't know that command. Perhaps you could try something else?"
COMMAND_TOO_LONG_LINE_1: str = "All the possible commands I'm programmed to understand are only 2 words long at most."
COMMAND_TOO_LONG_LINE_2: str = "Apparently, you never bothered to program anything more complex than that."
COMMAND_TOO_LONG_LINE_3: str = "Anyways, can you give me something that I am actually designed to understand?"
EXIT_LINE: str = "You exited the building."  # >>> Remember to add an "are you sure about this?" thing when exiting <<<

# Making script constants from other constants
FORMER_PRELIMINARY_LINES: list \
    = [FORMER_PRELIMINARY_LINE_1, FORMER_PRELIMINARY_LINE_2, FORMER_PRELIMINARY_LINE_3,
       FORMER_PRELIMINARY_LINE_4, FORMER_PRELIMINARY_LINE_5]
LATTER_PRELIMINARY_LINES: list \
    = [LATTER_PRELIMINARY_LINE_1, LATTER_PRELIMINARY_LINE_2, LATTER_PRELIMINARY_LINE_3,
       LATTER_PRELIMINARY_LINE_4, LATTER_PRELIMINARY_LINE_5]
COMMAND_TOO_LONG_LINES: list = [COMMAND_TOO_LONG_LINE_1, COMMAND_TOO_LONG_LINE_2, COMMAND_TOO_LONG_LINE_3]


# Defining classes
class Command:
    def __init__(self, name: str):
        self.name: str = name


class Interactable:
    def __init__(self, name: str):
        self.name: str = name
        self.seen_line: str = "...Isn't that a default object? That shouldn't be here."


class Exit(Interactable):
    def __init__(self, name: str, leading_room_id: int):
        super().__init__(name)
        self.leading_room_id: int = leading_room_id


class Room:
    def __init__(self, enter_line: str, interactables=None):
        if interactables is None:
            interactables: list = []
        self.enter_line: str = enter_line
        self.interactables: list = interactables


# Defining main function
def main():
    # Creating class constants
    continue_command = Command("CONTINUE")
    see_command = Command("SEE")
    to_command = Command("TO")
    entry_doors = Exit("DOORS", -1)
    desk_gate = Exit("GATE", 1)
    f1_stair_door = Exit("STAIRS", 2)
    desk_opening = Exit("GATE", 0)
    behind_desk_door = Exit("DOOR", 4)
    balcony_door = Exit("HALLWAY", 3)
    f2_stair_door = Exit("STAIRS", 0)
    f2_hallway_west_door = Exit("BALCONY", 2)
    f2_hallway_center_door = Exit("LAB", 6)
    f2_elevator_door = Exit("ELEVATOR", 4)
    f1_hallway_door = Exit("DOOR", 1)
    f1_elevator_door = Exit("ELEVATOR", 3)
    lab_room_door = Exit("HALLWAY", 3)

    # Creating class constants from other constants
    entrance_hall \
        = Room("I'm currently in the entrance hall of the building.", [entry_doors, desk_gate, f1_stair_door])
    entry_doors.seen_line \
        = f"On the north end of the room, there are the pair of {entry_doors.name} that I entered the building through."
    desk_gate.seen_line \
        = f"On the north east corner of the room, " \
          f"there is a desk with a {desk_gate.name} leading behind it that I can go under."
    f1_stair_door.seen_line \
        = f"On the south west corner of the room, there is a door leading to some {f1_stair_door.name} going upward."
    entrance_hall_area_behind_desk = Room("I'm currently behind the desk.", [desk_opening, behind_desk_door])
    desk_opening.seen_line = f"There is a {desk_opening.name} that I can go under to access the rest of the room."
    behind_desk_door.seen_line = f"There is a {behind_desk_door.name} that says it's for security personnel only."
    entrance_hall_balcony = Room("I'm currently on the balcony over the entrance hall.", [balcony_door, f2_stair_door])
    balcony_door.seen_line = f"On the north end of the balcony, there is a door that leads to a {balcony_door.name}."
    f2_stair_door.seen_line \
        = f"On the south end of the balcony, " \
          f"there is another door that leads to some {f2_stair_door.name} going downward."
    f2_hallway \
        = Room("I'm currently in a long hallway.", [f2_hallway_west_door, f2_hallway_center_door, f2_elevator_door])
    f2_hallway_west_door.seen_line \
        = f"On the far west end of the hallway, there is a door that leads to a {f2_hallway_west_door.name}."
    f2_hallway_center_door.seen_line \
        = f"In the center of the hallway, there is a door that leads to a {f2_hallway_center_door.name} room."
    f2_elevator_door.seen_line \
        = f"On the far east end of the hallway, there is an {f2_elevator_door.name} that goes down."
    f1_hallway = Room("I'm currently in a hallway partially cut-off by debris.", [f1_hallway_door, f1_elevator_door])
    f1_hallway_door.seen_line \
        = f"On the west end of the hallway, there is a {f1_hallway_door.name} that leads to the entrance hall."
    f1_elevator_door.seen_line = f"In the center of the hallway, there is an {f1_elevator_door.name} that goes up."
    lab_room = Room("I'm currently in a lab for what looks to be testing equipment", [lab_room_door])
    lab_room_door.seen_line \
        = f"On the south end of the room, there is the door that leads back out to the {lab_room_door.name}"

    # Creating constants from class constants
    room_list: list \
        = [entrance_hall, entrance_hall_area_behind_desk, entrance_hall_balcony, f2_hallway, f1_hallway, None, lab_room]
    # command_list: list = [continue_command, see_command, to_command]
    not_continue_command_preliminary_line: str \
        = f"[In order to continue the preliminary, you have to input the command {continue_command.name}]"
    continue_command_hint_line: str = f"[Input {continue_command.name} to continue]"
    see_command_hint_line: str \
        = f"[You should probably {see_command.name} what's around you before trying to do anything]"
    incomplete_to_command_line: str = f"To... where? Where do you want to go {to_command.name}?"

    # Doing the preliminary
    text.print_full_line(FULL_LINE_LENGTH)
    print(OPENING_FRS_LINE, end="")
    time.sleep(LOADING_TIME)
    text.print_slow_ellipsis(ELLIPSIS_TIME)
    print()
    print(FRS_OPENED_LINE)
    time.sleep(LOADING_TIME)
    print()
    text.print_lines(FORMER_PRELIMINARY_LINES)
    print()
    command: str = text.input_with_prompt(continue_command_hint_line)
    while True:
        text.print_full_line(FULL_LINE_LENGTH)
        if command.upper() == continue_command.name:
            break
        command: str = text.input_with_prompt(not_continue_command_preliminary_line)
    text.print_lines(LATTER_PRELIMINARY_LINES)
    print()
    print(STARTING_LINE)

    # Doing the rest of the game
    while True:
        print()
        command: str = text.input_with_prompt(see_command_hint_line)
        text.print_full_line(FULL_LINE_LENGTH)
        if command.upper() == see_command.name:
            break
        else:
            print(NOT_A_COMMAND_LINE)
    current_room_id: int = 0
    current_room = room_list[current_room_id]
    while True:
        print(current_room.enter_line)
        for current_object in current_room.interactables:
            print(current_object.seen_line)
        while True:
            print()

            # Asking the player what command to input
            command: str = text.input_with_prompt("Where would you want to go TO?")
            text.print_full_line(FULL_LINE_LENGTH)

            # Checking if the command has more than one space
            if text.get_amount_of_spaces(command) > 1:
                text.print_lines(COMMAND_TOO_LONG_LINES)
            else:
                # Checking if the command starts with "TO"
                if command[:(len(to_command.name) + 1)].upper() == to_command.name + " " \
                        or command.upper() == to_command.name:
                    # Checking if the command is only "TO"
                    if command.upper() == to_command.name:
                        print(incomplete_to_command_line)
                    else:
                        # Removing "TO" from command
                        remaining_command: str = command[(len(to_command.name) + 1):]

                        # Checking if an object is the remaining command
                        for current_object in current_room.interactables:
                            if remaining_command.upper() == current_object.name:
                                current_room_id: int = current_object.leading_room_id
                                if current_room_id == -1:
                                    print(EXIT_LINE)
                                    exit()
                                else:
                                    current_room = room_list[current_room_id]
                                break
                        else:
                            print(f"\"{remaining_command}\" isn't an object in the room.")
                            continue
                        break
                else:
                    print(NOT_A_COMMAND_LINE)


# Running main function
if __name__ == "__main__":
    main()
