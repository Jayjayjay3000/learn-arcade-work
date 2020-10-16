# Importing libraries
import arcade
import draw_shapes as draw

# Making constants
WINDOW_WIDTH: int = 512
WINDOW_HEIGHT: int = 512
WINDOW_TEXT: str = "Test"


# Defining main function
def main():
    # Making class constants
    window = draw.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TEXT, (64, 64, 64))

    arcade.run()


# Running main function
if __name__ == "__main__":
    main()
