import tkinter as tk
from tkinter import messagebox


def to_string(x):
    return "Current counter\nvalue is:\n" + str(x)


def plus():
    global counter
    counter += 1
    text.set(to_string(counter))


def do_it_again():
    text1.set(text1.get() + "and again...")


def digits_only(*args):
    global last_string
    string = text2.get()
    if string == '' or string.isdigit():  # Field's content is valid.
        last_string = string
    else:
        text2.set(last_string)


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")
    

def are_you_sure(event=None):
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()


def open_file():
    answer = messagebox.askquestion("?", "I'm going to format your hard drive")
    # messagebox.showinfo("Open doc", "We'll open a file here...")
    
    # answer = messagebox.askyesno("?", "To be or not to be?")
    # answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
    # answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")
    # answer = messagebox.showerror("!", "Your code does nothing!") its only button is titled OK
    # answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!")

def on_off():
    global accessible
    if accessible == tk.DISABLED:
        accessible = tk.ACTIVE
    else:
        accessible = tk.DISABLED
    sub_menu.entryconfigure(1, state=accessible)


def click(*args):
    global counter1
    if counter1 > 0:
        counter1 -= 1
    window.title(str(counter1))
    
    
counter = 0
counter1 = 10
window = tk.Tk()

window.resizable(width=False, height=False)
# window.minsize(width=250, height=200)
# window.maxsize(width=500, height=300)
window.geometry("500x500")
window.bind("<Button-1>", click)

window.title(str(counter1))
window.bind("<Button-1>", click)
# window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='logo.png'))
# window.bind("&lt;Button-1&gt;", lambda e: window.destroy())

button = tk.Button(window, text="Go on!", command=plus)
button.pack()
text = tk.StringVar()
label = tk.Label(window, textvariable=text, height=4)
text.set(to_string(counter))
label.pack()


button1 = tk.Button(window, text="Go ahead!", command=do_it_again)
button1.pack()
text1 = tk.StringVar()
message = tk.Message(window, textvariable=text1, width=400)
text1.set("You did it again... ")
message.pack()


frame_1 = tk.Frame(window, width=200, height=100, bg='white')
frame_2 = tk.Frame(window, width=200, height=100, bg='yellow')

button_1_1 = tk.Button(frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

frame_1.pack()
frame_2.pack()

label_frame_1 = tk.LabelFrame(window, text="Frame #1",
                              width=200, height=100, bg='white')
label_frame_2 = tk.LabelFrame(window, text="Frame #2",
                              labelanchor='se', width=200, height=100, bg='yellow')

button_1_1 = tk.Button(label_frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(label_frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(label_frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(label_frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

label_frame_1.pack()
label_frame_2.pack()


last_string = ''
text2 = tk.StringVar()
entry = tk.Entry(window, textvariable=text2)
text2.set(last_string)
text2.trace('w', digits_only)
entry.pack()
entry.focus_set()


# main menu creation
main_menu = tk.Menu(window)
window.config(menu=main_menu)

accessible = tk.DISABLED
sub_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Menu", menu=sub_menu)
sub_menu.add_command(label="On/Off", command=on_off)
sub_menu.add_command(label="Switch", state=tk.DISABLED)

# 1st main menu item: an empty (as far) submenu
sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
sub_menu_file.add_command(label="Open...", underline=0, command=open_file)

sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

for i in range(8):
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)


sub_menu_file.add_separator()
sub_menu_file.add_command(label="Quit", underline=0, accelerator="Ctrl-Q", command=are_you_sure)
# 2nd main menu item: a simple callback
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app, underline=1)

window.bind_all("<Control-q>", are_you_sure)

window.mainloop()