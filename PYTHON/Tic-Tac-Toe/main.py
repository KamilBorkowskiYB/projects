import tkinter as tk

XorO=1

def btn_state():
    global XorO
    if (tk.Button['text']==" "):
        if XorO==1:
            tk.Button['text']='X'
        elif XorO==0:
            tk.Button['text']='Y'

def test():
    global XorO
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            if (widget['text'] == " "):
                if XorO == 1:
                    widget['text'] = 'X'
                elif XorO == 0:
                    widget['text'] = 'Y'

root = tk.Tk()
root.geometry('300x300')
root.title('Tic-Tac-Toe')

btn_1 = tk.Button(root, text=" ", command=lambda: btn_state(), width=5, font=("Arial", 14))
btn_1.grid(row=0,column=0)
btn_2 = tk.Button(root, text=" ", command=lambda: test(), width=5, font=("Arial", 14))
btn_2.grid(row=0,column=1)
btn_3 = tk.Button(root, text=" ", width=5, font=("Arial", 14))
btn_3.grid(row=0,column=2)
btn_4 = tk.Button(root, text=" ", width=5, font=("Arial", 14))
btn_4.grid(row=1,column=0)
btn_5 = tk.Button(root, text=" ", width=5, font=("Arial", 14))
btn_5.grid(row=1,column=1)
btn_6 = tk.Button(root, text=" ", width=5, font=("Arial", 14))
btn_6.grid(row=1,column=2)
btn_7 = tk.Button(root, text=" ", width=5, font=("Arial", 14))
btn_7.grid(row=2,column=0)
btn_8 = tk.Button(root, text=" ", width=5, font=("Arial", 14))
btn_8.grid(row=2,column=1)
btn_9 = tk.Button(root, text=" ", width=5, font=("Arial", 14))
btn_9.grid(row=2,column=2)
root.mainloop()

