from typing import Tuple, List

import src.utils as utils


TURNS_LIMIT: int = 8

ROWS_COUNT: int = 5
COLUMNS_COUNT: int = 5
BUTTONS_COUNT: int = 9

WINDOW_SETTINGS = {
    'main_width': '1300',
    'main_height': '550'
}

HISTORY_TURNS_FRAMES_COORDS = [
    {'x': 25, 'y': 70},
    {'x': 225, 'y': 70},
    {'x': 425, 'y': 70},
    {'x': 625, 'y': 70},
    {'x': 25, 'y': 300},
    {'x': 225, 'y': 300},
    {'x': 425, 'y': 300},
    {'x': 625, 'y': 300},
]

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
    },
    'history_frame': {
        'window': {
            'height': 550,
            'width': 700,
        },
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


CORRECT_LABEL_HORIZ_SETTINGS = {
    'game_frame': {
        'width': 4,
        'height': 5,
        'text': '0',
        'font': ('Times', 15),
        'bd': 3,
        'bg': 'orange',
        'relief': 'raised'
    },
    'history_frame': {
        'height': 2,
        'width': 3,
        'bd': 2,
        'font': ('Times', 8),
        'relief': 'raised',
        'pady': 2,
        'bg': 'orange'
    }
}

ROW_CORRECT_LABEL_HORIZ_SETTINGS = {
    'game_frame':{
        'width': 4,
        'height': 5,
        'text': '0',
        'font': ('Times', 15),
        'bd': 3,
        'bg': 'green',
        'relief': 'raised'
    },
    'history_frame': {
        'height': 2,
        'width': 3,
        'bd': 2,
        'font': ('Times', 8),
        'relief': 'raised',
        'pady': 2,
        'bg': 'green'
    }
}

CORRECT_LABEL_VERTICAL_SETTINGS = {
    'game_frame': {
        'width': 10,
        'height': 2,
        'text': '0',
        'font': ('Times', 15),
        'bd': 3,
        'bg': 'orange',
        'relief': 'raised'
    },
    'history_frame': {
        'height': 1,
        'width': 4,
        'bd': 2,
        'font': ('Times', 8),
        'relief': 'raised',
        'padx': 3,
        'pady': 2,
        'bg': 'orange'
    }
}

ROW_CORRECT_LABEL_VERTICAL_SETTINGS = {
    'game_frame': {
        'width': 10,
        'height': 2,
        'text': '0',
        'font': ('Times', 15),
        'bd': 3,
        'bg': 'green',
        'relief': 'raised'
    },
    'history_frame': {
        'height': 1,
        'width': 4,
        'bd': 2,
        'font': ('Times', 8),
        'relief': 'raised',
        'padx': 3,
        'pady': 2,
        'bg': 'green'
    }
}


CHECK_BUTTON_SETTINGS = {
    'width': 8,
    'height': 4,
    'text': 'Check',
    'font': ('Times', 15),
    'bd': 4,
    'relief': 'raised'
}


HISTORY_BUTTON_LABEL_SETTINGS = {
    'height': 2,
    'width': 4,
    'bd': 2,
    'font': ('Times', 10),
    'relief': 'raised'
}


RESTART_BUTTON_SETTINGS = {
    'text': 'Restart',
    'font': ('Times', 20),
    'bd': 4
}

current_turns = 0

game_grid: Tuple[Tuple[int, int]] = utils.initialize_grid(
    rows=ROWS_COUNT,
    columns=COLUMNS_COUNT
)

values: List[str] = utils.initialize_values(
    buttons_count=BUTTONS_COUNT
)
