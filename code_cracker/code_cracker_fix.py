from tkinter import *

import main_window.settings as settings
import main_window.funcs as funcs
from main_window.labels import GameButton


main_window = Tk()
main_window.title('Code Cracker')
main_window.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")

game_frame = Frame(main_window)
game_frame.place(x=820, y=70)

buttons = funcs.create_buttons(game_frame)


def main():
    main_window.mainloop()


if __name__ == '__main__':
    main()

