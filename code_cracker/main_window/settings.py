from typing import Tuple, List

from main_window.utils import initialize_grid, initialize_values

WIDTH: str = '1300'
HEIGHT: str = '550'

ROWS_COUNT: int = 5
COLUMNS_COUNT: int = 5
BUTTONS_COUNT: int = 9

GAME_BUTTON_LABEL_SETTINGS = {
    'width': 5,
    'height': 2,
    'text': '1',
    'font': ('Times', 25),
    'padx': 10,
    'pady': 20,
    'bd': 4,
    'bg': 'SystemButtonFace',
    'relief': 'raised'
}

game_grid: Tuple[Tuple[int, int]] = initialize_grid(
    rows=ROWS_COUNT,
    columns=COLUMNS_COUNT
)
values: List[str] = initialize_values(
    buttons_count=BUTTONS_COUNT
)
