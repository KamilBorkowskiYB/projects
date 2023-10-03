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
menu_line1 = ttk.Label(frame_start, text='You will answer 10 math question in a limited time', anchor="center")
menu_line2 = ttk.Label(frame_start, text='Are you ready?', anchor="center")
btn_play = ttk.Button(frame_start, text='Play', command=lambda: start_quiz())

# game widgets
question_label = ttk.Label(frame_game, text='Question 1')

# menu grid
frame_start.columnconfigure(0, weight=1)
frame_start.rowconfigure([0,1,2], weight=1)
frame_start.pack(expand=True,fill='both')
menu_line1.grid(row = 0, column = 0, sticky='nswe')
menu_line2.grid(row = 1, column = 0, sticky='nswe')
btn_play.grid(row = 2, column = 0, sticky='NSEW')

# game grid
frame_game.pack()
question_label.pack()
frame_game.pack_forget()
win.mainloop()
