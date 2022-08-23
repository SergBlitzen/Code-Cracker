from tkinter import *
import random

game_list = list(range(1, 10))
random.shuffle(game_list)


class GameButton:

    def __init__(self, row, column):
        self.value = random.choice(game_list)
        game_list.remove(self.value)

        self.button = Label(
            game_frame,
            width=5,
            height=2,
            text='1',
            font=('Times', 25),
            padx=10,
            pady=20,
            bd=4,
            relief=RAISED,
            bg='SystemButtonFace'
        )
        self.button.grid(row=row, column=column)
        self.text_number = self.button['text']
        self.config = self.button.config
        self.bind = self.button.bind
        self.get = self.button.cget


def restart():

    global turns
    turns = 0

    new_game_list = list(range(1, 10))
    random.shuffle(new_game_list)

    for i in buttons:
        i.value = random.choice(new_game_list)
        new_game_list.remove(i.value)
        i.config(bg='SystemButtonFace', text='1')
        i.text_number = '1'

    for i in history_buttons:
        for j in i:
            j.config(bg='SystemButtonFace', text='')

    for i in labels_history:
        i.config(text='')

    highlight_numbers()

    correct_label_horizontal_1.config(text='0')
    correct_label_vertical_1.config(text='0')
    correct_label_horizontal_2.config(text='0')
    correct_label_vertical_2.config(text='0')
    correct_label_horizontal_3.config(text='0')
    correct_label_vertical_3.config(text='0')

    row_correct_label_horizontal_1.config(text='0')
    row_correct_label_vertical_1.config(text='0')
    row_correct_label_horizontal_2.config(text='0')
    row_correct_label_vertical_2.config(text='0')
    row_correct_label_horizontal_3.config(text='0')
    row_correct_label_vertical_3.config(text='0')


def highlight_button(button):

    if button.get('bg') == 'SystemButtonFace':
        button.config(bg='coral')
        return

    if button.get('bg') == 'coral':
        button.config(bg='SystemButtonFace')
        return


def change_number_up(button):

    while int(button.text_number) >= 1 <= 9:
        button.text_number = str(eval(button.text_number) + 1)
        button.config(text=str(button.text_number))
        break

    if int(button.text_number) == 10:
        button.text_number = '1'
        button.config(text=button.text_number)

    highlight_numbers()


def change_number_down(button):

    while int(button.text_number) >= 1 <= 9:
        button.text_number = str(eval(button.text_number) - 1)
        button.config(text=str(button.text_number))
        break

    if int(button.text_number) == 0:
        button.text_number = '9'
        button.config(text=button.text_number)

    highlight_numbers()


def check():

    global turns

    turns += 1

    while turns < 8:
        show_correct_numbers()
        show_correct_row_numbers()
        fill_history()
        break

    if turns == 8:
        print('You lose!')

        fill_history()

        for i in buttons:
            i.config(text=i.value)

        for i in correct_labels:
            i.config(text=str('3'))

        for i in row_correct_labels:
            i.config(text=str('3'))

    return


def show_correct_numbers():

    correct_number_1_1 = 0  # верхняя горизонтальная
    correct_number_1_2 = 0  # центральная горизонтальная
    correct_number_1_3 = 0  # нижняя горизонтальная
    correct_number_2_1 = 0  # левая вертикальная
    correct_number_2_2 = 0  # центральная вертикальная
    correct_number_2_3 = 0  # правая вертикальная

    correct_label_horizontal_1.config(text=str(correct_number_1_1))
    correct_label_vertical_1.config(text=str(correct_number_2_1))
    correct_label_horizontal_2.config(text=str(correct_number_1_2))
    correct_label_vertical_2.config(text=str(correct_number_2_2))
    correct_label_horizontal_3.config(text=str(correct_number_1_3))
    correct_label_vertical_3.config(text=str(correct_number_2_3))

    if button_1.text_number == str(button_1.value):
        correct_number_1_1 += 1
        correct_number_2_1 += 1
        correct_label_horizontal_1.config(text=str(correct_number_1_1))
        correct_label_vertical_1.config(text=str(correct_number_2_1))

    else:
        correct_number_1_1 += 0
        correct_number_2_1 += 0
        correct_label_horizontal_1.config(text=str(correct_number_1_1))
        correct_label_vertical_1.config(text=str(correct_number_2_1))

    if button_2.text_number == str(button_2.value):
        correct_number_1_1 += 1
        correct_number_2_2 += 1
        correct_label_horizontal_1.config(text=str(correct_number_1_1))
        correct_label_vertical_2.config(text=str(correct_number_2_2))

    else:
        correct_number_1_1 += 0
        correct_number_2_2 += 0
        correct_label_horizontal_1.config(text=str(correct_number_1_1))
        correct_label_vertical_2.config(text=str(correct_number_2_2))

    if button_3.text_number == str(button_3.value):
        correct_number_1_1 += 1
        correct_number_2_3 += 1
        correct_label_horizontal_1.config(text=str(correct_number_1_1))
        correct_label_vertical_3.config(text=str(correct_number_2_3))

    else:
        correct_number_1_1 += 0
        correct_number_2_3 += 0
        correct_label_horizontal_1.config(text=str(correct_number_1_1))
        correct_label_vertical_3.config(text=str(correct_number_2_3))

    if button_4.text_number == str(button_4.value):
        correct_number_1_2 += 1
        correct_number_2_1 += 1
        correct_label_horizontal_2.config(text=str(correct_number_1_2))
        correct_label_vertical_1.config(text=str(correct_number_2_1))

    else:
        correct_number_1_2 += 0
        correct_number_2_1 += 0
        correct_label_horizontal_2.config(text=str(correct_number_1_2))
        correct_label_vertical_1.config(text=str(correct_number_2_1))

    if button_5.text_number == str(button_5.value):
        correct_number_1_2 += 1
        correct_number_2_2 += 1
        correct_label_horizontal_2.config(text=str(correct_number_1_2))
        correct_label_vertical_2.config(text=str(correct_number_2_2))

    else:
        correct_number_1_2 += 0
        correct_number_2_2 += 0
        correct_label_horizontal_2.config(text=str(correct_number_1_2))
        correct_label_vertical_2.config(text=str(correct_number_2_2))

    if button_6.text_number == str(button_6.value):
        correct_number_1_2 += 1
        correct_number_2_3 += 1
        correct_label_horizontal_2.config(text=str(correct_number_1_2))
        correct_label_vertical_3.config(text=str(correct_number_2_3))

    else:
        correct_number_1_2 += 0
        correct_number_2_3 += 0
        correct_label_horizontal_2.config(text=str(correct_number_1_2))
        correct_label_vertical_3.config(text=str(correct_number_2_3))

    if button_7.text_number == str(button_7.value):
        correct_number_1_3 += 1
        correct_number_2_1 += 1
        correct_label_horizontal_3.config(text=str(correct_number_1_3))
        correct_label_vertical_1.config(text=str(correct_number_2_1))

    else:
        correct_number_1_3 += 0
        correct_number_2_1 += 0
        correct_label_horizontal_3.config(text=str(correct_number_1_3))
        correct_label_vertical_1.config(text=str(correct_number_2_1))

    if button_8.text_number == str(button_8.value):
        correct_number_1_3 += 1
        correct_number_2_2 += 1
        correct_label_horizontal_3.config(text=str(correct_number_1_3))
        correct_label_vertical_2.config(text=str(correct_number_2_2))

    else:
        correct_number_1_3 += 0
        correct_number_2_2 += 0
        correct_label_horizontal_3.config(text=str(correct_number_1_3))
        correct_label_vertical_2.config(text=str(correct_number_2_2))

    if button_9.text_number == str(button_9.value):
        correct_number_1_3 += 1
        correct_number_2_3 += 1
        correct_label_horizontal_3.config(text=str(correct_number_1_3))
        correct_label_vertical_3.config(text=str(correct_number_2_3))

    else:
        correct_number_1_3 += 0
        correct_number_2_3 += 0
        correct_label_horizontal_3.config(text=str(correct_number_1_3))
        correct_label_vertical_3.config(text=str(correct_number_2_3))

    print("Turns: " + str(turns))

    if correct_number_1_1 ==\
       correct_number_1_2 ==\
       correct_number_1_3 ==\
       correct_number_2_1 ==\
       correct_number_2_2 ==\
       correct_number_2_3 == 3:
        print("You win!")

        for i in button_1_history:
            if i['text'] == str(button_1.value):
                i.config(bg='coral')

        for i in button_2_history:
            if i['text'] == str(button_2.value):
                i.config(bg='coral')

        for i in button_3_history:
            if i['text'] == str(button_3.value):
                i.config(bg='coral')

        for i in button_4_history:
            if i['text'] == str(button_4.value):
                i.config(bg='coral')

        for i in button_5_history:
            if i['text'] == str(button_5.value):
                i.config(bg='coral')

        for i in button_6_history:
            if i['text'] == str(button_6.value):
                i.config(bg='coral')

        for i in button_7_history:
            if i['text'] == str(button_7.value):
                i.config(bg='coral')

        for i in button_8_history:
            if i['text'] == str(button_8.value):
                i.config(bg='coral')

        for i in button_9_history:
            if i['text'] == str(button_9.value):
                i.config(bg='coral')

    return


