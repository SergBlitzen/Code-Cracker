from tkinter import Tk, Frame, Label, Button
from typing import List, Dict, Tuple

import src.settings as settings
import src.funcs as funcs
import src.labels as labels


class MainWindow(Tk):
    """
    Main window implemented as inherited TK object with
    methods which are running by default when object is created.

    """

    def __init__(self):
        super().__init__()
        # Default Tk settings adjust.
        self.title('Code Cracker')
        self.geometry(f"{settings.WINDOW_SETTINGS['main_width']}"
                      f"x{settings.WINDOW_SETTINGS['main_height']}")

        # Custom window attributes.
        self.game_frame = self.create_game_frame()
        self.game_buttons = self.create_game_buttons()
        self.numbers_frame = self.create_numbers_frame()
        self.chosen_numbers = self.create_chosen_numbers()
        self.override_number_change()
        self.correct_labels = self.create_correct_labels()
        self.rows_dict = self.create_rows_dict()
        self.history_frames = self.create_history_frames()
        self.override_check_function()
        self.check_button = self.create_check_button()
        self.override_restart_function()
        self.restart_button = self.create_restart_button()

    def create_game_frame(self) -> Frame:
        """Creates main game frame and returns it as object."""

        frame = funcs.create_frame(
            self, settings.FRAME_SETTINGS['game_frame']
        )
        return frame

    def create_game_buttons(self) -> List[labels.GameButton]:
        """Creates game buttons and returns it as list of objects."""

        buttons = funcs.create_buttons(self.game_frame)
        return buttons

    def create_numbers_frame(self) -> Frame:
        """Creates chosen numbers frame and returns it as object."""

        frame = funcs.create_frame(
            self, settings.FRAME_SETTINGS['numbers_frame']
        )
        return frame

    def create_chosen_numbers(self) -> List[Label]:
        """Creates chosen numbers labels and returns it as list of objects."""

        numbers = funcs.create_chosen_numbers(self.numbers_frame)
        return numbers

    def override_number_change(self) -> None:
        """
        Overriding number changing functions by wrapping
        them with other functions and providing attributes
        as parameters here to prevent circular import.
        """

        funcs.change_number_up = funcs.highlight_numbers(
            funcs.change_number_up,
            self.game_buttons,
            self.chosen_numbers
        )
        funcs.change_number_down = funcs.highlight_numbers(
            funcs.change_number_down,
            self.game_buttons,
            self.chosen_numbers
        )
        return

    def create_correct_labels(self) -> List[labels.CorrectLabel]:
        """Creates correct labels and returns them as list of objects."""

        labels = funcs.create_correct_label(
            self.game_frame,
            'game_frame'
        )
        return labels

    def create_rows_dict(self) ->\
            Dict[(Tuple[int, int]):List[labels.GameButton]]:
        """Creates dictionary with row and columns data for each button."""

        rows_dict = funcs.create_button_rows_dict(self.game_buttons)
        return rows_dict

    def create_history_frames(self) -> List[Frame]:
        """Creates history frames and returns them as list of objects."""

        frames = funcs.create_history_turns_frames(self)
        return frames

    def override_check_function(self) -> None:
        """
        Overriding check function by wrapping it in other and
        providing window data here to prevent circular import.
        """

        funcs.check = funcs.show_row_numbers(
            funcs.check,
            self.game_buttons,
            self.correct_labels,
            self.rows_dict,
            self.history_frames
        )
        return

    def create_check_button(self) -> Button:
        """Creates check button and returns it as object."""

        button = funcs.create_check_button(self.game_frame)
        return button

    def override_restart_function(self) -> None:
        """
        Overriding restart function by wrapping it in other
        and providing window data to prevent circular import.
        """

        funcs.restart = funcs.reset_labels(
            funcs.restart,
            self.game_buttons,
            self.correct_labels,
            self.history_frames
        )
        return

    def create_restart_button(self) -> Button:
        """Creates restart button and returns it as object."""

        button = funcs.create_restart_button(self)
        return button
