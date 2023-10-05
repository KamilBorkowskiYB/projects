import tkinter as tk
import ttkbootstrap as ttk
import random

win = ttk.Window()
win.geometry('900x900')
win.title('Math Quiz')

question_number = 2
good_answers = 0


def start_quiz():
    frame_start.pack_forget()
    frame_game.pack(expand=True, fill='both')


def submit_answer():
    global question_number
    if question_number < 11:
        question_label['text'] = 'Question ' + str(question_number)
        question_number += 1
    get_equation()

def get_equation():
    # 1 = +     2 = -   3 = *   4 = /
    operation = random.randint(1,4)
    if operation == 1:
        x = random.randint(1, 256)
        y = random.randint(0, 256)
        w = x+y
        operation_symbol = '+'
    if operation == 2:
        x = random.randint(1, 256)
        y = random.randint(0, 256)
        w = x-y
        operation_symbol = '-'
    if operation == 3:
        x = random.randint(1, 16)
        y = random.randint(0, 16)
        w = x*y
        operation_symbol = '*'
    if operation == 4:
        x = random.randint(12, 150)
        y = random.randint(2, 12)
        while x % y != 0:
            y = random.randint(2, 12)
        w = x/y
        operation_symbol = '/'
    equation_label['text'] = str(x) + operation_symbol + str(y)
    print(operation)
    print(x)
    print(y)


# frames
frame_start = ttk.Frame(win)
frame_game = ttk.Frame(win)

# styles
style = ttk.Style()
style.configure('.', font=('Helvetica', 48))
style.configure('my.TButton', font=('Helvetica', 150))

# start menu widgets
menu_line1 = ttk.Label(frame_start, text='You will answer 10 math\nquestion in a limited time.\nAre you ready?', anchor="center", justify="center")
btn_play = ttk.Button(frame_start, text='Play', command=lambda: start_quiz(), style='my.TButton')

# game widgets
question_label = ttk.Label(frame_game, text='Question 1')
equation_label = ttk.Label(frame_game, text='Equation 1')
answer_entry = ttk.Entry(frame_game)
next_question = ttk.Button(frame_game, text='Next Question', command=lambda: submit_answer())

# menu grid
frame_start.columnconfigure(0, weight=1)
frame_start.rowconfigure([0,1], weight=1)
frame_start.pack(expand=True,fill='both')
menu_line1.grid(row = 0, column = 0, sticky='nswe')
btn_play.grid(row = 1, column = 0, sticky='NSEW')

# game grid
frame_game.pack(expand=True)
question_label.pack(pady=(50,0))
equation_label.pack()
next_question.pack(side='bottom',pady=(0,90))
answer_entry.pack(side='bottom')
frame_game.pack_forget()
win.mainloop()