def show_correct_row_numbers():
    """
    суть функции - проверить, находится ли значение кнопки в ряде из трёх и есть
    ли среди них верно отмеченные кнопки, чтобы не учитывать их, после чего
    отправить каждой плашке итоговую цифру, которая по умолчанию "0"
    """
    correct_number_1_1 = 0  # верхняя горизонтальная
    correct_number_1_2 = 0  # центральная горизонтальная
    correct_number_1_3 = 0  # нижняя горизонтальная
    correct_number_2_1 = 0  # левая вертикальная
    correct_number_2_2 = 0  # центральная вертикальная
    correct_number_2_3 = 0  # правая вертикальная

    # обнуление всех лейблов перед тем, как снова их изменить
    row_correct_label_horizontal_1.config(text=str(correct_number_1_1))
    row_correct_label_vertical_1.config(text=str(correct_number_2_1))
    row_correct_label_horizontal_2.config(text=str(correct_number_1_2))
    row_correct_label_vertical_2.config(text=str(correct_number_2_2))
    row_correct_label_horizontal_3.config(text=str(correct_number_1_3))
    row_correct_label_vertical_3.config(text=str(correct_number_2_3))

    # блоки для каждой кнопки разделены, чтобы не запутаться
    # кнопка 1
    ####################################################################################################################
    if str(button_1.value) in [button_1.text_number, button_2.text_number, button_3.text_number]:
        if str(button_1.value) != button_1.text_number:
            correct_number_1_1 += 1
            row_correct_label_horizontal_1.config(text=str(correct_number_1_1))

    else:
        correct_number_1_1 += 0
        row_correct_label_horizontal_1.config(text=str(correct_number_1_1))

    if str(button_1.value) in [button_1.text_number, button_4.text_number, button_7.text_number]:
        if str(button_1.value) != button_1.text_number:
            correct_number_2_1 += 1
            row_correct_label_vertical_1.config(text=str(correct_number_2_1))
    else:
        correct_number_2_1 += 0
        row_correct_label_vertical_1.config(text=str(correct_number_2_1))

    # кнопка 2
    ####################################################################################################################
    if str(button_2.value) in [button_1.text_number, button_2.text_number, button_3.text_number]:
        if str(button_2.value) != button_2.text_number:
            correct_number_1_1 += 1
            row_correct_label_horizontal_1.config(text=str(correct_number_1_1))

    else:
        correct_number_1_1 += 0
        row_correct_label_horizontal_1.config(text=str(correct_number_1_1))

    if str(button_2.value) in [button_2.text_number, button_5.text_number, button_8.text_number]:
        if str(button_2.value) != button_2.text_number:
            correct_number_2_2 += 1
            row_correct_label_vertical_2.config(text=str(correct_number_2_2))

    else:
        correct_number_2_2 += 0
        row_correct_label_vertical_2.config(text=str(correct_number_2_2))

    # кнопка 3
    ####################################################################################################################
    if str(button_3.value) in [button_1.text_number, button_2.text_number, button_3.text_number]:
        if str(button_3.value) != button_3.text_number:
            correct_number_1_1 += 1
            row_correct_label_horizontal_1.config(text=str(correct_number_1_1))

    else:
        correct_number_1_1 += 0
        row_correct_label_horizontal_1.config(text=str(correct_number_1_1))

    if str(button_3.value) in [button_3.text_number, button_6.text_number, button_9.text_number]:
        if str(button_3.value) != button_3.text_number:
            correct_number_2_3 += 1
            row_correct_label_vertical_3.config(text=str(correct_number_2_3))

    else:
        correct_number_2_3 += 0
        row_correct_label_vertical_3.config(text=str(correct_number_2_3))

    # кнопка 2
    ####################################################################################################################
    if str(button_4.value) in [button_4.text_number, button_5.text_number, button_6.text_number]:
        if str(button_4.value) != button_4.text_number:
            correct_number_1_2 += 1
            row_correct_label_horizontal_2.config(text=str(correct_number_1_2))

    else:
        correct_number_1_2 += 0
        row_correct_label_horizontal_2.config(text=str(correct_number_1_2))

    if str(button_4.value) in [button_1.text_number, button_4.text_number, button_7.text_number]:
        if str(button_4.value) != button_4.text_number:
            correct_number_2_1 += 1
            row_correct_label_vertical_1.config(text=str(correct_number_2_1))

    else:
        correct_number_2_1 += 0
        row_correct_label_vertical_1.config(text=str(correct_number_2_1))

    # кнопка 5
    ####################################################################################################################
    if str(button_5.value) in [button_4.text_number, button_5.text_number, button_6.text_number]:
        if str(button_5.value) != button_5.text_number:
            correct_number_1_2 += 1
            row_correct_label_horizontal_2.config(text=str(correct_number_1_2))

    else:
        correct_number_1_2 += 0
        row_correct_label_horizontal_2.config(text=str(correct_number_1_2))

    if str(button_5.value) in [button_2.text_number, button_5.text_number, button_8.text_number]:
        if str(button_5.value) != button_5.text_number:
            correct_number_2_2 += 1
            row_correct_label_vertical_2.config(text=str(correct_number_2_2))

    else:
        correct_number_2_2 += 0
        row_correct_label_vertical_2.config(text=str(correct_number_2_2))

    # кнопка 6
    ####################################################################################################################
    if str(button_6.value) in [button_4.text_number, button_5.text_number, button_6.text_number]:
        if str(button_6.value) != button_6.text_number:
            correct_number_1_2 += 1
            row_correct_label_horizontal_2.config(text=str(correct_number_1_2))

    else:
        correct_number_1_2 += 0
        row_correct_label_horizontal_2.config(text=str(correct_number_1_2))

    if str(button_6.value) in [button_3.text_number, button_6.text_number, button_9.text_number]:
        if str(button_6.value) != button_6.text_number:
            correct_number_2_3 += 1
            row_correct_label_vertical_3.config(text=str(correct_number_2_3))

    else:
        correct_number_2_3 += 0
        row_correct_label_vertical_3.config(text=str(correct_number_2_3))

    # кнопка 7
    ####################################################################################################################
    if str(button_7.value) in [button_7.text_number, button_8.text_number, button_9.text_number]:
        if str(button_7.value) != button_7.text_number:
            correct_number_1_3 += 1
            row_correct_label_horizontal_3.config(text=str(correct_number_1_3))

    else:
        correct_number_1_3 += 0
        row_correct_label_horizontal_3.config(text=str(correct_number_1_3))

    if str(button_7.value) in [button_1.text_number, button_4.text_number, button_7.text_number]:
        if str(button_7.value) != button_7.text_number:
            correct_number_2_1 += 1
            row_correct_label_vertical_1.config(text=str(correct_number_2_1))

    else:
        correct_number_2_1 += 0
        row_correct_label_vertical_1.config(text=str(correct_number_2_1))

    # кнопка 8
    ####################################################################################################################
    if str(button_8.value) in [button_7.text_number, button_8.text_number, button_9.text_number]:
        if str(button_8.value) != button_8.text_number:
            correct_number_1_3 += 1
            row_correct_label_horizontal_3.config(text=str(correct_number_1_3))

    else:
        correct_number_1_3 += 0
        row_correct_label_horizontal_3.config(text=str(correct_number_1_3))

    if str(button_8.value) in [button_2.text_number, button_5.text_number, button_8.text_number]:
        if str(button_8.value) != button_8.text_number:
            correct_number_2_2 += 1
            row_correct_label_vertical_2.config(text=str(correct_number_2_2))

    else:
        correct_number_2_2 += 0
        row_correct_label_vertical_2.config(text=str(correct_number_2_2))

    # кнопка 9
    ####################################################################################################################
    if str(button_9.value) in [button_7.text_number, button_8.text_number, button_9.text_number]:
        if str(button_9.value) != button_9.text_number:
            correct_number_1_3 += 1
            row_correct_label_horizontal_3.config(text=str(correct_number_1_3))

    else:
        correct_number_1_3 += 0
        row_correct_label_horizontal_3.config(text=str(correct_number_1_3))

    if str(button_9.value) in [button_3.text_number, button_6.text_number, button_9.text_number]:
        if str(button_9.value) != button_9.text_number:
            correct_number_2_3 += 1
            row_correct_label_vertical_3.config(text=str(correct_number_2_3))

    else:
        correct_number_2_3 += 0
        row_correct_label_vertical_3.config(text=str(correct_number_2_3))

    return


