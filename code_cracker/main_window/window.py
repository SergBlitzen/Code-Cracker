from tkinter import Tk
from functools import wraps

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
game_buttons = funcs.create_buttons(game_frame)

# Initializing numbers frame.
numbers_frame = funcs.create_frame(
    main_window,
    settings.FRAME_SETTINGS['numbers_frame']
)

# Initializing number labels.
chosen_numbers = funcs.create_chosen_numbers(numbers_frame)


# Function needs access to window elements, so it is implemented here.
def highlight_numbers(func, buttons, labels):
    """
    Highlights chosen numbers panel above the game frame.
    Functions as decorator.

    :param func: Wrapped function.
    :param List[GameButton] buttons: Game buttons list.
    :param List[Label] labels: Number labels list.
    :return wrapper: Returns wrapped function.
    """

    @wraps(func)
    def wrapper(*args):
        func(*args)
        # Getting set of used numbers and changing color of
        # labels according to selected.
        num_set = set([button['text'] for button in buttons])

        for number in labels:
            if number['text'] in num_set:
                number['bg'] = 'coral'
            else:
                number['bg'] = 'SystemButtonFace'

        return

    return wrapper


# Wrapping functions for number changing.
funcs.change_number_up = highlight_numbers(
    funcs.change_number_up,
    game_buttons,
    chosen_numbers
)
funcs.change_number_down = highlight_numbers(
    funcs.change_number_down,
    game_buttons,
    chosen_numbers
)

# Initializing correct labels.
correct_labels = funcs.create_correct_label(game_frame)

coords_dict = funcs.create_rows_dict(game_buttons)
print(coords_dict)
