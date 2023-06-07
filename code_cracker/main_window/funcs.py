import tkinter

from typing import Tuple, List
from functools import wraps

import main_window.settings as settings
from main_window.labels import GameButton
from main_window.utils import get_button_coords


COORDS: List[Tuple[int, int]] = get_button_coords(settings.game_grid)


def create_buttons(frame: tkinter.Frame) -> List[GameButton]:

    buttons = []

    for coord in COORDS:
        button = GameButton(frame, coord, **settings.GAME_BUTTON_LABEL_SETTINGS)
        button.bind("<Button-1>", lambda i, button=button: change_number_up(button))
        button.bind("<Button-3>", lambda i, button=button: change_number_down(button))
        button.bind("<Button-2>", lambda i, button=button: highlight_button(button))
        buttons.append(button)

    return buttons


def highlight_button(button):

    if button['bg'] == 'SystemButtonFace':
        button['bg'] = 'coral'
        return

    if button['bg'] == 'coral':
        button['bg'] = 'SystemButtonFace'
        return


def change_number_up(button):

    if button['text'] == '9':
        button['text'] = '1'
        return

    if int(button['text']) >= 1 < 9:
        button['text'] = str(int(button['text']) + 1)
        return


def change_number_down(button):

    if button['text'] == '1':
        button['text'] = '9'
        return

    if int(button['text']) >= 1 < 9:
        button['text'] = str(int(button['text']) - 1)
        return