def highlight_numbers():

    global buttons

    for i in buttons:
        if '1' in i.text_number:
            chosen_number_1.config(bg='coral')
            break
        else:
            chosen_number_1.config(bg='SystemButtonFace')

    for i in buttons:
        if '2' in i.text_number:
            chosen_number_2.config(bg='coral')
            break
        else:
            chosen_number_2.config(bg='SystemButtonFace')

    for i in buttons:
        if '3' in i.text_number:
            chosen_number_3.config(bg='coral')
            break
        else:
            chosen_number_3.config(bg='SystemButtonFace')

    for i in buttons:
        if '4' in i.text_number:
            chosen_number_4.config(bg='coral')
            break
        else:
            chosen_number_4.config(bg='SystemButtonFace')

    for i in buttons:
        if '5' in i.text_number:
            chosen_number_5.config(bg='coral')
            break
        else:
            chosen_number_5.config(bg='SystemButtonFace')

    for i in buttons:
        if '6' in i.text_number:
            chosen_number_6.config(bg='coral')
            break
        else:
            chosen_number_6.config(bg='SystemButtonFace')

    for i in buttons:
        if '7' in i.text_number:
            chosen_number_7.config(bg='coral')
            break
        else:
            chosen_number_7.config(bg='SystemButtonFace')

    for i in buttons:
        if '8' in i.text_number:
            chosen_number_8.config(bg='coral')
            break
        else:
            chosen_number_8.config(bg='SystemButtonFace')

    for i in buttons:
        if '9' in i.text_number:
            chosen_number_9.config(bg='coral')
            break
        else:
            chosen_number_9.config(bg='SystemButtonFace')


def fill_history():

    global turns

    if turns == 1:
        button_1_history_turn_1.config(text=button_1.text_number)
        button_2_history_turn_1.config(text=button_2.text_number)
        button_3_history_turn_1.config(text=button_3.text_number)
        button_4_history_turn_1.config(text=button_4.text_number)
        button_5_history_turn_1.config(text=button_5.text_number)
        button_6_history_turn_1.config(text=button_6.text_number)
        button_7_history_turn_1.config(text=button_7.text_number)
        button_8_history_turn_1.config(text=button_8.text_number)
        button_9_history_turn_1.config(text=button_9.text_number)
        correct_label_horizontal_1_turn_1.config(text=correct_label_horizontal_1['text'])
        correct_label_horizontal_2_turn_1.config(text=correct_label_horizontal_2['text'])
        correct_label_horizontal_3_turn_1.config(text=correct_label_horizontal_3['text'])
        correct_label_vertical_1_turn_1.config(text=correct_label_vertical_1['text'])
        correct_label_vertical_2_turn_1.config(text=correct_label_vertical_2['text'])
        correct_label_vertical_3_turn_1.config(text=correct_label_vertical_3['text'])
        row_correct_label_horizontal_1_turn_1.config(text=row_correct_label_horizontal_1['text'])
        row_correct_label_horizontal_2_turn_1.config(text=row_correct_label_horizontal_2['text'])
        row_correct_label_horizontal_3_turn_1.config(text=row_correct_label_horizontal_3['text'])
        row_correct_label_vertical_1_turn_1.config(text=row_correct_label_vertical_1['text'])
        row_correct_label_vertical_2_turn_1.config(text=row_correct_label_vertical_2['text'])
        row_correct_label_vertical_3_turn_1.config(text=row_correct_label_vertical_3['text'])

    if turns == 2:
        button_1_history_turn_2.config(text=button_1.text_number)
        button_2_history_turn_2.config(text=button_2.text_number)
        button_3_history_turn_2.config(text=button_3.text_number)
        button_4_history_turn_2.config(text=button_4.text_number)
        button_5_history_turn_2.config(text=button_5.text_number)
        button_6_history_turn_2.config(text=button_6.text_number)
        button_7_history_turn_2.config(text=button_7.text_number)
        button_8_history_turn_2.config(text=button_8.text_number)
        button_9_history_turn_2.config(text=button_9.text_number)
        correct_label_horizontal_1_turn_2.config(text=correct_label_horizontal_1['text'])
        correct_label_horizontal_2_turn_2.config(text=correct_label_horizontal_2['text'])
        correct_label_horizontal_3_turn_2.config(text=correct_label_horizontal_3['text'])
        correct_label_vertical_1_turn_2.config(text=correct_label_vertical_1['text'])
        correct_label_vertical_2_turn_2.config(text=correct_label_vertical_2['text'])
        correct_label_vertical_3_turn_2.config(text=correct_label_vertical_3['text'])
        row_correct_label_horizontal_1_turn_2.config(text=row_correct_label_horizontal_1['text'])
        row_correct_label_horizontal_2_turn_2.config(text=row_correct_label_horizontal_2['text'])
        row_correct_label_horizontal_3_turn_2.config(text=row_correct_label_horizontal_3['text'])
        row_correct_label_vertical_1_turn_2.config(text=row_correct_label_vertical_1['text'])
        row_correct_label_vertical_2_turn_2.config(text=row_correct_label_vertical_2['text'])
        row_correct_label_vertical_3_turn_2.config(text=row_correct_label_vertical_3['text'])

    if turns == 3:
        button_1_history_turn_3.config(text=button_1.text_number)
        button_2_history_turn_3.config(text=button_2.text_number)
        button_3_history_turn_3.config(text=button_3.text_number)
        button_4_history_turn_3.config(text=button_4.text_number)
        button_5_history_turn_3.config(text=button_5.text_number)
        button_6_history_turn_3.config(text=button_6.text_number)
        button_7_history_turn_3.config(text=button_7.text_number)
        button_8_history_turn_3.config(text=button_8.text_number)
        button_9_history_turn_3.config(text=button_9.text_number)
        correct_label_horizontal_1_turn_3.config(text=correct_label_horizontal_1['text'])
        correct_label_horizontal_2_turn_3.config(text=correct_label_horizontal_2['text'])
        correct_label_horizontal_3_turn_3.config(text=correct_label_horizontal_3['text'])
        correct_label_vertical_1_turn_3.config(text=correct_label_vertical_1['text'])
        correct_label_vertical_2_turn_3.config(text=correct_label_vertical_2['text'])
        correct_label_vertical_3_turn_3.config(text=correct_label_vertical_3['text'])
        row_correct_label_horizontal_1_turn_3.config(text=row_correct_label_horizontal_1['text'])
        row_correct_label_horizontal_2_turn_3.config(text=row_correct_label_horizontal_2['text'])
        row_correct_label_horizontal_3_turn_3.config(text=row_correct_label_horizontal_3['text'])
        row_correct_label_vertical_1_turn_3.config(text=row_correct_label_vertical_1['text'])
        row_correct_label_vertical_2_turn_3.config(text=row_correct_label_vertical_2['text'])
        row_correct_label_vertical_3_turn_3.config(text=row_correct_label_vertical_3['text'])

    if turns == 4:
        button_1_history_turn_4.config(text=button_1.text_number)
        button_2_history_turn_4.config(text=button_2.text_number)
        button_3_history_turn_4.config(text=button_3.text_number)
        button_4_history_turn_4.config(text=button_4.text_number)
        button_5_history_turn_4.config(text=button_5.text_number)
        button_6_history_turn_4.config(text=button_6.text_number)
        button_7_history_turn_4.config(text=button_7.text_number)
        button_8_history_turn_4.config(text=button_8.text_number)
        button_9_history_turn_4.config(text=button_9.text_number)
        correct_label_horizontal_1_turn_4.config(text=correct_label_horizontal_1['text'])
        correct_label_horizontal_2_turn_4.config(text=correct_label_horizontal_2['text'])
        correct_label_horizontal_3_turn_4.config(text=correct_label_horizontal_3['text'])
        correct_label_vertical_1_turn_4.config(text=correct_label_vertical_1['text'])
        correct_label_vertical_2_turn_4.config(text=correct_label_vertical_2['text'])
        correct_label_vertical_3_turn_4.config(text=correct_label_vertical_3['text'])
        row_correct_label_horizontal_1_turn_4.config(text=row_correct_label_horizontal_1['text'])
        row_correct_label_horizontal_2_turn_4.config(text=row_correct_label_horizontal_2['text'])
        row_correct_label_horizontal_3_turn_4.config(text=row_correct_label_horizontal_3['text'])
        row_correct_label_vertical_1_turn_4.config(text=row_correct_label_vertical_1['text'])
        row_correct_label_vertical_2_turn_4.config(text=row_correct_label_vertical_2['text'])
        row_correct_label_vertical_3_turn_4.config(text=row_correct_label_vertical_3['text'])

    if turns == 5:
        button_1_history_turn_5.config(text=button_1.text_number)
        button_2_history_turn_5.config(text=button_2.text_number)
        button_3_history_turn_5.config(text=button_3.text_number)
        button_4_history_turn_5.config(text=button_4.text_number)
        button_5_history_turn_5.config(text=button_5.text_number)
        button_6_history_turn_5.config(text=button_6.text_number)
        button_7_history_turn_5.config(text=button_7.text_number)
        button_8_history_turn_5.config(text=button_8.text_number)
        button_9_history_turn_5.config(text=button_9.text_number)
        correct_label_horizontal_1_turn_5.config(text=correct_label_horizontal_1['text'])
        correct_label_horizontal_2_turn_5.config(text=correct_label_horizontal_2['text'])
        correct_label_horizontal_3_turn_5.config(text=correct_label_horizontal_3['text'])
        correct_label_vertical_1_turn_5.config(text=correct_label_vertical_1['text'])
        correct_label_vertical_2_turn_5.config(text=correct_label_vertical_2['text'])
        correct_label_vertical_3_turn_5.config(text=correct_label_vertical_3['text'])
        row_correct_label_horizontal_1_turn_5.config(text=row_correct_label_horizontal_1['text'])
        row_correct_label_horizontal_2_turn_5.config(text=row_correct_label_horizontal_2['text'])
        row_correct_label_horizontal_3_turn_5.config(text=row_correct_label_horizontal_3['text'])
        row_correct_label_vertical_1_turn_5.config(text=row_correct_label_vertical_1['text'])
        row_correct_label_vertical_2_turn_5.config(text=row_correct_label_vertical_2['text'])
        row_correct_label_vertical_3_turn_5.config(text=row_correct_label_vertical_3['text'])

    if turns == 6:
        button_1_history_turn_6.config(text=button_1.text_number)
        button_2_history_turn_6.config(text=button_2.text_number)
        button_3_history_turn_6.config(text=button_3.text_number)
        button_4_history_turn_6.config(text=button_4.text_number)
        button_5_history_turn_6.config(text=button_5.text_number)
        button_6_history_turn_6.config(text=button_6.text_number)
        button_7_history_turn_6.config(text=button_7.text_number)
        button_8_history_turn_6.config(text=button_8.text_number)
        button_9_history_turn_6.config(text=button_9.text_number)
        correct_label_horizontal_1_turn_6.config(text=correct_label_horizontal_1['text'])
        correct_label_horizontal_2_turn_6.config(text=correct_label_horizontal_2['text'])
        correct_label_horizontal_3_turn_6.config(text=correct_label_horizontal_3['text'])
        correct_label_vertical_1_turn_6.config(text=correct_label_vertical_1['text'])
        correct_label_vertical_2_turn_6.config(text=correct_label_vertical_2['text'])
        correct_label_vertical_3_turn_6.config(text=correct_label_vertical_3['text'])
        row_correct_label_horizontal_1_turn_6.config(text=row_correct_label_horizontal_1['text'])
        row_correct_label_horizontal_2_turn_6.config(text=row_correct_label_horizontal_2['text'])
        row_correct_label_horizontal_3_turn_6.config(text=row_correct_label_horizontal_3['text'])
        row_correct_label_vertical_1_turn_6.config(text=row_correct_label_vertical_1['text'])
        row_correct_label_vertical_2_turn_6.config(text=row_correct_label_vertical_2['text'])
        row_correct_label_vertical_3_turn_6.config(text=row_correct_label_vertical_3['text'])

    if turns == 7:
        button_1_history_turn_7.config(text=button_1.text_number)
        button_2_history_turn_7.config(text=button_2.text_number)
        button_3_history_turn_7.config(text=button_3.text_number)
        button_4_history_turn_7.config(text=button_4.text_number)
        button_5_history_turn_7.config(text=button_5.text_number)
        button_6_history_turn_7.config(text=button_6.text_number)
        button_7_history_turn_7.config(text=button_7.text_number)
        button_8_history_turn_7.config(text=button_8.text_number)
        button_9_history_turn_7.config(text=button_9.text_number)
        correct_label_horizontal_1_turn_7.config(text=correct_label_horizontal_1['text'])
        correct_label_horizontal_2_turn_7.config(text=correct_label_horizontal_2['text'])
        correct_label_horizontal_3_turn_7.config(text=correct_label_horizontal_3['text'])
        correct_label_vertical_1_turn_7.config(text=correct_label_vertical_1['text'])
        correct_label_vertical_2_turn_7.config(text=correct_label_vertical_2['text'])
        correct_label_vertical_3_turn_7.config(text=correct_label_vertical_3['text'])
        row_correct_label_horizontal_1_turn_7.config(text=row_correct_label_horizontal_1['text'])
        row_correct_label_horizontal_2_turn_7.config(text=row_correct_label_horizontal_2['text'])
        row_correct_label_horizontal_3_turn_7.config(text=row_correct_label_horizontal_3['text'])
        row_correct_label_vertical_1_turn_7.config(text=row_correct_label_vertical_1['text'])
        row_correct_label_vertical_2_turn_7.config(text=row_correct_label_vertical_2['text'])
        row_correct_label_vertical_3_turn_7.config(text=row_correct_label_vertical_3['text'])

    if turns == 8:
        button_1_history_turn_8.config(text=button_1.text_number)
        button_2_history_turn_8.config(text=button_2.text_number)
        button_3_history_turn_8.config(text=button_3.text_number)
        button_4_history_turn_8.config(text=button_4.text_number)
        button_5_history_turn_8.config(text=button_5.text_number)
        button_6_history_turn_8.config(text=button_6.text_number)
        button_7_history_turn_8.config(text=button_7.text_number)
        button_8_history_turn_8.config(text=button_8.text_number)
        button_9_history_turn_8.config(text=button_9.text_number)
        correct_label_horizontal_1_turn_8.config(text=correct_label_horizontal_1['text'])
        correct_label_horizontal_2_turn_8.config(text=correct_label_horizontal_2['text'])
        correct_label_horizontal_3_turn_8.config(text=correct_label_horizontal_3['text'])
        correct_label_vertical_1_turn_8.config(text=correct_label_vertical_1['text'])
        correct_label_vertical_2_turn_8.config(text=correct_label_vertical_2['text'])
        correct_label_vertical_3_turn_8.config(text=correct_label_vertical_3['text'])
        row_correct_label_horizontal_1_turn_8.config(text=row_correct_label_horizontal_1['text'])
        row_correct_label_horizontal_2_turn_8.config(text=row_correct_label_horizontal_2['text'])
        row_correct_label_horizontal_3_turn_8.config(text=row_correct_label_horizontal_3['text'])
        row_correct_label_vertical_1_turn_8.config(text=row_correct_label_vertical_1['text'])
        row_correct_label_vertical_2_turn_8.config(text=row_correct_label_vertical_2['text'])
        row_correct_label_vertical_3_turn_8.config(text=row_correct_label_vertical_3['text'])

        for i in button_1_history:
            if i['text'] == str(button_1.value):
                i.config(bg='coral')

        for i in button_2_history:
            if i['text'] == str(button_2.value):
                i.config(bg='coral')

        for i in button_3_history:
            if i['text'] == str(button_3.value):
                i.config(bg='coral')

        for i in button_4_history:
            if i['text'] == str(button_4.value):
                i.config(bg='coral')

        for i in button_5_history:
            if i['text'] == str(button_5.value):
                i.config(bg='coral')

        for i in button_6_history:
            if i['text'] == str(button_6.value):
                i.config(bg='coral')

        for i in button_7_history:
            if i['text'] == str(button_7.value):
                i.config(bg='coral')

        for i in button_8_history:
            if i['text'] == str(button_8.value):
                i.config(bg='coral')

        for i in button_9_history:
            if i['text'] == str(button_9.value):
                i.config(bg='coral')


