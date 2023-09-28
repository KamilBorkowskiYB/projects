import tkinter as tk

# X=1 O=0
XorO = 1
moves = 0
play_on = True


def btn_state(b):
    global XorO
    global moves
    global play_on
    if play_on is True:
        if b['text'] == " ":
            if XorO == 1:
                b['text'] = 'X'
                moves += 1
                XorO = 0
                info['text'] = 'O on move'
            elif XorO == 0:
                b['text'] = 'O'
                moves += 1
                XorO = 1
                info['text'] = 'X on move'


def who_won(b):
    global play_on
    if b['text'] == 'O':
        info['text'] = 'O won'
        play_on = False
    if b['text'] == 'X':
        info['text'] = 'X won'
        play_on = False


def win():
    if (btn_1['text'] == btn_2['text'] == btn_3['text']) and btn_1['text'] != " ":
        btn_1.config(bg='red')
        btn_2.config(bg='red')
        btn_3.config(bg='red')
        who_won(btn_1)
    if (btn_1['text'] == btn_4['text'] == btn_7['text']) and btn_1['text'] != " ":
        btn_1.config(bg='red')
        btn_4.config(bg='red')
        btn_7.config(bg='red')
        who_won(btn_1)
    if (btn_1['text'] == btn_5['text'] == btn_9['text']) and btn_1['text'] != " ":
        btn_1.config(bg='red')
        btn_5.config(bg='red')
        btn_9.config(bg='red')
        who_won(btn_1)
    if (btn_2['text'] == btn_5['text'] == btn_8['text']) and btn_2['text'] != " ":
        btn_2.config(bg='red')
        btn_5.config(bg='red')
        btn_8.config(bg='red')
        who_won(btn_2)
    if (btn_3['text'] == btn_6['text'] == btn_9['text']) and btn_3['text'] != " ":
        btn_3.config(bg='red')
        btn_6.config(bg='red')
        btn_9.config(bg='red')
        who_won(btn_3)
    if (btn_3['text'] == btn_5['text'] == btn_7['text']) and btn_3['text'] != " ":
        btn_3.config(bg='red')
        btn_5.config(bg='red')
        btn_7.config(bg='red')
        who_won(btn_3)
    if (btn_4['text'] == btn_5['text'] == btn_6['text']) and btn_4['text'] != " ":
        btn_4.config(bg='red')
        btn_5.config(bg='red')
        btn_6.config(bg='red')
        who_won(btn_4)
    if (btn_7['text'] == btn_8['text'] == btn_9['text']) and btn_7['text'] != " ":
        btn_7.config(bg='red')
        btn_8.config(bg='red')
        btn_9.config(bg='red')
        who_won(btn_7)
    elif moves >= 9:
        info['text'] = 'Draw'


def reset():
    global moves
    global play_on
    global XorO
    moves = 0
    play_on = True
    XorO = 1
    info['text'] = "X on move"
    btn_1.config(bg='white', text=" ")
    btn_2.config(bg='white', text=" ")
    btn_3.config(bg='white', text=" ")
    btn_4.config(bg='white', text=" ")
    btn_5.config(bg='white', text=" ")
    btn_6.config(bg='white', text=" ")
    btn_7.config(bg='white', text=" ")
    btn_8.config(bg='white', text=" ")
    btn_9.config(bg='white', text=" ")


root = tk.Tk()
root.geometry('375x600')
root.title('Tic-Tac-Toe')

game_frame = tk.Frame(root)
game_frame.pack()

btn_1 = tk.Button(game_frame, text=" ", command=lambda: [btn_state(btn_1), win()], height=2, width=5, font=("Arial", 30))
btn_1.grid(row=0, column=0)
btn_2 = tk.Button(game_frame, text=" ", command=lambda: [btn_state(btn_2), win()], height=2, width=5, font=("Arial", 30))
btn_2.grid(row=0, column=1)
btn_3 = tk.Button(game_frame, text=" ", command=lambda: [btn_state(btn_3), win()], height=2, width=5, font=("Arial", 30))
btn_3.grid(row=0, column=2)
btn_4 = tk.Button(game_frame, text=" ", command=lambda: [btn_state(btn_4), win()], height=2, width=5, font=("Arial", 30))
btn_4.grid(row=1, column=0)
btn_5 = tk.Button(game_frame, text=" ", command=lambda: [btn_state(btn_5), win()], height=2, width=5, font=("Arial", 30))
btn_5.grid(row=1, column=1)
btn_6 = tk.Button(game_frame, text=" ", command=lambda: [btn_state(btn_6), win()], height=2, width=5, font=("Arial", 30))
btn_6.grid(row=1, column=2)
btn_7 = tk.Button(game_frame, text=" ", command=lambda: [btn_state(btn_7), win()], height=2, width=5, font=("Arial", 30))
btn_7.grid(row=2, column=0)
btn_8 = tk.Button(game_frame, text=" ", command=lambda: [btn_state(btn_8), win()], height=2, width=5, font=("Arial", 30))
btn_8.grid(row=2, column=1)
btn_9 = tk.Button(game_frame, text=" ", command=lambda: [btn_state(btn_9), win()], height=2, width=5, font=("Arial", 30))
btn_9.grid(row=2, column=2)

info = tk.Label(root, text="X on move", font=("Arial", 30), pady=30)
info.pack()
btn_res = tk.Button(root, text="Restart", command=lambda: reset(), width=10, font=("Arial", 24))
btn_res.pack()
root.mainloop()
