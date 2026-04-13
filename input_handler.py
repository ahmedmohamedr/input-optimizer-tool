import pygame

class InputHandler:
    """
    A class to handle user inputs for the game. This class uses
    the Pygame library to capture keyboard and mouse events. The
    captured inputs can then be used to control game actions.
    """

    def __init__(self):
        """
        Initialize the InputHandler class.
        Here we initialize the Pygame library and create a dictionary
        to keep track of currently pressed keys.
        """
        pygame.init()  # Initialize all Pygame modules
        self.keys_pressed = {}  # Dictionary to store keys' states

    def update(self) -> None:
        """
        Update the state of the input handler by capturing all
        events that happen since the last frame. This method updates
        the keys_pressed dictionary based on the current state of
        the keyboard.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # When a key is pressed, set its state to True
                self.keys_pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                # When a key is released, set its state to False
                if event.key in self.keys_pressed:
                    self.keys_pressed[event.key] = False

    def is_key_pressed(self, key: int) -> bool:
        """
        Check if a particular key is currently pressed.

        Parameters:
            key (int): The Pygame key constant for the key to check.

        Returns:
            bool: True if the key is pressed, False otherwise.
        """
        return self.keys_pressed.get(key, False)

    def quit(self) -> None:
        """
        Properly quit the Pygame library by uninitializing all modules.
        This should be called when the game is exiting.
        """
        pygame.quit()