window = Tk()
window.title('Code Cracker')
window.geometry("1300x550")


turns = 0


game_frame = Frame(window)
game_frame.place(x=820, y=70)


button_1 = GameButton(0, 0)
button_1.bind("<Button-1>", lambda i, button=button_1: change_number_up(button))
button_1.bind("<Button-3>", lambda i, button=button_1: change_number_down(button))
button_1.bind("<Button-2>", lambda i, button=button_1: highlight_button(button))

button_2 = GameButton(0, 1)
button_2.bind("<Button-1>", lambda i, button=button_2: change_number_up(button))
button_2.bind("<Button-3>", lambda i, button=button_2: change_number_down(button))
button_2.bind("<Button-2>", lambda i, button=button_2: highlight_button(button))

button_3 = GameButton(0, 2)
button_3.bind("<Button-1>", lambda i, button=button_3: change_number_up(button))
button_3.bind("<Button-3>", lambda i, button=button_3: change_number_down(button))
button_3.bind("<Button-2>", lambda i, button=button_3: highlight_button(button))

button_4 = GameButton(1, 0)
button_4.bind("<Button-1>", lambda i, button=button_4: change_number_up(button))
button_4.bind("<Button-3>", lambda i, button=button_4: change_number_down(button))
button_4.bind("<Button-2>", lambda i, button=button_4: highlight_button(button))

button_5 = GameButton(1, 1)
button_5.bind("<Button-1>", lambda i, button=button_5: change_number_up(button))
button_5.bind("<Button-3>", lambda i, button=button_5: change_number_down(button))
button_5.bind("<Button-2>", lambda i, button=button_5: highlight_button(button))

button_6 = GameButton(1, 2)
button_6.bind("<Button-1>", lambda i, button=button_6: change_number_up(button))
button_6.bind("<Button-3>", lambda i, button=button_6: change_number_down(button))
button_6.bind("<Button-2>", lambda i, button=button_6: highlight_button(button))

button_7 = GameButton(2, 0)
button_7.bind("<Button-1>", lambda i, button=button_7: change_number_up(button))
button_7.bind("<Button-3>", lambda i, button=button_7: change_number_down(button))
button_7.bind("<Button-2>", lambda i, button=button_7: highlight_button(button))

