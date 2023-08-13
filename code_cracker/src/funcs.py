from functools import wraps
from tkinter import Frame, Label, Tk, Button

from typing import Tuple, List, Dict

import src.settings as settings
import src.utils as utils
import src.labels as labels

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


def create_correct_label(frame: Frame, label_settings) -> List[labels.CorrectLabel]:
    """Creates coordinates for indication labels."""

    correct_labels = []

    for coord in CORRECT_COORDS:
        if coord[0] != 4 and coord[1] != 4:
            if coord[0] < coord[1]:
                label = labels.CorrectLabel(
                    frame, coord, **settings.CORRECT_LABEL_HORIZ_SETTINGS[label_settings]
                )
            else:
                label = labels.CorrectLabel(
                    frame, coord, **settings.CORRECT_LABEL_VERTICAL_SETTINGS[label_settings]
                )
        else:
            if coord[0] < coord[1]:
                label = labels.CorrectLabel(
                    frame, coord, **settings.ROW_CORRECT_LABEL_HORIZ_SETTINGS[label_settings]
                )
            else:
                label = labels.CorrectLabel(
                    frame, coord, **settings.ROW_CORRECT_LABEL_VERTICAL_SETTINGS[label_settings]
                )
        correct_labels.append(label)

    return correct_labels


def create_button_rows_dict(buttons) ->\
            Dict[(Tuple[int, int]):List[labels.GameButton]]:
    """
    Creates dictionary with rows and columns for each button.

    :param buttons: Game buttons.
    :return rows_dict:
    """

    rows_dict = {}

    for main_button in buttons:
        horizontal_row: List[labels.GameButton] = []
        vertical_row: List[labels.GameButton] = []
        for secondary_button in buttons:
            # Row and columns are formed by checking coordinates.
            # First digit is horizontal, second is vertical.
            if main_button.coords[0] == secondary_button.coords[0]:
                if main_button.coords == secondary_button.coords:
                    vertical_row.append(secondary_button)
                horizontal_row.append(secondary_button)
            elif main_button.coords[1] == secondary_button.coords[1]:
                vertical_row.append(secondary_button)
        rows_dict[main_button.coords] = [horizontal_row, vertical_row]

    return rows_dict


def create_check_button(frame: Frame) -> Button:
    """
    Creates check button.

    :param frame: Game frame.
    :return Button check_button: Check button.
    """

    check_coord = utils.get_check_coord()
    check_button = Button(
        frame, command=check, **settings.CHECK_BUTTON_SETTINGS
    )
    check_button.grid(
        row=check_coord[0], column=check_coord[1], rowspan=2, columnspan=2
    )

    return check_button


def create_restart_button(window) -> Button:
    """
    Creates restart button.

    :param window: Game window.
    :return Button check_button: Check button.
    """

    restart_button = Button(
        window, command=restart, **settings.RESTART_BUTTON_SETTINGS
    )
    # Coordinates are magical for now.
    restart_button.place(x=350, y=475)

    return restart_button


def show_row_numbers(func, buttons, labels, rows_dict, history_frames):
    """
    Wrapper for check function. Changes correct label numbers.
    Also calls function to fill history frames.

    :param func: Main function.
    :param buttons: List of game buttons.
    :param labels: List of correct labels.
    :param rows_dict: Dictionary of rows and columns for each button.
    :param history_frames: List of history frames.
    :return: Wrapped function.
    """

    @wraps(func)
    def wrapper(*args):

        # Limit is magical for now.
        # Some optimization required.
        if settings.current_turns < 7:
            correct_labels = []
            row_correct_labels = []

            # Filling distinct correct and row correct label lists.
            for label in labels:
                label['text'] = '0'
                if label['bg'] == 'green':
                    row_correct_labels.append(label)
                else:
                    correct_labels.append(label)

            for button in buttons:
                button_row = rows_dict[button.coords][0]
                button_column = rows_dict[button.coords][1]
                # Process of getting button labels. Optimization required.
                button_labels = (
                    [label for label in correct_labels if button.coords[0] == label.coords[0]
                     or button.coords[1] == label.coords[1]] +
                    [label for label in row_correct_labels if button.coords[0] == label.coords[0]
                     or button.coords[1] == label.coords[1]])
                # Process of getting label numbers.
                # Odd numbers are vertical labels,
                # even are horizontal.
                row_values = [but['text'] for but in button_row]
                if str(button.value) in row_values:
                    if str(button.value) == button['text']:
                        button_labels[0]['text'] = int(button_labels[0]['text']) + 1
                    else:
                        button_labels[2]['text'] = int(button_labels[2]['text']) + 1
                column_values = [but['text'] for but in button_column]
                if str(button.value) in column_values:
                    if str(button.value) == button['text']:
                        button_labels[1]['text'] = int(button_labels[1]['text']) + 1
                    else:
                        button_labels[3]['text'] = int(button_labels[3]['text']) + 1

            # Calling function to fill history.
            fill_history(buttons, labels, history_frames)

        # Last move is either winning or losing.
        # Some adjustments required.
        elif settings.current_turns == 7:
            fill_history(buttons, labels, history_frames)
            for label in labels:
                label['text'] = '3'

            for button in buttons:
                button['text'] = button.value

            button_values = [button.value for button in buttons]
            for frame in history_frames:
                for i in range(9):
                    if frame['buttons'][i]['text'] == button_values[i]:
                        frame['buttons'][i]['bg'] = 'coral'

        # For now exceeding the limit does nothing.
        else:
            return

        # Calling check function.
        func(*args)
        return

    return wrapper


