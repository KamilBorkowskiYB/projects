import tkinter as tk

# X=1 O=0
XorO = 1
moves = 0


def btn_state(b):
    global XorO
    global moves
    if b['text'] == " ":
        if XorO == 1:
            b['text'] = 'X'
            moves += 1
            XorO = 0
        elif XorO == 0:
            b['text'] = 'Y'
            moves += 1
            XorO = 1


def win():
    global moves
    if (btn_1['text'] == btn_2['text'] == btn_3['text']) and btn_1['text'] != " ":
        print("win")
    if (btn_1['text'] == btn_4['text'] == btn_7['text']) and btn_1['text'] != " ":
        print("win")
    if (btn_1['text'] == btn_5['text'] == btn_9['text']) and btn_1['text'] != " ":
        print("win")
    if (btn_2['text'] == btn_5['text'] == btn_8['text']) and btn_2['text'] != " ":
        print("win")
    if (btn_3['text'] == btn_6['text'] == btn_9['text']) and btn_3['text'] != " ":
        print("win")
    if (btn_3['text'] == btn_5['text'] == btn_7['text']) and btn_3['text'] != " ":
        print("win")
    if (btn_4['text'] == btn_5['text'] == btn_6['text']) and btn_4['text'] != " ":
        print("win")
    if (btn_7['text'] == btn_8['text'] == btn_9['text']) and btn_7['text'] != " ":
        print("win")
    if moves >= 9:
        print("draw")


root = tk.Tk()
root.geometry('300x300')
root.title('Tic-Tac-Toe')

btn_1 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_1), win()], width=5, font=("Arial", 14))
btn_1.grid(row=0, column=0)
btn_2 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_2), win()], width=5, font=("Arial", 14))
btn_2.grid(row=0, column=1)
btn_3 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_3), win()], width=5, font=("Arial", 14))
btn_3.grid(row=0, column=2)
btn_4 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_4), win()], width=5, font=("Arial", 14))
btn_4.grid(row=1, column=0)
btn_5 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_5), win()], width=5, font=("Arial", 14))
btn_5.grid(row=1, column=1)
btn_6 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_6), win()], width=5, font=("Arial", 14))
btn_6.grid(row=1, column=2)
btn_7 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_7), win()], width=5, font=("Arial", 14))
btn_7.grid(row=2, column=0)
btn_8 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_8), win()], width=5, font=("Arial", 14))
btn_8.grid(row=2, column=1)
btn_9 = tk.Button(root, text=" ", command=lambda: [btn_state(btn_9), win()], width=5, font=("Arial", 14))
btn_9.grid(row=2, column=2)
root.mainloop()
