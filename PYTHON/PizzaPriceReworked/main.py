import tkinter as tk

root=tk.Tk()
root.geometry('600x600')
root.title('Pizza Worth Calc')

def calculation():
    d = pizza_D.get(1.0, "end-1c")
    p = pizza_price.get(1.0, "end-1c")
    area = (float(d)/2)*(float(d)/2)*3.14
    worth = area/(float(p))
    print(area)
    print(worth)
    print(float(d)+float(p))

label_d = tk.Label(root,text = "Diameter of pizza")
label_d.pack()
pizza_D = tk.Text(root,height=2, width=20, font=("Arial",24))
pizza_D.pack()
label_p = tk.Label(root, text = "Pizza's price")
label_p.pack()
pizza_price = tk.Text(root,height=2, width=20, font=("Arial",24))
pizza_price.pack()
btn_calc = tk.Button(root, text="Calculate", command=lambda: calculation())
btn_calc.pack()


root.mainloop()