import tkinter as tk
from tkinter import messagebox
import tkinter
from tomlkit.api import string


def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks")
    else:
        string = "x=" +str(event.x) + ",y=" + str(event.y) + \
                 ",num=" + str(event.num) + ",type=" + event.type
        tk.messagebox.showinfo("Click!", string)


def clicked():
    messagebox.showinfo("info", "some\nInfo")


def on_off():
    global switch
    if switch:
        button_2.config(command=lambda: None)
        button_2.config(text="Gee!")
    else:
        button_2.config(command=peekaboo)
        button_2.config(text="Peekabeoo!")
    switch = not switch
    

def peekaboo():
    messagebox.showinfo("", "PEEKABOO")
    

window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(window, text ="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=30)
entry.pack()

radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
radiobutton_2.pack()

button_i = tkinter.Button(window, text="show info", command=clicked)
button_i.pack()

button_i1 = tkinter.Button(window, text='Quit?', command=window.destroy)
button_i1.pack()


label_1 = tk.Label(window, text="Label")
label_1.bind("<Button-1>", click)
label_1.pack()

button_i2 = tk.Button(window, text="Button Text", command=click)
button_i2.pack(fill=tk.X)

frame_1 = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame_1.bind("<Button-1>", click)
frame_1.pack()

switch = True
button_1 = tkinter.Button(window, text="on/off", command=on_off)
button_1.pack()
button_2 = tkinter.Button(window, text="Peekaboo", command=peekaboo)
button_2.pack()

window.mainloop()
