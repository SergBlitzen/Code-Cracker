from tkinter import Frame, Label, Tk

from typing import Tuple, List
from functools import wraps

import main_window.settings as settings
import main_window.utils as utils
import main_window.labels as labels

# List of coordinates needed for buttons.
COORDS: List[Tuple[int, int]] = utils.get_button_coords(settings.game_grid)

# List of numbers needed for highlights.
NUMBERS: List[int] = utils.get_chosen_numbers()


def create_frame(window: Tk, kwargs) -> Frame:
    """
    Creates frame with assigned data.

    :param window: Window to place (main window).
    :param kwargs: Dictionary of kwargs to create frame.
    :return Frame: New frame.
    """

    new_frame = Frame(window, **kwargs['window'])
    new_frame.place(**kwargs['frame'])

    return new_frame


def create_buttons(frame: Frame) -> List[labels.GameButton]:
    """Creates buttons and packs them in list."""

    buttons = []

    for coord in COORDS:
        # Creating button with assigned coordinates and settings.
        button = labels.GameButton(frame, coord, **settings.GAME_BUTTON_LABEL_SETTINGS)
        # Binding mouse actions to button.
        button.bind("<Button-1>", lambda i, button=button: change_number_up(button))
        button.bind("<Button-3>", lambda i, button=button: change_number_down(button))
        button.bind("<Button-2>", lambda i, button=button: highlight_button(button))
        buttons.append(button)

    return buttons


def highlight_button(button):
    """Highlights selected button."""

    if button['bg'] == 'SystemButtonFace':
        button['bg'] = 'coral'
        return

    if button['bg'] == 'coral':
        button['bg'] = 'SystemButtonFace'
        return


def highlight_numbers(func):

    def wrapper(*args):
        func(*args)
        return

    return wrapper


@highlight_numbers
def change_number_up(button):
    """Increases selected button number."""

    # Changes number from 9 to 1.
    if button['text'] == '9':
        button['text'] = '1'
        return

    if int(button['text']) >= 1 < 9:
        button['text'] = str(int(button['text']) + 1)
        return


@highlight_numbers
def change_number_down(button):
    """Decreases selected button number."""

    # Changes number from 1 to 9.
    if button['text'] == '1':
        button['text'] = '9'
        return

    if int(button['text']) >= 1 < 9:
        button['text'] = str(int(button['text']) - 1)
        return


def create_chosen_numbers(frame: Frame) -> List[Label]:

    chosen_numbers = []

    for num in NUMBERS:
        chosen_number = Label(frame, text=num, **settings.CHOSEN_NUMBERS_LABEL_SETTINGS)
        chosen_numbers.append(chosen_number)
        chosen_number.pack(side='left')

    return chosen_numbers
