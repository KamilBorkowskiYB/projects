import tkinter as tk
import ttkbootstrap as ttk

win = ttk.Window()
win.geometry('300x300')
win.title('Math Quiz')


def start_quiz():
    frame_start.pack_forget()
    frame_game.pack()


# frames
frame_start = ttk.Frame(win)
frame_game = ttk.Frame(win)

# start menu widgets
menu_line1 = ttk.Label(frame_start, text='Are you ready?')
btn_play = ttk.Button(frame_start, text='Play', command=lambda: start_quiz())

# game widgets
question_label = ttk.Label(frame_game, text='Question 1')

# grid
frame_start.pack()
menu_line1.pack()
btn_play.pack()

frame_game.pack()
question_label.pack()
frame_game.pack_forget()
win.mainloop()
