# Importing libraries
from arcade import run
import window_07 as w

# Making constants
WINDOW_WIDTH: int = 512
WINDOW_HEIGHT: int = 512
WINDOW_TEXT: str = "Test"
BACKGROUND_COLOR = (64, 64, 64)


# Defining main function
def main():
    # Making class constants
    lab_window = w.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TEXT, BACKGROUND_COLOR)

    run()


# Running main function
if __name__ == "__main__":
    main()
