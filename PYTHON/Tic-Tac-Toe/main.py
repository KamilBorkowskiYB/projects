import tkinter as tk

# X=1 O=0
XorO = 1


def btn_state(b):
    global XorO
    if b['text'] == " ":
        if XorO == 1:
            b['text'] = 'X'
            XorO = 0
        elif XorO == 0:
            b['text'] = 'Y'
            XorO = 1


root = tk.Tk()
root.geometry('300x300')
root.title('Tic-Tac-Toe')

btn_1 = tk.Button(root, text=" ", command=lambda: btn_state(btn_1), width=5, font=("Arial", 14))
btn_1.grid(row=0, column=0)
btn_2 = tk.Button(root, text=" ", command=lambda: btn_state(btn_2), width=5, font=("Arial", 14))
btn_2.grid(row=0, column=1)
btn_3 = tk.Button(root, text=" ", command=lambda: btn_state(btn_3), width=5, font=("Arial", 14))
btn_3.grid(row=0, column=2)
btn_4 = tk.Button(root, text=" ", command=lambda: btn_state(btn_4), width=5, font=("Arial", 14))
btn_4.grid(row=1, column=0)
btn_5 = tk.Button(root, text=" ", command=lambda: btn_state(btn_5), width=5, font=("Arial", 14))
btn_5.grid(row=1, column=1)
btn_6 = tk.Button(root, text=" ", command=lambda: btn_state(btn_6), width=5, font=("Arial", 14))
btn_6.grid(row=1, column=2)
btn_7 = tk.Button(root, text=" ", command=lambda: btn_state(btn_7), width=5, font=("Arial", 14))
btn_7.grid(row=2, column=0)
btn_8 = tk.Button(root, text=" ", command=lambda: btn_state(btn_8), width=5, font=("Arial", 14))
btn_8.grid(row=2, column=1)
btn_9 = tk.Button(root, text=" ", command=lambda: btn_state(btn_9), width=5, font=("Arial", 14))
btn_9.grid(row=2, column=2)
root.mainloop()
