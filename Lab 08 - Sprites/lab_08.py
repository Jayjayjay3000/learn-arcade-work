# Importing libraries
import arcade

# Making constants
WINDOW_WIDTH: int = 512
WINDOW_HEIGHT: int = 512
WINDOW_TEXT: str = "Test"


class Window(arcade.Window):
    def __init__(self, width: int = 800, height: int = 600, title: str = "Arcade Window",
                 fullscreen: bool = False, resizable: bool = False, update_rate=1/60, antialiasing: bool = True):
        super().__init__(width, height, title, fullscreen, resizable, update_rate, antialiasing)


# Defining main function
def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TEXT)
    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
