import tkinter as tk

root = tk.Tk()
root.geometry('300x600')
root.title('Pizza Worth Calc')


def calculation():
    d = pizza_D.get()
    p = pizza_price.get()
    area = (float(d)/2)*(float(d)/2)*3.14
    worth = area/(float(p))
    pizza_area.config(state='normal')
    pizza_worth.config(state='normal')
    pizza_area.delete("1.0", "end")
    pizza_worth.delete("1.0", "end")
    pizza_area.insert(1.0, str(area))
    pizza_worth.insert(1.0, str(worth))
    pizza_area.config(state='disabled')
    pizza_worth.config(state='disabled')
    print(area)
    print(worth)
    pizza_area.tag_configure("space", justify='center')
    pizza_area.tag_add("space", "1.0", "end")
    pizza_worth.tag_configure("space", justify='center')
    pizza_worth.tag_add("space", "1.0", "end")


# widgets
label_d = tk.Label(root, text="Diameter of pizza", font=("Arial", 14))
pizza_D = tk.Entry(root, justify='center', width=10, font=("Arial", 24))
label_p = tk.Label(root, text="Pizza's price", font=("Arial", 14))
pizza_price = tk.Entry(root, justify='center', width=10, font=("Arial", 24))
btn_calc = tk.Button(root, text="Calculate", command=lambda: calculation(), font=("Arial", 24), padx=50)
label_area = tk.Label(root, text="Pizza's area", font=("Arial", 14))
pizza_area = tk.Text(root, height=1, width=10, state='disabled', font=("Arial", 24), pady=10, padx=10)
label_worth = tk.Label(root, text="Pizza's worth", font=("Arial", 14))
pizza_worth = tk.Text(root, height=1, width=10, state='disabled', font=("Arial", 24), pady=10, padx=10)

pad_y1 = 10
label_SPACE1 = tk.Label(root, text=" ", pady=pad_y1)
label_SPACE2 = tk.Label(root, text=" ", pady=pad_y1)
label_SPACE3 = tk.Label(root, text=" ", pady=pad_y1)
label_space1 = tk.Label(root, text=" ")
label_space2 = tk.Label(root, text=" ")

# pack
label_SPACE1.pack()
label_d.pack()
pizza_D.pack()
label_space1.pack()
label_p.pack()
pizza_price.pack()
label_SPACE2.pack()
btn_calc.pack()
label_SPACE3.pack()
label_area.pack()
pizza_area.pack()
label_space2.pack()
label_worth.pack()
pizza_worth.pack()
root.mainloop()
