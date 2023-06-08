from typing import Tuple, List

import main_window.utils as utils

ROWS_COUNT: int = 5
COLUMNS_COUNT: int = 5
BUTTONS_COUNT: int = 9

WINDOW_SETTINGS = {
    'main_width': '1300',
    'main_height': '550'
}

FRAME_SETTINGS = {
    'game_frame': {
        'window': {},
        'frame': {
            'x': 820,
            'y': 70
        }
    },
    'numbers_frame': {
        'window': {
            'pady': 10
        },
        'frame': {
            'x': 834,
            'y': 0,
        }
    }
}

GAME_BUTTON_LABEL_SETTINGS = {
    'width': 5,
    'height': 2,
    'padx': 10,
    'pady': 20,
    'text': '1',
    'font': ('Times', 25),
    'bd': 4,
    'bg': 'SystemButtonFace',
    'relief': 'raised'
}

CHOSEN_NUMBERS_LABEL_SETTINGS = {
    'width': 2,
    'height': 2,
    'padx': 10,
    'font': ('Times', 15),
    'fg': 'black',
    'bd': 3,
    'relief': 'raised'
}

game_grid: Tuple[Tuple[int, int]] = utils.initialize_grid(
    rows=ROWS_COUNT,
    columns=COLUMNS_COUNT
)
values: List[str] = utils.initialize_values(
    buttons_count=BUTTONS_COUNT
)
