import tkinter as tk


def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


dummy = tk.Tk()    # we need this although we won't display any windows
variable = tk.StringVar()
variable.set("abc")
r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)

print("1")
variable.set(variable.get() + 'd')  # read followed by write
variable.trace_vdelete("r", r_obsid)

print("2")
variable.set(variable.get() + 'e')
variable.trace_vdelete("w", w_obsid)

print("3")
variable.set(variable.get() + 'f')
print(variable.get())
