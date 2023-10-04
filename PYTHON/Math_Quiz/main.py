import tkinter as tk
import ttkbootstrap as ttk

win = ttk.Window()
win.geometry('900x900')
win.title('Math Quiz')


def start_quiz():
    frame_start.pack_forget()
    frame_game.pack(expand=True, fill='both')


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
next_question = ttk.Button(frame_game, text='Next Question')

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
