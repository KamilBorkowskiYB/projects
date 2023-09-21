import tkinter as tk

root=tk.Tk()
root.geometry('600x600')
root.title('Pizza Worth Calc')

pizza_D = tk.Text(root,height=2, width=20, font=("Arial",24))
pizza_D.pack()
pizza_price = tk.Text(root,height=2, width=20, font=("Arial",24))
pizza_price.pack()


root.mainloop()