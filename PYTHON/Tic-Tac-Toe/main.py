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
            elif XorO == 0:
                b['text'] = 'O'
                moves += 1
                XorO = 1


def who_won(b):
    global play_on
    if b['text'] == 'O':
        print("O won")
        play_on = False
    if b['text'] == 'X':
        print("X won")
        play_on = False


def win():
    if (btn_1['text'] == btn_2['text'] == btn_3['text']) and btn_1['text'] != " ":
        who_won(btn_1)
    if (btn_1['text'] == btn_4['text'] == btn_7['text']) and btn_1['text'] != " ":
        who_won(btn_1)
    if (btn_1['text'] == btn_5['text'] == btn_9['text']) and btn_1['text'] != " ":
        who_won(btn_1)
    if (btn_2['text'] == btn_5['text'] == btn_8['text']) and btn_2['text'] != " ":
        who_won(btn_2)
    if (btn_3['text'] == btn_6['text'] == btn_9['text']) and btn_3['text'] != " ":
        who_won(btn_3)
    if (btn_3['text'] == btn_5['text'] == btn_7['text']) and btn_3['text'] != " ":
        who_won(btn_3)
    if (btn_4['text'] == btn_5['text'] == btn_6['text']) and btn_4['text'] != " ":
        who_won(btn_4)
    if (btn_7['text'] == btn_8['text'] == btn_9['text']) and btn_7['text'] != " ":
        who_won(btn_7)
    elif moves >= 9:
        print("Draw")


root = tk.Tk()
root.geometry('375x600')
root.title('Tic-Tac-Toe')

btn_1 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_1), win()], height=2, width=5, font=("Arial", 30))
btn_1.grid(row=0, column=0)
btn_2 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_2), win()], height=2, width=5, font=("Arial", 30))
btn_2.grid(row=0, column=1)
btn_3 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_3), win()], height=2, width=5, font=("Arial", 30))
btn_3.grid(row=0, column=2)
btn_4 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_4), win()], height=2, width=5, font=("Arial", 30))
btn_4.grid(row=1, column=0)
btn_5 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_5), win()], height=2, width=5, font=("Arial", 30))
btn_5.grid(row=1, column=1)
btn_6 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_6), win()], height=2, width=5, font=("Arial", 30))
btn_6.grid(row=1, column=2)
btn_7 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_7), win()], height=2, width=5, font=("Arial", 30))
btn_7.grid(row=2, column=0)
btn_8 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_8), win()], height=2, width=5, font=("Arial", 30))
btn_8.grid(row=2, column=1)
btn_9 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_9), win()], height=2, width=5, font=("Arial", 30))
btn_9.grid(row=2, column=2)
root.mainloop()
