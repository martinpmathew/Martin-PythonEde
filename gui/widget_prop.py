import tkinter as tk


def on_off():
    global button
    state = button["text"]
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state


# oter methods
#
# def on_off():
#     global button
#     state = button.cget("text")
#     if state == "ON":
#         state = "OFF"
#     else:
#         state = "ON"
#     button.config(text=state)
window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button["borderwidth"] = 10
button["highlightthickness"] = 10
button["padx"] = 10
button["pady"] = 5
button["underline"] = 1
button["anchor"] = "nw"
button["width"] = 20
button["height"] = 3  # rows
button.pack()

label_1 = tk.Label(window, height=3, text="arrow", cursor="man")
label_1.pack()
label_2 = tk.Label(window, height=3, text="clock", cursor="clock")
label_2.pack()
label_3 = tk.Label(window, height=3, text="heart", cursor="heart")
label_3.pack()
# label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
# label_1.grid(column=0, row=0)
# label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
# label_2.grid(column=0, row=1)
# label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
# label_3.grid(column=0, row=2)

window.mainloop()
