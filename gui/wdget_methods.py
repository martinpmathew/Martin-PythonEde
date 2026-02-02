import tkinter as tk


def blink():
    global is_white
    if is_white:
        color = "black"
    else:
        color = "white"
    
    is_white = not is_white
    frame.config(bg=color)
    frame.after(500, blink)


def suicide():
    # Note: Frame Destroy
    frame1.destroy()
    

def flip_focus():
    if window.focus_get() is button_1:
        button_2.focus_set()
    else:
        button_1.focus_set()
    window.after(1000, flip_focus)
      
is_white = True
window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='white')
frame.after(500, blink)
frame.pack()

frame1 = tk.Frame(window, width=200, height=100, bg='green')

# Note: its not windows frame1
button = tk.Button(frame1, text="I'm a frame's child")
button.place(x=10, y=10)
frame1.after(5000, suicide) # 5000 ms

button_1 = tk.Button(window, text="First")
button_1.pack()
button_2 = tk.Button(window, text="Second")
button_2.pack()
window.after(1000, flip_focus)

frame1.pack()

window.mainloop()

