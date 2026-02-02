import tkinter as tk
from tkinter import messagebox
from collections import Counter



def count():
    global counter
    counter += 1


def show():
    messagebox.showinfo("", "counter=" + str(counter) + ",state=" + str(switch1.get()))
    
    
def switch():
    if button_1.cget('state') == tk.DISABLED:
        button_1.config(state=tk.NORMAL)
        button_1.flash()
    else:
        button_1.flash()
        button_1.config(state=tk.DISABLED)
    

def mouseover(ev):
    button_1['bg'] = "green"


def mouseout(ev):
    button_1['bg'] = 'red' 
    


window = tk.Tk()
switch1 = tk.IntVar()
counter = 0

button_1 = tk.Button(window, text="Enabled", bg='red')
button_1.bind("<Enter>", mouseover)
button_1.bind("<Leave>", mouseout)
button_1.pack()

button_2 = tk.Button(window, text="Enable/Disable", command=switch)
button_2.pack()


button3 = tk.Button(window, text="Show", command=show)
button3.pack()
checkbutton = tk.Checkbutton(window, text="Tick", variable=switch1, command=count)
checkbutton.pack()

window.mainloop()