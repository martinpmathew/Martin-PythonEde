import tkinter as tk

def create_calculator():
    root = tk.Tk()
    root.title("Simple Calculator")

    # Create the display entry field
    display = tk.Entry(root, width=25, font=('Arial', 16), justify='right')
    display.grid(row=0, column=0, columnspan=4, pady=10)

    # Function to update the display when a button is clicked
    def button_click(number):
        current = display.get()
        display.delete(0, tk.END)
        display.insert(0, str(current) + str(number))

    # Function to clear the display
    def button_clear():
        display.delete(0, tk.END)

    # Function to calculate the result
    def button_equal():
        try:
            expression = display.get()
            # The `eval` function evaluates the string expression
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(0, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    
    # Define the button layout
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    # Add the number and operator buttons
    for (text, row, col) in buttons:
        if text == '=':
            button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=button_equal)
        else:
            button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: button_click(t))
        button.grid(row=row, column=col, sticky="nsew")

    # Add the Clear button separately
    clear_button = tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 14), command=button_clear)
    clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

    # Make the buttons expand to fill the grid cells
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
        
    root.mainloop()

if __name__ == "__main__":
    create_calculator()