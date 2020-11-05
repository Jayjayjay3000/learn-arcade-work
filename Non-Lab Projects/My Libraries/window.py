# Importing libraries
import arcade


# Defining classes
class W(arcade.Window):
    """
    Class for windows.
    """
    def __init__(self, width: int = 800, height: int = 600, title: str = "Arcade Window", background_color=(0, 0, 0),
                 fullscreen: bool = False, resizable: bool = False, update_rate=1/60, antialiasing: bool = True):
        """
        Constructs a new window as well as set the window's background color.

        :param width: Window width
        :param height: Window height
        :param title: Title (appears in title bar)
        :param background_color: List of 3 or 4 bytes in RGB/RGBA format.
        :param fullscreen: Should this be full screen?
        :param resizable: Can the user resize the window?
        :param update_rate: How frequently to update the window.
        :param antialiasing: Should OpenGL's anti-aliasing be enabled?
        """
        # Making the new window
        super().__init__(width, height, title, fullscreen, resizable, update_rate, antialiasing)

        # Setting additional class attributes
        self.color = background_color

        # Setting the window's background color
        arcade.set_background_color(self.color)

    def on_draw(self):
        """
        Renders the window.
        """
        # Starting to render the window
        arcade.start_render()
