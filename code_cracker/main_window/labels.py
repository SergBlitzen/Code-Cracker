from typing import Tuple
from tkinter import Label

from main_window.settings import values


class InfoLabel:
    ...


class GameButton(Label):

    # Initializing label settings with super(), instantly placing
    # with grid(coords) and assigning value from settings.
    def __init__(self, master, coords: Tuple[int, int], **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(row=coords[0], column=coords[1])
        self.value = values.pop()


