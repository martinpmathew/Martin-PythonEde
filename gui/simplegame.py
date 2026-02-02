from tkinter import *
import random

def move_to_next(event=None):
    global i, j, button
    button.destroy()
    if i.get() > 400:
        i.set(1)
    else:
        i.set(i.get() + 1)
    
    if i.get() > 400:
        j.set(1)
    else:
        j.set(j.get() + 1)
    button = Button(window, text="Catch me")
    button.place(x=i.get(), y=j.get())
    button.bind("<Enter>", move_to_next)

# Write your code here.
window = Tk()
i = IntVar()
i.set(1)
j = IntVar()
j.set(1)
window.title("Simple Game")
window.minsize(500, 500)
button = Button(window, text="Catch me")
button.place(x=i.get(), y=j.get())
button.bind("<Enter>", move_to_next)

window.mainloop()


# Objectives
# Learn practical skills related to:
#
# using screen coordinates,
# managing widgets with the place manager,
# binding events using the bind() method.
# Scenario
# Write a simple game - an infinite game which humans cannot win. Here are the rules:
#
# the game goes on between TkInter and the user (probably you)
# TkInter opens a 500x500 pixel window and places a button saying "Catch me!" in the top-left corner of the window;
# if the user moves the mouse cursor over the button, the button immediately jumps to another location inside the window; you have to assure that the new location is distant enough to prevent the user from making an instant click,
# the button must not cross the window's boundaries during the jump!
# Here is a sample picture for your reference:
#
# Catch me if you can - reference
#
#
# Use the place() method to move the button, and the bind() method to assign your own callback.