button_8 = GameButton(2, 1)
button_8.bind("<Button-1>", lambda i, button=button_8: change_number_up(button))
button_8.bind("<Button-3>", lambda i, button=button_8: change_number_down(button))
button_8.bind("<Button-2>", lambda i, button=button_8: highlight_button(button))

button_9 = GameButton(2, 2)
button_9.bind("<Button-1>", lambda i, button=button_9: change_number_up(button))
button_9.bind("<Button-3>", lambda i, button=button_9: change_number_down(button))
button_9.bind("<Button-2>", lambda i, button=button_9: highlight_button(button))

buttons = [button_1,
           button_2,
           button_3,
           button_4,
           button_5,
           button_6,
           button_7,
           button_8,
           button_9]


chosen_numbers = Frame(window, pady=10)
chosen_numbers.place(x=834, y=0)

chosen_number_1 = Label(
    chosen_numbers,
    text='1',
    font=('Times', 15),
    fg='black', bg='white',
    height=2,
    width=2,
    bd=3,
    relief=RAISED,
    padx=10
)
chosen_number_1.pack(side="left")

chosen_number_2 = Label(
    chosen_numbers,
    text='2',
    font=('Times', 15),
    fg='black', bg='white',
    height=2,
    width=2,
    bd=3,
    relief=RAISED,
    padx=10
)
chosen_number_2.pack(side="left")

chosen_number_3 = Label(
    chosen_numbers,
    text='3',
    font=('Times', 15),
    fg='black',
    bg='white',
    height=2,
    width=2,
    bd=3,
    relief=RAISED,
    padx=10
)
chosen_number_3.pack(side="left")

chosen_number_4 = Label(
    chosen_numbers,
    text='4',
    font=('Times', 15),
    fg='black',
    bg='white',
    height=2,
    width=2,
    bd=3,
    relief=RAISED,
    padx=10
)
chosen_number_4.pack(side="left")

chosen_number_5 = Label(
    chosen_numbers,
    text='5',
    font=('Times', 15),
    fg='black',
    bg='white',
    height=2,
    width=2,
    bd=3,
    relief=RAISED,
    padx=10
)
chosen_number_5.pack(side="left")

chosen_number_6 = Label(
    chosen_numbers,
    text='6',
    font=('Times', 15),
    fg='black',
    bg='white',
    height=2,
    width=2,
    bd=3,
    relief=RAISED,
    padx=10
)
chosen_number_6.pack(side="left")

chosen_number_7 = Label(
    chosen_numbers,
    text='7',
    font=('Times', 15),
    fg='black', bg='white',
    height=2,
    width=2,
    bd=3,
    relief=RAISED,
    padx=10
)
chosen_number_7.pack(side="left")

chosen_number_8 = Label(
    chosen_numbers,
    text='8',
    font=('Times', 15),
    fg='black',
    bg='white',
    height=2,
    width=2,
    bd=3,
    relief=RAISED,
    padx=10
)
chosen_number_8.pack(side="left")

chosen_number_9 = Label(
    chosen_numbers,
    text='9',
    font=('Times', 15),
    fg='black',
    bg='white',
    height=2,
    width=2,
    bd=3,
    relief=RAISED,
    padx=10
)
chosen_number_9.pack(side="left")

highlight_numbers()


