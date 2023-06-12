from tkinter import Frame, Label, Tk

from typing import Tuple, List, Dict

import main_window.settings as settings
import main_window.utils as utils
import main_window.labels as labels

# List of coordinates needed for buttons.
BUTTON_COORDS: List[Tuple[int, int]] = utils.get_button_coords(settings.game_grid)

# List of coordinates for correct labels.
CORRECT_COORDS: List[Tuple[int, int]] = utils.get_correct_labels(settings.game_grid)

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

    for coord in BUTTON_COORDS:
        # Creating button with assigned coordinates and settings.
        button = labels.GameButton(frame, coord, **settings.GAME_BUTTON_LABEL_SETTINGS)
        # Binding mouse actions to button.
        button.bind("<Button-1>", lambda i, button=button: change_number_up(button))
        button.bind("<Button-3>", lambda i, button=button: change_number_down(button))
        button.bind("<Button-2>", lambda i, button=button: highlight_button(button))
        buttons.append(button)

    return buttons


def highlight_button(button) -> None:
    """Highlights selected button."""

    if button['bg'] == 'SystemButtonFace':
        button['bg'] = 'coral'
        return

    if button['bg'] == 'coral':
        button['bg'] = 'SystemButtonFace'
        return


def change_number_up(button: labels.GameButton) -> None:
    """Increases selected button number."""

    # Changes number from 9 to 1.
    if button['text'] == '9':
        button['text'] = '1'
        return

    if int(button['text']) >= 1 < 9:
        button['text'] = str(int(button['text']) + 1)
        return


def change_number_down(button: labels.GameButton) -> None:
    """Decreases selected button number."""

    # Changes number from 1 to 9.
    if button['text'] == '1':
        button['text'] = '9'
        return

    if int(button['text']) >= 1 < 9:
        button['text'] = str(int(button['text']) - 1)
        return


def create_chosen_numbers(frame: Frame) -> List[Label]:
    """Creates labels for chosen numbers panel."""

    chosen_numbers = []

    for num in NUMBERS:
        chosen_number = Label(frame, text=num, **settings.CHOSEN_NUMBERS_LABEL_SETTINGS)
        # Highlighting number '1' by default.
        if num == '1':
            chosen_number['bg'] = 'coral'
        chosen_numbers.append(chosen_number)
        chosen_number.pack(side='left')

    return chosen_numbers


def create_correct_label(frame: Frame) -> List[Label]:

    correct_labels = []

    for coord in CORRECT_COORDS:
        if coord[0] != 4 and coord[1] != 4:
            if coord[0] < coord[1]:
                label = labels.CorrectLabel(frame, coord, **settings.CORRECT_LABEL_HORIZ_SETTINGS)
            else:
                label = labels.CorrectLabel(frame, coord, **settings.CORRECT_LABEL_VERTICAL_SETTINGS)
        else:
            if coord[0] < coord[1]:
                label = labels.CorrectLabel(frame, coord, **settings.ROW_CORRECT_LABEL_HORIZ_SETTINGS)
            else:
                label = labels.CorrectLabel(frame, coord, **settings.ROW_CORRECT_LABEL_VERTICAL_SETTINGS)
        correct_labels.append(label)

    return correct_labels


def create_rows(button: labels.GameButton) -> List[List[Tuple[int, int]]]:

    button_rows_horizontal = []
    button_rows_vertical = []

    for coord in BUTTON_COORDS:
        if coord[0] == button.coords[0]:
            if coord == button.coords:
                button_rows_vertical.append(coord)
            button_rows_horizontal.append(coord)
        elif coord[1] == button.coords[1]:
            button_rows_vertical.append(coord)

    return [button_rows_horizontal, button_rows_vertical]


def create_rows_dict(buttons: List[labels.GameButton]) -> Dict:

    rows_dict = {}
    print(buttons)

    for button in buttons:
        rows_dict[button.coords] = create_rows(button)

    return rows_dict
