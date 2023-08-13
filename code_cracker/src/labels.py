from typing import Tuple
from tkinter import Label

from src.settings import values


class GameButton(Label):

    # Initializing label settings with super(), instantly placing
    # with grid(coords) and assigning value from settings.
    def __init__(self, master, coords: Tuple[int, int], **kwargs):
        super().__init__(master=master, **kwargs)
        self.coords = coords
        self.grid(row=coords[0], column=coords[1])
        self.value = values.pop()

    def __eq__(self, other):
        return self.coords == other

    def __str__(self):
        return self.coords

    def __repr__(self):
        return str(f'Button: {self.coords}')


class CorrectLabel(Label):
    """
    Distinct class of label for storing coordinates data.
    """

    def __init__(self, master, coords, **kwargs):
        super().__init__(master=master, **kwargs)
        self.coords = coords
        self.grid(row=coords[0], column=coords[1])

    def __str__(self):
        return self.coords

    def __repr__(self):
        return str(f'Label: {self.coords}, "{self.show_type()}"')

    def show_type(self) -> str | None:
        """Method for checking the label type."""

        if self['bg'] == 'green':
            return 'row_correct'
        elif self['bg'] == 'orange':
            return 'correct'
        else:
            return None


class HistoryButton(Label):

    def __init__(self, master, coords: Tuple[int, int], **kwargs):
        super().__init__(master=master, **kwargs)
        self.coords = coords
        self.grid(row=coords[0], column=coords[1])