correct_label_horizontal_1 = Label(
    game_frame,
    width=4,
    height=5,
    bg='orange',
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
correct_label_horizontal_1.grid(row=0, column=3)

correct_label_horizontal_2 = Label(
    game_frame,
    width=4,
    height=5,
    bg='orange',
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
correct_label_horizontal_2.grid(row=1, column=3)

correct_label_horizontal_3 = Label(
    game_frame,
    width=4,
    height=5,
    bg='orange',
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
correct_label_horizontal_3.grid(row=2, column=3)

correct_label_vertical_1 = Label(
    game_frame,
    width=10,
    height=2,
    bg='orange',
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
correct_label_vertical_1.grid(row=3, column=0)

correct_label_vertical_2 = Label(
    game_frame,
    width=10,
    height=2,
    bg='orange',
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
correct_label_vertical_2.grid(row=3, column=1)

correct_label_vertical_3 = Label(
    game_frame,
    width=10,
    height=2,
    bg='orange',
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
correct_label_vertical_3.grid(row=3, column=2)

correct_labels = [correct_label_horizontal_1, correct_label_horizontal_2, correct_label_horizontal_3,
                  correct_label_vertical_1, correct_label_vertical_2, correct_label_vertical_3]


row_correct_label_horizontal_1 = Label(
    game_frame,
    width=4,
    height=5,
    bg="green",
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
row_correct_label_horizontal_1.grid(row=0, column=4)

row_correct_label_horizontal_2 = Label(
    game_frame,
    width=4,
    height=5,
    bg="green",
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
row_correct_label_horizontal_2.grid(row=1, column=4)

row_correct_label_horizontal_3 = Label(
    game_frame,
    width=4,
    height=5,
    bg="green",
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
row_correct_label_horizontal_3.grid(row=2, column=4)

row_correct_label_vertical_1 = Label(
    game_frame,
    width=10,
    height=2,
    bg="green",
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
row_correct_label_vertical_1.grid(row=4, column=0)

row_correct_label_vertical_2 = Label(
    game_frame,
    width=10,
    height=2,
    bg="green",
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
row_correct_label_vertical_2.grid(row=4, column=1)

row_correct_label_vertical_3 = Label(
    game_frame,
    width=10,
    height=2,
    bg="green",
    text='0',
    font=('Times', 15),
    bd=3,
    relief=RAISED
)
row_correct_label_vertical_3.grid(row=4, column=2)

row_correct_labels = [row_correct_label_horizontal_1, row_correct_label_horizontal_2, row_correct_label_horizontal_3,
                      row_correct_label_vertical_1, row_correct_label_vertical_2, row_correct_label_vertical_3]


check = Button(
    game_frame,
    width=8,
    height=4,
    text='Check',
    font=('Times', 15),
    command=check,
    bd=4,
    relief=RAISED
)
check.grid(row=3, column=3, rowspan=2, columnspan=2)



# здесь начинается блок для фреймов лога ходов
#######################################################################################################################
history_turn_1 = Frame(window, height=550, width=700)
history_turn_1.place(x=25, y=70)


button_1_history_turn_1 = Label(
    history_turn_1,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_1_history_turn_1.grid(row=0, column=0)

button_2_history_turn_1 = Label(
    history_turn_1,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_2_history_turn_1.grid(row=0, column=1)

button_3_history_turn_1 = Label(
    history_turn_1,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_3_history_turn_1.grid(row=0, column=2)

button_4_history_turn_1 = Label(
    history_turn_1,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_4_history_turn_1.grid(row=1, column=0)

button_5_history_turn_1 = Label(
    history_turn_1,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_5_history_turn_1.grid(row=1, column=1)

button_6_history_turn_1 = Label(
    history_turn_1,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_6_history_turn_1.grid(row=1, column=2)

button_7_history_turn_1 = Label(
    history_turn_1,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_7_history_turn_1.grid(row=2, column=0)

button_8_history_turn_1 = Label(
    history_turn_1,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_8_history_turn_1.grid(row=2, column=1)

button_9_history_turn_1 = Label(
    history_turn_1,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_9_history_turn_1.grid(row=2, column=2)



correct_label_horizontal_1_turn_1 = Label(
    history_turn_1,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_1_turn_1.grid(row=0, column=3)

correct_label_horizontal_2_turn_1 = Label(
    history_turn_1,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_2_turn_1.grid(row=1, column=3)

correct_label_horizontal_3_turn_1 = Label(
    history_turn_1,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_3_turn_1.grid(row=2, column=3)

correct_label_vertical_1_turn_1 = Label(
    history_turn_1,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_1_turn_1.grid(row=3, column=0)

correct_label_vertical_2_turn_1 = Label(
    history_turn_1,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_2_turn_1.grid(row=3, column=1)

correct_label_vertical_3_turn_1 = Label(
    history_turn_1,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_3_turn_1.grid(row=3, column=2)


row_correct_label_horizontal_1_turn_1 = Label(
    history_turn_1,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_1_turn_1.grid(row=0, column=4)

row_correct_label_horizontal_2_turn_1 = Label(
    history_turn_1,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_2_turn_1.grid(row=1, column=4)

row_correct_label_horizontal_3_turn_1 = Label(
    history_turn_1,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_3_turn_1.grid(row=2, column=4)

row_correct_label_vertical_1_turn_1 = Label(
    history_turn_1,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_1_turn_1.grid(row=4, column=0)

row_correct_label_vertical_2_turn_1 = Label(
    history_turn_1,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_2_turn_1.grid(row=4, column=1)

row_correct_label_vertical_3_turn_1 = Label(
    history_turn_1,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_3_turn_1.grid(row=4, column=2)


########################################################################################################################
history_turn_2 = Frame(window, height=550, width=700)
history_turn_2.place(x=225, y=70)

button_1_history_turn_2 = Label(
    history_turn_2,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_1_history_turn_2.grid(row=0, column=0)

button_2_history_turn_2 = Label(
    history_turn_2,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_2_history_turn_2.grid(row=0, column=1)

button_3_history_turn_2 = Label(
    history_turn_2,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_3_history_turn_2.grid(row=0, column=2)

button_4_history_turn_2 = Label(
    history_turn_2,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_4_history_turn_2.grid(row=1, column=0)

button_5_history_turn_2 = Label(
    history_turn_2,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_5_history_turn_2.grid(row=1, column=1)

button_6_history_turn_2 = Label(
    history_turn_2,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_6_history_turn_2.grid(row=1, column=2)

button_7_history_turn_2 = Label(
    history_turn_2,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_7_history_turn_2.grid(row=2, column=0)

button_8_history_turn_2 = Label(
    history_turn_2,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_8_history_turn_2.grid(row=2, column=1)

button_9_history_turn_2 = Label(
    history_turn_2,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_9_history_turn_2.grid(row=2, column=2)


correct_label_horizontal_1_turn_2 = Label(
    history_turn_2,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_1_turn_2.grid(row=0, column=3)

correct_label_horizontal_2_turn_2 = Label(
    history_turn_2,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_2_turn_2.grid(row=1, column=3)

correct_label_horizontal_3_turn_2 = Label(
    history_turn_2,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_3_turn_2.grid(row=2, column=3)

correct_label_vertical_1_turn_2 = Label(
    history_turn_2,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_1_turn_2.grid(row=3, column=0)

correct_label_vertical_2_turn_2 = Label(
    history_turn_2,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_2_turn_2.grid(row=3, column=1)

correct_label_vertical_3_turn_2 = Label(
    history_turn_2,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_3_turn_2.grid(row=3, column=2)


row_correct_label_horizontal_1_turn_2 = Label(
    history_turn_2,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_1_turn_2.grid(row=0, column=4)

row_correct_label_horizontal_2_turn_2 = Label(
    history_turn_2,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_2_turn_2.grid(row=1, column=4)

row_correct_label_horizontal_3_turn_2 = Label(
    history_turn_2,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_3_turn_2.grid(row=2, column=4)

row_correct_label_vertical_1_turn_2 = Label(
    history_turn_2,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_1_turn_2.grid(row=4, column=0)

row_correct_label_vertical_2_turn_2 = Label(
    history_turn_2,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_2_turn_2.grid(row=4, column=1)

row_correct_label_vertical_3_turn_2 = Label(
    history_turn_2,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_3_turn_2.grid(row=4, column=2)


########################################################################################################################
history_turn_3 = Frame(window, height=550, width=700)
history_turn_3.place(x=425, y=70)


button_1_history_turn_3 = Label(
    history_turn_3,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_1_history_turn_3.grid(row=0, column=0)

button_2_history_turn_3 = Label(
    history_turn_3,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_2_history_turn_3.grid(row=0, column=1)

button_3_history_turn_3 = Label(
    history_turn_3,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_3_history_turn_3.grid(row=0, column=2)

button_4_history_turn_3 = Label(
    history_turn_3,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_4_history_turn_3.grid(row=1, column=0)

button_5_history_turn_3 = Label(
    history_turn_3,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_5_history_turn_3.grid(row=1, column=1)

button_6_history_turn_3 = Label(
    history_turn_3,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_6_history_turn_3.grid(row=1, column=2)

button_7_history_turn_3 = Label(
    history_turn_3,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_7_history_turn_3.grid(row=2, column=0)

button_8_history_turn_3 = Label(
    history_turn_3,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_8_history_turn_3.grid(row=2, column=1)

button_9_history_turn_3 = Label(
    history_turn_3,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_9_history_turn_3.grid(row=2, column=2)



correct_label_horizontal_1_turn_3 = Label(
    history_turn_3,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_1_turn_3.grid(row=0, column=3)

correct_label_horizontal_2_turn_3 = Label(
    history_turn_3,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_2_turn_3.grid(row=1, column=3)

correct_label_horizontal_3_turn_3 = Label(
    history_turn_3,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_3_turn_3.grid(row=2, column=3)

correct_label_vertical_1_turn_3 = Label(
    history_turn_3,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_1_turn_3.grid(row=3, column=0)

correct_label_vertical_2_turn_3 = Label(
    history_turn_3,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_2_turn_3.grid(row=3, column=1)

correct_label_vertical_3_turn_3 = Label(
    history_turn_3,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_3_turn_3.grid(row=3, column=2)


row_correct_label_horizontal_1_turn_3 = Label(
    history_turn_3,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_1_turn_3.grid(row=0, column=4)

row_correct_label_horizontal_2_turn_3 = Label(
    history_turn_3,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_2_turn_3.grid(row=1, column=4)

row_correct_label_horizontal_3_turn_3 = Label(
    history_turn_3,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_3_turn_3.grid(row=2, column=4)

row_correct_label_vertical_1_turn_3 = Label(
    history_turn_3,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_1_turn_3.grid(row=4, column=0)

row_correct_label_vertical_2_turn_3 = Label(
    history_turn_3,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_2_turn_3.grid(row=4, column=1)

row_correct_label_vertical_3_turn_3 = Label(
    history_turn_3,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_3_turn_3.grid(row=4, column=2)


########################################################################################################################
history_turn_4 = Frame(window, height=550, width=700)
history_turn_4.place(x=625, y=70)


button_1_history_turn_4 = Label(
    history_turn_4,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_1_history_turn_4.grid(row=0, column=0)

button_2_history_turn_4 = Label(
    history_turn_4,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_2_history_turn_4.grid(row=0, column=1)

button_3_history_turn_4 = Label(
    history_turn_4,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_3_history_turn_4.grid(row=0, column=2)

button_4_history_turn_4 = Label(
    history_turn_4,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_4_history_turn_4.grid(row=1, column=0)

button_5_history_turn_4 = Label(
    history_turn_4,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_5_history_turn_4.grid(row=1, column=1)

button_6_history_turn_4 = Label(
    history_turn_4,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_6_history_turn_4.grid(row=1, column=2)

button_7_history_turn_4 = Label(
    history_turn_4,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_7_history_turn_4.grid(row=2, column=0)

button_8_history_turn_4 = Label(
    history_turn_4,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_8_history_turn_4.grid(row=2, column=1)

button_9_history_turn_4 = Label(
    history_turn_4,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_9_history_turn_4.grid(row=2, column=2)



correct_label_horizontal_1_turn_4 = Label(
    history_turn_4,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_1_turn_4.grid(row=0, column=3)

correct_label_horizontal_2_turn_4 = Label(
    history_turn_4,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_2_turn_4.grid(row=1, column=3)

correct_label_horizontal_3_turn_4 = Label(
    history_turn_4,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_3_turn_4.grid(row=2, column=3)

correct_label_vertical_1_turn_4 = Label(
    history_turn_4,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_1_turn_4.grid(row=3, column=0)

correct_label_vertical_2_turn_4 = Label(
    history_turn_4,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_2_turn_4.grid(row=3, column=1)

correct_label_vertical_3_turn_4 = Label(
    history_turn_4,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_3_turn_4.grid(row=3, column=2)


row_correct_label_horizontal_1_turn_4 = Label(
    history_turn_4,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_1_turn_4.grid(row=0, column=4)

row_correct_label_horizontal_2_turn_4 = Label(
    history_turn_4,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_2_turn_4.grid(row=1, column=4)

row_correct_label_horizontal_3_turn_4 = Label(
    history_turn_4,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_3_turn_4.grid(row=2, column=4)

row_correct_label_vertical_1_turn_4 = Label(
    history_turn_4,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_1_turn_4.grid(row=4, column=0)

row_correct_label_vertical_2_turn_4 = Label(
    history_turn_4,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_2_turn_4.grid(row=4, column=1)

row_correct_label_vertical_3_turn_4 = Label(
    history_turn_4,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_3_turn_4.grid(row=4, column=2)


########################################################################################################################

history_turn_5 = Frame(window, height=550, width=700)
history_turn_5.place(x=25, y=300)


button_1_history_turn_5 = Label(
    history_turn_5,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_1_history_turn_5.grid(row=0, column=0)

button_2_history_turn_5 = Label(
    history_turn_5,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_2_history_turn_5.grid(row=0, column=1)

button_3_history_turn_5 = Label(
    history_turn_5,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_3_history_turn_5.grid(row=0, column=2)

button_4_history_turn_5 = Label(
    history_turn_5,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_4_history_turn_5.grid(row=1, column=0)

button_5_history_turn_5 = Label(
    history_turn_5,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_5_history_turn_5.grid(row=1, column=1)

button_6_history_turn_5 = Label(
    history_turn_5,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_6_history_turn_5.grid(row=1, column=2)

button_7_history_turn_5 = Label(
    history_turn_5,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_7_history_turn_5.grid(row=2, column=0)

button_8_history_turn_5 = Label(
    history_turn_5,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_8_history_turn_5.grid(row=2, column=1)

button_9_history_turn_5 = Label(
    history_turn_5,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_9_history_turn_5.grid(row=2, column=2)



correct_label_horizontal_1_turn_5 = Label(
    history_turn_5,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_1_turn_5.grid(row=0, column=3)

correct_label_horizontal_2_turn_5 = Label(
    history_turn_5,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_2_turn_5.grid(row=1, column=3)

correct_label_horizontal_3_turn_5 = Label(
    history_turn_5,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_3_turn_5.grid(row=2, column=3)

correct_label_vertical_1_turn_5 = Label(
    history_turn_5,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_1_turn_5.grid(row=3, column=0)

correct_label_vertical_2_turn_5 = Label(
    history_turn_5,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_2_turn_5.grid(row=3, column=1)

correct_label_vertical_3_turn_5 = Label(
    history_turn_5,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_3_turn_5.grid(row=3, column=2)


row_correct_label_horizontal_1_turn_5 = Label(
    history_turn_5,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_1_turn_5.grid(row=0, column=4)

row_correct_label_horizontal_2_turn_5 = Label(
    history_turn_5,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_2_turn_5.grid(row=1, column=4)

row_correct_label_horizontal_3_turn_5 = Label(
    history_turn_5,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_3_turn_5.grid(row=2, column=4)

row_correct_label_vertical_1_turn_5 = Label(
    history_turn_5,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_1_turn_5.grid(row=4, column=0)

row_correct_label_vertical_2_turn_5 = Label(
    history_turn_5,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_2_turn_5.grid(row=4, column=1)

row_correct_label_vertical_3_turn_5 = Label(
    history_turn_5,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_3_turn_5.grid(row=4, column=2)


########################################################################################################################

history_turn_6 = Frame(window, height=550, width=700)
history_turn_6.place(x=225, y=300)


button_1_history_turn_6 = Label(
    history_turn_6,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_1_history_turn_6.grid(row=0, column=0)

button_2_history_turn_6 = Label(
    history_turn_6,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_2_history_turn_6.grid(row=0, column=1)

button_3_history_turn_6 = Label(
    history_turn_6,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_3_history_turn_6.grid(row=0, column=2)

button_4_history_turn_6 = Label(
    history_turn_6,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_4_history_turn_6.grid(row=1, column=0)

button_5_history_turn_6 = Label(
    history_turn_6,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_5_history_turn_6.grid(row=1, column=1)

button_6_history_turn_6 = Label(
    history_turn_6,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_6_history_turn_6.grid(row=1, column=2)

button_7_history_turn_6 = Label(
    history_turn_6,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_7_history_turn_6.grid(row=2, column=0)

button_8_history_turn_6 = Label(
    history_turn_6,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_8_history_turn_6.grid(row=2, column=1)

button_9_history_turn_6 = Label(
    history_turn_6,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_9_history_turn_6.grid(row=2, column=2)



correct_label_horizontal_1_turn_6 = Label(
    history_turn_6,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_1_turn_6.grid(row=0, column=3)

correct_label_horizontal_2_turn_6 = Label(
    history_turn_6,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_2_turn_6.grid(row=1, column=3)

correct_label_horizontal_3_turn_6 = Label(
    history_turn_6,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_3_turn_6.grid(row=2, column=3)

correct_label_vertical_1_turn_6 = Label(
    history_turn_6,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_1_turn_6.grid(row=3, column=0)

correct_label_vertical_2_turn_6 = Label(
    history_turn_6,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_2_turn_6.grid(row=3, column=1)

correct_label_vertical_3_turn_6 = Label(
    history_turn_6,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_3_turn_6.grid(row=3, column=2)


row_correct_label_horizontal_1_turn_6 = Label(
    history_turn_6,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_1_turn_6.grid(row=0, column=4)

row_correct_label_horizontal_2_turn_6 = Label(
    history_turn_6,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_2_turn_6.grid(row=1, column=4)

row_correct_label_horizontal_3_turn_6 = Label(
    history_turn_6,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_3_turn_6.grid(row=2, column=4)

row_correct_label_vertical_1_turn_6 = Label(
    history_turn_6,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_1_turn_6.grid(row=4, column=0)

row_correct_label_vertical_2_turn_6 = Label(
    history_turn_6,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_2_turn_6.grid(row=4, column=1)

row_correct_label_vertical_3_turn_6 = Label(
    history_turn_6,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_3_turn_6.grid(row=4, column=2)


########################################################################################################################

history_turn_7 = Frame(window, height=550, width=700)
history_turn_7.place(x=425, y=300)


button_1_history_turn_7 = Label(
    history_turn_7,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_1_history_turn_7.grid(row=0, column=0)

button_2_history_turn_7 = Label(
    history_turn_7,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_2_history_turn_7.grid(row=0, column=1)

button_3_history_turn_7 = Label(
    history_turn_7,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_3_history_turn_7.grid(row=0, column=2)

button_4_history_turn_7 = Label(
    history_turn_7,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_4_history_turn_7.grid(row=1, column=0)

button_5_history_turn_7 = Label(
    history_turn_7,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_5_history_turn_7.grid(row=1, column=1)

button_6_history_turn_7 = Label(
    history_turn_7,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_6_history_turn_7.grid(row=1, column=2)

button_7_history_turn_7 = Label(
    history_turn_7,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_7_history_turn_7.grid(row=2, column=0)

button_8_history_turn_7 = Label(
    history_turn_7,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_8_history_turn_7.grid(row=2, column=1)

button_9_history_turn_7 = Label(
    history_turn_7,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_9_history_turn_7.grid(row=2, column=2)



correct_label_horizontal_1_turn_7 = Label(
    history_turn_7,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_1_turn_7.grid(row=0, column=3)

correct_label_horizontal_2_turn_7 = Label(
    history_turn_7,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_2_turn_7.grid(row=1, column=3)

correct_label_horizontal_3_turn_7 = Label(
    history_turn_7,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_3_turn_7.grid(row=2, column=3)

correct_label_vertical_1_turn_7 = Label(
    history_turn_7,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_1_turn_7.grid(row=3, column=0)

correct_label_vertical_2_turn_7 = Label(
    history_turn_7,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_2_turn_7.grid(row=3, column=1)

correct_label_vertical_3_turn_7 = Label(
    history_turn_7,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_3_turn_7.grid(row=3, column=2)


row_correct_label_horizontal_1_turn_7 = Label(
    history_turn_7,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_1_turn_7.grid(row=0, column=4)

row_correct_label_horizontal_2_turn_7 = Label(
    history_turn_7,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_2_turn_7.grid(row=1, column=4)

row_correct_label_horizontal_3_turn_7 = Label(
    history_turn_7,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_3_turn_7.grid(row=2, column=4)

row_correct_label_vertical_1_turn_7 = Label(
    history_turn_7,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_1_turn_7.grid(row=4, column=0)

row_correct_label_vertical_2_turn_7 = Label(
    history_turn_7,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_2_turn_7.grid(row=4, column=1)

row_correct_label_vertical_3_turn_7 = Label(
    history_turn_7,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_3_turn_7.grid(row=4, column=2)


########################################################################################################################

history_turn_8 = Frame(window, height=550, width=700)
history_turn_8.place(x=625, y=300)


button_1_history_turn_8 = Label(
    history_turn_8,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_1_history_turn_8.grid(row=0, column=0)

button_2_history_turn_8 = Label(
    history_turn_8,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_2_history_turn_8.grid(row=0, column=1)

button_3_history_turn_8 = Label(
    history_turn_8,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_3_history_turn_8.grid(row=0, column=2)

button_4_history_turn_8 = Label(
    history_turn_8,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_4_history_turn_8.grid(row=1, column=0)

button_5_history_turn_8 = Label(
    history_turn_8,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_5_history_turn_8.grid(row=1, column=1)

button_6_history_turn_8 = Label(
    history_turn_8,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_6_history_turn_8.grid(row=1, column=2)

button_7_history_turn_8 = Label(
    history_turn_8,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_7_history_turn_8.grid(row=2, column=0)

button_8_history_turn_8 = Label(
    history_turn_8,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_8_history_turn_8.grid(row=2, column=1)

button_9_history_turn_8 = Label(
    history_turn_8,
    height=2,
    width=4,
    bd=3,
    font=('Times', 10),
    relief=RAISED
)
button_9_history_turn_8.grid(row=2, column=2)



correct_label_horizontal_1_turn_8 = Label(
    history_turn_8,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_1_turn_8.grid(row=0, column=3)

correct_label_horizontal_2_turn_8 = Label(
    history_turn_8,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_2_turn_8.grid(row=1, column=3)

correct_label_horizontal_3_turn_8 = Label(
    history_turn_8,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='orange'
)
correct_label_horizontal_3_turn_8.grid(row=2, column=3)

correct_label_vertical_1_turn_8 = Label(
    history_turn_8,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_1_turn_8.grid(row=3, column=0)

correct_label_vertical_2_turn_8 = Label(
    history_turn_8,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_2_turn_8.grid(row=3, column=1)

correct_label_vertical_3_turn_8 = Label(
    history_turn_8,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='orange'
)
correct_label_vertical_3_turn_8.grid(row=3, column=2)


row_correct_label_horizontal_1_turn_8 = Label(
    history_turn_8,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_1_turn_8.grid(row=0, column=4)

row_correct_label_horizontal_2_turn_8 = Label(
    history_turn_8,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_2_turn_8.grid(row=1, column=4)

row_correct_label_horizontal_3_turn_8 = Label(
    history_turn_8,
    height=2,
    width=3,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    pady=2,
    bg='green'
)
row_correct_label_horizontal_3_turn_8.grid(row=2, column=4)

row_correct_label_vertical_1_turn_8 = Label(
    history_turn_8,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_1_turn_8.grid(row=4, column=0)

row_correct_label_vertical_2_turn_8 = Label(
    history_turn_8,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_2_turn_8.grid(row=4, column=1)

row_correct_label_vertical_3_turn_8 = Label(
    history_turn_8,
    height=1,
    width=4,
    bd=2,
    font=('Times', 8),
    relief=RAISED,
    padx=3,
    pady=2,
    bg='green'
)
row_correct_label_vertical_3_turn_8.grid(row=4, column=2)


button_1_history = [button_1_history_turn_1,
                    button_1_history_turn_2,
                    button_1_history_turn_3,
                    button_1_history_turn_4,
                    button_1_history_turn_5,
                    button_1_history_turn_6,
                    button_1_history_turn_7,
                    button_1_history_turn_8]

button_2_history = [button_2_history_turn_1,
                    button_2_history_turn_2,
                    button_2_history_turn_3,
                    button_2_history_turn_4,
                    button_2_history_turn_5,
                    button_2_history_turn_6,
                    button_2_history_turn_7,
                    button_2_history_turn_8]

button_3_history = [button_3_history_turn_1,
                    button_3_history_turn_2,
                    button_3_history_turn_3,
                    button_3_history_turn_4,
                    button_3_history_turn_5,
                    button_3_history_turn_6,
                    button_3_history_turn_7,
                    button_3_history_turn_8]

button_4_history = [button_4_history_turn_1,
                    button_4_history_turn_2,
                    button_4_history_turn_3,
                    button_4_history_turn_4,
                    button_4_history_turn_5,
                    button_4_history_turn_6,
                    button_4_history_turn_7,
                    button_4_history_turn_8]

button_5_history = [button_5_history_turn_1,
                    button_5_history_turn_2,
                    button_5_history_turn_3,
                    button_5_history_turn_4,
                    button_5_history_turn_5,
                    button_5_history_turn_6,
                    button_5_history_turn_7,
                    button_5_history_turn_8]

button_6_history = [button_6_history_turn_1,
                    button_6_history_turn_2,
                    button_6_history_turn_3,
                    button_6_history_turn_4,
                    button_6_history_turn_5,
                    button_6_history_turn_6,
                    button_6_history_turn_7,
                    button_6_history_turn_8]

button_7_history = [button_7_history_turn_1,
                    button_7_history_turn_2,
                    button_7_history_turn_3,
                    button_7_history_turn_4,
                    button_7_history_turn_5,
                    button_7_history_turn_6,
                    button_7_history_turn_7,
                    button_7_history_turn_8]

button_8_history = [button_8_history_turn_1,
                    button_8_history_turn_2,
                    button_8_history_turn_3,
                    button_8_history_turn_4,
                    button_8_history_turn_5,
                    button_8_history_turn_6,
                    button_8_history_turn_7,
                    button_8_history_turn_8]

button_9_history = [button_9_history_turn_1,
                    button_9_history_turn_2,
                    button_9_history_turn_3,
                    button_9_history_turn_4,
                    button_9_history_turn_5,
                    button_9_history_turn_6,
                    button_9_history_turn_7,
                    button_9_history_turn_8]

history_buttons = [button_1_history,
                   button_2_history,
                   button_3_history,
                   button_4_history,
                   button_5_history,
                   button_6_history,
                   button_7_history,
                   button_8_history,
                   button_9_history]

labels_history = [correct_label_vertical_1_turn_1,
                  correct_label_vertical_2_turn_1,
                  correct_label_vertical_3_turn_1,
                  correct_label_horizontal_1_turn_1,
                  correct_label_horizontal_2_turn_1,
                  correct_label_horizontal_3_turn_1,
                  row_correct_label_vertical_1_turn_1,
                  row_correct_label_vertical_2_turn_1,
                  row_correct_label_vertical_3_turn_1,
                  row_correct_label_horizontal_1_turn_1,
                  row_correct_label_horizontal_2_turn_1,
                  row_correct_label_horizontal_3_turn_1,
                  correct_label_vertical_1_turn_2,
                  correct_label_vertical_2_turn_2,
                  correct_label_vertical_3_turn_2,
                  correct_label_horizontal_1_turn_2,
                  correct_label_horizontal_2_turn_2,
                  correct_label_horizontal_3_turn_2,
                  row_correct_label_vertical_1_turn_2,
                  row_correct_label_vertical_2_turn_2,
                  row_correct_label_vertical_3_turn_2,
                  row_correct_label_horizontal_1_turn_2,
                  row_correct_label_horizontal_2_turn_2,
                  row_correct_label_horizontal_3_turn_2,
                  correct_label_vertical_1_turn_3,
                  correct_label_vertical_2_turn_3,
                  correct_label_vertical_3_turn_3,
                  correct_label_horizontal_1_turn_3,
                  correct_label_horizontal_2_turn_3,
                  correct_label_horizontal_3_turn_3,
                  row_correct_label_vertical_1_turn_3,
                  row_correct_label_vertical_2_turn_3,
                  row_correct_label_vertical_3_turn_3,
                  row_correct_label_horizontal_1_turn_3,
                  row_correct_label_horizontal_2_turn_3,
                  row_correct_label_horizontal_3_turn_3,
                  correct_label_vertical_1_turn_4,
                  correct_label_vertical_2_turn_4,
                  correct_label_vertical_3_turn_4,
                  correct_label_horizontal_1_turn_4,
                  correct_label_horizontal_2_turn_4,
                  correct_label_horizontal_3_turn_4,
                  row_correct_label_vertical_1_turn_4,
                  row_correct_label_vertical_2_turn_4,
                  row_correct_label_vertical_3_turn_4,
                  row_correct_label_horizontal_1_turn_4,
                  row_correct_label_horizontal_2_turn_4,
                  row_correct_label_horizontal_3_turn_4,
                  correct_label_vertical_1_turn_5,
                  correct_label_vertical_2_turn_5,
                  correct_label_vertical_3_turn_5,
                  correct_label_horizontal_1_turn_5,
                  correct_label_horizontal_2_turn_5,
                  correct_label_horizontal_3_turn_5,
                  row_correct_label_vertical_1_turn_5,
                  row_correct_label_vertical_2_turn_5,
                  row_correct_label_vertical_3_turn_5,
                  row_correct_label_horizontal_1_turn_5,
                  row_correct_label_horizontal_2_turn_5,
                  row_correct_label_horizontal_3_turn_5,
                  correct_label_vertical_1_turn_6,
                  correct_label_vertical_2_turn_6,
                  correct_label_vertical_3_turn_6,
                  correct_label_horizontal_1_turn_6,
                  correct_label_horizontal_2_turn_6,
                  correct_label_horizontal_3_turn_6,
                  row_correct_label_vertical_1_turn_6,
                  row_correct_label_vertical_2_turn_6,
                  row_correct_label_vertical_3_turn_6,
                  row_correct_label_horizontal_1_turn_6,
                  row_correct_label_horizontal_2_turn_6,
                  row_correct_label_horizontal_3_turn_6,
                  correct_label_vertical_1_turn_7,
                  correct_label_vertical_2_turn_7,
                  correct_label_vertical_3_turn_7,
                  correct_label_horizontal_1_turn_7,
                  correct_label_horizontal_2_turn_7,
                  correct_label_horizontal_3_turn_7,
                  row_correct_label_vertical_1_turn_7,
                  row_correct_label_vertical_2_turn_7,
                  row_correct_label_vertical_3_turn_7,
                  row_correct_label_horizontal_1_turn_7,
                  row_correct_label_horizontal_2_turn_7,
                  row_correct_label_horizontal_3_turn_7,
                  correct_label_vertical_1_turn_8,
                  correct_label_vertical_2_turn_8,
                  correct_label_vertical_3_turn_8,
                  correct_label_horizontal_1_turn_8,
                  correct_label_horizontal_2_turn_8,
                  correct_label_horizontal_3_turn_8,
                  row_correct_label_vertical_1_turn_8,
                  row_correct_label_vertical_2_turn_8,
                  row_correct_label_vertical_3_turn_8,
                  row_correct_label_horizontal_1_turn_8,
                  row_correct_label_horizontal_2_turn_8,
                  row_correct_label_horizontal_3_turn_8,
                  ]

restart_button = Button(window,
                        text='Restart',
                        font=('Times', 20),
                        bd=4,
                        command=restart
                        )
restart_button.place(x=350, y=475)

window.mainloop()