def create_history_buttons(frame) -> List[labels.HistoryButton]:
    """
    Creates list of button labels for each frame.

    :param Frame frame: History frame.
    :return List buttons: List of button labels.
    """

    buttons: List[labels.HistoryButton] = []
    for coord in BUTTON_COORDS:
        button = labels.HistoryButton(
            frame, coord, **settings.HISTORY_BUTTON_LABEL_SETTINGS
        )
        buttons.append(button)

    return buttons


def create_history_turns_frames(window) -> List[Frame]:
    """
    Creates list of frames for provided window.

    :param window: Main window object.
    :return List history_turns: List of history turns frames.
    """

    history_turns = []

    for coord in settings.HISTORY_TURNS_FRAMES_COORDS:
        settings.FRAME_SETTINGS['history_frame']['frame'] = coord
        history_frame = create_frame(
            window,
            settings.FRAME_SETTINGS['history_frame']
        )
        history_labels = create_history_turns_labels(history_frame)
        history_turns.append(history_labels)

    return history_turns


def create_history_turns_labels(history_frame) -> Dict[str: List]:
    """
    Creates dictionary of correct labels data for provided history frame.

    :param history_frame: History turn frame.
    :return Dict history_labels: Dictionary of history frame data
    """

    history_labels = {
        'correct_labels': create_correct_label(history_frame, 'history_frame'),
        'buttons': create_history_buttons(history_frame)
    }

    return history_labels


def fill_history(buttons, labels, history_frames) -> None:
    """

    :param buttons: Game buttons.
    :param labels: List of correct labels.
    :param history_frames: List of history turns data.
    :return None:
    """

    current_turn = history_frames[settings.current_turns]
    current_turns_button_values = [button['text'] for button in buttons]
    current_turns_label_values = [label['text'] for label in labels]

    for button in current_turn['buttons']:
        button['text'] = current_turns_button_values[0]
        current_turns_button_values.pop(0)

    for label in current_turn['correct_labels']:
        label['text'] = current_turns_label_values[0]
        current_turns_label_values.pop(0)

    return


def check() -> None:
    """Main check function."""

    settings.current_turns += 1
    return


def reset_labels(func, buttons, labels, history_frames):
    """
    Wrapper for reset function.

    :param func: Main restart function.
    :param buttons: Game buttons.
    :param labels: Correct labels.
    :param history_frames: History frames.
    """

    @wraps(func)
    def wrapper(*args):
        func(*args)

        # Resetting turn counter.
        settings.values = utils.initialize_values(settings.BUTTONS_COUNT)

        # Resetting values and color.
        for button in buttons:
            button.value = settings.values.pop()
            button['text'] = '1'
            button['bg'] = 'SystemButtonFace'

        for label in labels:
            label['text'] = 0

        for frame in history_frames:
            for button in frame['buttons']:
                button['text'] = ''
                button['bg'] = 'SystemButtonFace'
            for label in frame['correct_labels']:
                label['text'] = ''

        return

    return wrapper


def restart() -> None:
    """Main restart function."""

    # Resetting turn counter.
    settings.current_turns = 0
    return
