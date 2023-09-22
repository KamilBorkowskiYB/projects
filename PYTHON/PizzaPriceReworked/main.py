import tkinter as tk

root=tk.Tk()
root.geometry('600x600')
root.title('Pizza Worth Calc')

label_d = tk.Label(root,text = "Diameter of pizza")
label_d.pack()
pizza_D = tk.Text(root,height=2, width=20, font=("Arial",24))
pizza_D.pack()
label_p = tk.Label(root, text = "Pizza's price")
label_p.pack()
pizza_price = tk.Text(root,height=2, width=20, font=("Arial",24))
pizza_price.pack()
btn_calc = tk.Button(root, text="Calculate")
btn_calc.pack()


root.mainloop()