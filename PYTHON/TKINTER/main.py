import tkinter as tk

calculation = ""
btn_width = 5
font_size = 14
calc_size = 24

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_resoult.delete(1.0, "end")
    text_resoult.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_resoult.delete(1.0, "end")
        text_resoult.insert(1.0, calculation)
    except:
        clear_field()
        text_resoult.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_resoult.delete(1.0, "end")

def lay_size1():
    window.geometry('300x350')
    global btn_width
    global font_size
    global calc_size
    btn_width = 5
    font_size = 14
    calc_size = 24
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(font=("Arial", font_size))
    text_resoult.config(font=("Arial", calc_size))


def lay_size2():
    window.geometry('505x600')
    global btn_width
    global font_size
    global calc_size
    btn_width = 7
    font_size = 28
    calc_size = 42
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(font=("Arial", font_size))
    text_resoult.config(font=("Arial", calc_size))


def lay_size3():
    window.geometry('700x800')
    global btn_width
    global font_size
    global calc_size
    btn_width = 10
    font_size = 40
    calc_size = 57
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(font=("Arial", font_size))
    text_resoult.config(font=("Arial", calc_size))


window = tk.Tk()
window.geometry('300x350')
window.title("Calculator with tkinter")

text_resoult = tk.Text(window, height=2, width=16, font=("Arial", calc_size))
text_resoult.grid(columnspan=5)

btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1), width=btn_width, font=("Arial", font_size))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(window, text="2", command=lambda: add_to_calculation(2), width=btn_width, font=("Arial", font_size))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(window, text="3", command=lambda: add_to_calculation(3), width=btn_width, font=("Arial", font_size))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(window, text="4", command=lambda: add_to_calculation(4), width=btn_width, font=("Arial", font_size))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(window, text="5", command=lambda: add_to_calculation(5), width=btn_width, font=("Arial", font_size))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(window, text="6", command=lambda: add_to_calculation(6), width=btn_width, font=("Arial", font_size))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(window, text="7", command=lambda: add_to_calculation(7), width=btn_width, font=("Arial", font_size))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(window, text="8", command=lambda: add_to_calculation(8), width=btn_width, font=("Arial", font_size))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(window, text="9", command=lambda: add_to_calculation(9), width=btn_width, font=("Arial", font_size))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(window, text="0", command=lambda: add_to_calculation(0), width=btn_width, font=("Arial", font_size))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(window, text="+", command=lambda: add_to_calculation('+'), width=btn_width, font=("Arial", font_size))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(window, text="-", command=lambda: add_to_calculation('-'), width=btn_width, font=("Arial", font_size))
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(window, text="*", command=lambda: add_to_calculation('*'), width=btn_width, font=("Arial", font_size))
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(window, text="/", command=lambda: add_to_calculation('/'), width=btn_width, font=("Arial", font_size))
btn_div.grid(row=5, column=4)
btn_open = tk.Button(window, text="(", command=lambda: add_to_calculation('('), width=btn_width, font=("Arial", font_size))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(window, text=")", command=lambda: add_to_calculation(')'), width=btn_width, font=("Arial", font_size))
btn_close.grid(row=5, column=3)
btn_equal = tk.Button(window, text="=", command=lambda: evaluate_calculation(), width=btn_width*2+1, font=("Arial", font_size))
btn_equal.grid(row=6, column=3, columnspan=2)
btn_clear = tk.Button(window, text="Clear", command=lambda: clear_field(), width=btn_width*2+1, font=("Arial", font_size))
btn_clear.grid(row=6, column=1, columnspan=2)

btn_size1 = tk.Button(window, text="Size1", command=lambda: lay_size1(), width=7, font=("Arial", font_size))
btn_size1.grid(row=7, column=1, columnspan=2, sticky="W")
btn_size2 = tk.Button(window, text="Size2", command=lambda: lay_size2(), width=7, font=("Arial", font_size))
btn_size2.grid(row=7, column=2, columnspan=2)
btn_size3 = tk.Button(window, text="Size3", command=lambda: lay_size3(), width=7, font=("Arial", font_size))
btn_size3.grid(row=7, column=3, columnspan=2, sticky="E")
window.mainloop()
