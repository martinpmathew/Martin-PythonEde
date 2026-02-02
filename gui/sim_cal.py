from tkinter import *
from tkinter import messagebox


def print_result():
    result = 0
    if value3.get() == "+":
       result = value1.get() + value2.get()
    elif value3.get() == "-":
        result = value1.get() - value2.get()
    elif value3.get() == "*":
        result = value1.get() * value2.get()
    elif value3.get() == "/":
        result = value1.get() / value2.get()
    
    messagebox.showinfo("Result", str(value1.get()) + " " + str(value3.get()) + " " + str(value2.get()) + " = " + str(result)) 


def set_value3():
    if rb1.cget('state') == True:
        value3 = "+"
    elif rb2.cget('state') == True:
        value3 = "+"
    elif rb3.cget('state') == True:
        value3 = "*"
    elif rb4.cget('state') == True:
        value3 = "/"        
    
def check_val():
    pass


# Write your code here.
window = Tk()

value1 = IntVar()
value1.set(2)
value2 = IntVar()
value2.set(2)
value3 = StringVar()


rb1 = Radiobutton(window, text='+', variable=value3, value='+', command=set_value3)
rb1.select()
rb2 = Radiobutton(window, text='-', variable=value3, value='-', command=set_value3)
rb2.deselect()
rb3 = Radiobutton(window, text='*', variable=value3, value='*', command=set_value3)
rb3.deselect()
rb4 = Radiobutton(window, text='/', variable=value3, value='/', command=set_value3)
rb4.deselect()

ey1 = Entry(window)
ey2 = Entry(window)

bn = Button(window, text="Evaluate", command=print_result)

ey1.grid(column=1, row=2)
rb1.grid(column=2, row=1)
rb2.grid(column=2, row=2)
rb3.grid(column=2, row=3)
rb4.grid(column=2, row=4)
ey2.grid(column=3, row=2)
bn.grid(column=2, row=5)

window.mainloop()
