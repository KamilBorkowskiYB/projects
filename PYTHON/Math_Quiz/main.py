import tkinter as tk
import ttkbootstrap as ttk
import random
import time
import threading as th

win = ttk.Window()
win.geometry('900x900')
win.title('Math Quiz')

question_number = 2
good_answers = 0
answer = 0
quiz_time = 70


def start_quiz():
    frame_start.pack_forget()
    frame_game.place(x=0, y=0, relwidth=0.75, relheight=1)
    frame_timer.place(relx=0.75, y=0, relwidth=0.25, relheight=1)
    timer_thread.start()
    answer_entry.focus()
    get_equation()
    win.unbind('<Return>')


def submit_answer():
    global question_number
    global good_answers
    if question_number <= 10:
        question_label['text'] = 'Question ' + str(question_number)
        question_number += 1
        check_equation()
        get_equation()
    else:
        print('--------')
        print(good_answers)
    answer_entry.delete(0, 'end')
    answer_entry.focus()


def get_equation():
    # 1 = +     2 = -   3 = *   4 = /
    global answer
    operation = random.randint(1, 4)
    if operation == 1:
        x = random.randint(1, 256)
        y = random.randint(0, 256)
        answer = x+y
        operation_symbol = '+'
    elif operation == 2:
        x = random.randint(1, 256)
        y = random.randint(0, 256)
        answer = x-y
        operation_symbol = '-'
    elif operation == 3:
        x = random.randint(1, 16)
        y = random.randint(0, 16)
        answer = x*y
        operation_symbol = '*'
    else:
        x = random.randint(12, 150)
        while not prime(x):
            x = random.randint(12, 150)
        y = random.randint(2, 12)
        while x % y != 0:
            y = random.randint(2, 12)
        answer = x/y
        operation_symbol = '/'
    equation_label['text'] = str(x) + operation_symbol + str(y)


def prime(x):
    for i in range(2, 12):
        if x % i == 0:
            return True
    return False


def check_equation():
    global answer
    global good_answers
    if len(answer_entry.get()) == 0:
        pass
    elif int(answer_entry.get()) == answer:
        good_answers += 1


def count_down():
    global quiz_time
    progress_bar_top['value'] = quiz_time
    for x in range(quiz_time, -1, -1):
        seconds = x % 60
        minutes = int(x/60) % 60
        timer_label['text']=f"{minutes:02}:{seconds:02}"
        progress()
        time.sleep(1)


def progress():
    progress_bar_top['value'] -= 1


# threads
timer_thread = th.Thread(target=count_down)

# frames
frame_start = ttk.Frame(win)
frame_game = ttk.Frame(win)
frame_timer = ttk.Frame(win)

# styles
style = ttk.Style()
style.configure('.', font=('Helvetica', 48))
style.configure('my.TButton', font=('Helvetica', 150))

# start menu widgets
menu_line1 = ttk.Label(frame_start, text='You will answer 10 math\nquestion in a limited time.\nAre you ready?', anchor="center", justify="center")
btn_play = ttk.Button(frame_start, text='Play', command=lambda: start_quiz(), style='my.TButton')

# game widgets
question_label = ttk.Label(frame_game, text='Question 1', anchor="center")
equation_label = ttk.Label(frame_game, text='Equation 1', anchor="center", font=('Helvetica', 100))
answer_entry = ttk.Entry(frame_game, justify="center", font=('Helvetica', 48))
next_question = ttk.Button(frame_game, text='Next Question', command=lambda: submit_answer())

# timer widgets
timer_label = ttk.Label(frame_timer, text='Time left', anchor='center')
timer_help_label = ttk.Label(frame_timer, background='red')
progress_bar_top = ttk.Progressbar(frame_timer, orient='vertical', mode='determinate', style='success', maximum=quiz_time)

# menu grid
frame_start.columnconfigure(0, weight=1)
frame_start.rowconfigure([0,1], weight=1)
frame_start.pack(expand=True, fill='both')
menu_line1.grid(row=0, column=0, sticky='NSEW')
btn_play.grid(row=1, column=0, sticky='NSEW', padx=100, pady=(0, 100))

# game grid
frame_game.columnconfigure(0, weight=1)
frame_game.rowconfigure([0,1,2,3], weight=1)
frame_game.place(x=0,y=0, relwidth=0.3,relheight=1)
question_label.grid(row=0, column=0, sticky='NSEW', pady=(50, 0), padx=(50, 50))
equation_label.grid(row=1, column=0, sticky='NSEW', pady=(0, 0), padx=(50, 50))
answer_entry.grid(row=2, column=0, sticky='NSEW', pady=50, padx=(50, 50))
next_question.grid(row=3, column=0, sticky='NSEW', pady=(0, 50), padx=(50, 50))
frame_game.place_forget()

# timer grid
frame_timer.columnconfigure(0, weight=1)
frame_timer.rowconfigure([0,1], weight=1)
frame_timer.place()
#timer_label.pack(expand= True, fill = 'both')
#timer_help_label.grid(row =0, column=0, sticky='NSEW')
progress_bar_top.grid(row =0, column=0, sticky='NSEW')
progress_bar_top['value'] = 100
timer_label.grid(row =1, column=0, sticky='NSEW')
frame_timer.place_forget()

# binds
win.bind("<Return>", lambda e: start_quiz())
frame_game.bind("<Return>", lambda e: submit_answer())
answer_entry.bind("<Return>", lambda e: submit_answer())

win.mainloop()
