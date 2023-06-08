from tkinter import Tk

import main_window.settings as settings
import main_window.funcs as funcs


# Initializing main window.
main_window = Tk()
main_window.title('Code Cracker')
main_window.geometry(f"{settings.WINDOW_SETTINGS['main_width']}"
                     f"x{settings.WINDOW_SETTINGS['main_height']}")

# Initializing game frame.
game_frame = funcs.create_frame(
    main_window,
    settings.FRAME_SETTINGS['game_frame']
)

# Initializing buttons.
buttons = funcs.create_buttons(game_frame)

# Initializing numbers frame.
numbers_frame = funcs.create_frame(
    main_window,
    settings.FRAME_SETTINGS['numbers_frame']
)

# Initializing number labels.
numbers = funcs.create_chosen_numbers(numbers_frame)
