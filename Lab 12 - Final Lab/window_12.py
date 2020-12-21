# Importing libraries
import arcade


# Defining classes
class Window(arcade.Window):
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
        self.mouse_x = None
        self.mouse_y = None
        self.mouse_on_window: bool = False

        # Setting the window's background color
        arcade.set_background_color(self.color)

    def on_draw(self):
        """
        Renders the window.
        """
        # Starting to render the window
        arcade.start_render()

    def update_mouse_position(self, mouse_x: float, mouse_y: float):
        """


        :param mouse_x:
        :param mouse_y:
        """
        self.mouse_x: float = mouse_x
        self.mouse_y: float = mouse_y

    def on_mouse_motion(self, mouse_x: float, mouse_y: float, mouse_dx: float, mouse_dy: float):
        """


        :param mouse_x:
        :param mouse_y:
        :param mouse_dx:
        :param mouse_dy:
        """
        # [...]
        self.update_mouse_position(mouse_x, mouse_y)

    def on_mouse_enter(self, mouse_x: int, mouse_y: int):
        """


        :param mouse_x:
        :param mouse_y:
        """
        # [...]
        self.update_mouse_position(mouse_x, mouse_y)
        self.mouse_on_window: bool = True

    def on_mouse_leave(self, mouse_x: int, mouse_y: int):
        """


        :param mouse_x:
        :param mouse_y:
        """
        # [...]
        self.update_mouse_position(mouse_x, mouse_y)
        self.mouse_on_window: bool = False

    def on_mouse_press(self, mouse_x: float, mouse_y: float, mouse_button: int, modifiers: int):
        """


        :param mouse_x:
        :param mouse_y:
        :param mouse_button:
        :param modifiers:
        """
        self.update_mouse_position(mouse_x, mouse_y)
