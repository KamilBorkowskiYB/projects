import tkinter as tk

root = tk.Tk()
root.geometry('560x840')
root.title('Pizza Worth Calc')


def calculation():
    d = pizza_D_p1.get()
    p = pizza_price_p1.get()
    area = round((float(d)/2)*(float(d)/2)*3.14, 2)
    worth = round(area/(float(p)), 2)
    pizza_area_p1.config(state='normal')
    pizza_worth_p1.config(state='normal')
    pizza_area_p1.delete("1.0", "end")
    pizza_worth_p1.delete("1.0", "end")
    pizza_area_p1.insert(1.0, str(area))
    pizza_worth_p1.insert(1.0, str(worth))
    pizza_area_p1.config(state='disabled')
    pizza_worth_p1.config(state='disabled')
    pizza_area_p1.tag_configure("space", justify='center')
    pizza_area_p1.tag_add("space", "1.0", "end")
    pizza_worth_p1.tag_configure("space", justify='center')
    pizza_worth_p1.tag_add("space", "1.0", "end")

    d2 = pizza_D_p2.get()
    p2 = pizza_price_p2.get()
    area2 = round((float(d2)/2)*(float(d2)/2)*3.14, 2)
    worth2 = round(area2/(float(p2)), 2)
    pizza_area_p2.config(state='normal')
    pizza_worth_p2.config(state='normal')
    pizza_area_p2.delete("1.0", "end")
    pizza_worth_p2.delete("1.0", "end")
    pizza_area_p2.insert(1.0, str(area2))
    pizza_worth_p2.insert(1.0, str(worth2))
    pizza_area_p2.config(state='disabled')
    pizza_worth_p2.config(state='disabled')
    pizza_area_p2.tag_configure("space", justify='center')
    pizza_area_p2.tag_add("space", "1.0", "end")
    pizza_worth_p2.tag_configure("space", justify='center')
    pizza_worth_p2.tag_add("space", "1.0", "end")

    if worth > worth2:
        pizza_worth_p1.config(state='normal')
        pizza_worth_p1.configure(bg='green')
        pizza_worth_p2.config(state='normal')
        pizza_worth_p2.configure(bg='white')
        pizza_worth_p1.config(state='disabled')
        pizza_worth_p2.config(state='disabled')
        ratio = round((1-(worth2/worth))*100)
        calculation_result['text'] = 'Pizza 1 has better worth ratio by ' + str(ratio) + '%'
    elif worth2 > worth:
        pizza_worth_p1.config(state='normal')
        pizza_worth_p1.configure(bg='white')
        pizza_worth_p2.config(state='normal')
        pizza_worth_p2.configure(bg='green')
        pizza_worth_p1.config(state='disabled')
        pizza_worth_p2.config(state='disabled')
        ratio = round((1 - (worth / worth2)) * 100)
        calculation_result['text'] = 'Pizza 2 has better worth ratio by ' + str(ratio) + '%'
    frame_results.pack()
    print(root.winfo_height())


# frames
frame_D = tk.Frame(root)
frame_P = tk.Frame(root)
frame_A = tk.Frame(root)
frame_W = tk.Frame(root)
frame_results = tk.Frame(root)


# widgets
label_d = tk.Label(root, text="Diameter of pizza", font=("Arial", 24))
label_d_p1 = tk.Label(frame_D, text="1 pizza", font=("Arial", 14))
label_d_p2 = tk.Label(frame_D, text="2 pizza", font=("Arial", 14))
pizza_D_p1 = tk.Entry(frame_D, justify='center', width=10, font=("Arial", 24))
pizza_D_p2 = tk.Entry(frame_D, justify='center', width=10, font=("Arial", 24))
label_p = tk.Label(root, text="Pizza's price", font=("Arial", 24))
label_p_p1 = tk.Label(frame_P, text="1 pizza", font=("Arial", 14))
label_p_p2 = tk.Label(frame_P, text="2 pizza", font=("Arial", 14))
pizza_price_p1 = tk.Entry(frame_P, justify='center', width=10, font=("Arial", 24))
pizza_price_p2 = tk.Entry(frame_P, justify='center', width=10, font=("Arial", 24))
btn_calc = tk.Button(root, text="Calculate", command=lambda: calculation(), font=("Arial", 24), padx=50)
label_area = tk.Label(root, text="Pizza's area", font=("Arial", 24))
label_area_p1 = tk.Label(frame_A, text="1 pizza", font=("Arial", 14))
label_area_p2 = tk.Label(frame_A, text="2 pizza", font=("Arial", 14))
pizza_area_p1 = tk.Text(frame_A, height=1, width=10, state='disabled', font=("Arial", 24), pady=10, padx=10)
pizza_area_p2 = tk.Text(frame_A, height=1, width=10, state='disabled', font=("Arial", 24), pady=10, padx=10)
label_worth = tk.Label(root, text="Pizza's worth", font=("Arial", 24))
label_worth_p1 = tk.Label(frame_W, text="1 pizza", font=("Arial", 14))
label_worth_p2 = tk.Label(frame_W, text="2 pizza", font=("Arial", 14))
pizza_worth_p1 = tk.Text(frame_W, height=1, width=10, state='disabled', font=("Arial", 24), pady=10, padx=10)
pizza_worth_p2 = tk.Text(frame_W, height=1, width=10, state='disabled', font=("Arial", 24), pady=10, padx=10)
calculation_result = tk.Label(frame_results, text="Pizza # has better worth ratio by #", font=("Arial", 24), pady=50)

pad_y1 = 10
label_SPACE1 = tk.Label(root, text=" ", pady=pad_y1)
label_SPACE2 = tk.Label(root, text=" ", pady=pad_y1)
label_SPACE3 = tk.Label(root, text=" ", pady=pad_y1)
label_space1 = tk.Label(root, text=" ")
label_space2 = tk.Label(root, text=" ")

root.bind("<Return>", lambda e: calculation())

# pack
label_SPACE1.pack()
label_d.pack()
frame_D.pack()
label_d_p1.grid(row=0, column=0)
label_d_p2.grid(row=0, column=1)
pizza_D_p1.grid(row=1, column=0)
pizza_D_p2.grid(row=1, column=1)
label_space1.pack()
label_p.pack()
frame_P.pack()
label_p_p1.grid(row=0, column=0)
label_p_p2.grid(row=0, column=1)
pizza_price_p1.grid(row=1, column=0)
pizza_price_p2.grid(row=1, column=1)
label_SPACE2.pack()
btn_calc.pack()
label_SPACE3.pack()
label_area.pack()
frame_A.pack()
label_area_p1.grid(row=0, column=0)
label_area_p2.grid(row=0, column=1)
pizza_area_p1.grid(row=1, column=0)
pizza_area_p2.grid(row=1, column=1)
label_space2.pack()
label_worth.pack()
frame_W.pack()
label_worth_p1.grid(row=0, column=0)
label_worth_p2.grid(row=0, column=1)
pizza_worth_p1.grid(row=1, column=0)
pizza_worth_p2.grid(row=1, column=1)
frame_results.pack_forget()
calculation_result.pack()
root.mainloop()
