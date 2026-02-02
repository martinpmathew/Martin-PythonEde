import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, master):
        """
        Initializes the calculator's main window, display, and buttons.
        Sets up the core logic for all arithmetic operations.
        """
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("240x350")
        self.master.resizable(False, False)

        # Class variables for calculator logic
        self.current_number = "0"
        self.first_operand = None
        self.operator = None
        self.is_new_number = True
        self.is_error = False

        # Set up a fixed-width font for the display
        display_font = font.Font(family="Courier", size=18, weight="bold")

        # Display entry widget
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Entry(
            self.master,
            textvariable=self.display_var,
            font=display_font,
            bd=5,
            relief=tk.SUNKEN,
            justify=tk.RIGHT,
            state="readonly"
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Define button layout and create buttons
        self.button_texts = [
            'AC', '+/-', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '='
        ]

        # Use a dictionary to map button text to its color
        self.colors = {
            'AC': '#f08080', '+/-': '#d3d3d3', '%': '#d3d3d3', '/': '#ff8c00',
            '*': '#ff8c00', '-': '#ff8c00', '+': '#ff8c00', '=': '#ff8c00',
            '0': '#a9a9a9', '1': '#a9a9a9', '2': '#a9a9a9', '3': '#a9a9a9',
            '4': '#a9a9a9', '5': '#a9a9a9', '6': '#a9a9a9', '7': '#a9a9a9',
            '8': '#a9a9a9', '9': '#a9a9a9', '.': '#a9a9a9'
        }

        row, col = 1, 0
        for text in self.button_texts:
            if text == '0':
                # Special case for the '0' button to span two columns
                btn = tk.Button(
                    self.master,
                    text=text,
                    font=display_font,
                    bg=self.colors.get(text, '#a9a9a9'),
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
                col += 2
            else:
                btn = tk.Button(
                    self.master,
                    text=text,
                    font=display_font,
                    bg=self.colors.get(text, '#d3d3d3'),
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
                col += 1

            if col > 3:
                col = 0
                row += 1

        # Make the grid cells expandable
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def update_display(self):
        """
        Updates the display with the current number, handling formatting
        and the 10-character length limit.
        """
        if self.is_error:
            self.display_var.set("E")
            return

        # Format the number for display
        display_text = self.current_number
        if '.' in display_text:
            # If the number has a decimal point, show it
            pass
        elif len(display_text) > 1 and display_text.startswith('0'):
            # Remove leading zero for integers
            if len(display_text) > 1 and display_text[1] != '.':
                display_text = display_text.lstrip('0')
                if not display_text:
                    display_text = '0'
        
        # Check for length limit
        if len(display_text) > 10:
            self.is_error = True
            self.display_var.set("E")
            return
        
        self.display_var.set(display_text)

    def on_button_click(self, text):
        """
        Main event handler for all button clicks.
        Dispatches to the correct method based on the button's text.
        """
        if self.is_error and text != 'AC':
            return
        
        if text.isdigit() or text == '.':
            self.on_digit_point_click(text)
        elif text in ['+', '-', '*', '/', '%']:
            self.on_operator_click(text)
        elif text == '=':
            self.on_equals_click()
        elif text == 'AC':
            self.on_clear_click()
        elif text == '+/-':
            self.on_sign_change_click()
    
    def on_digit_point_click(self, char):
        """Handles clicks on digit and decimal point buttons."""
        if self.is_new_number:
            if char == '.':
                self.current_number = "0."
            else:
                self.current_number = char
            self.is_new_number = False
        else:
            if char == '.' and '.' in self.current_number:
                return # Prevent multiple decimal points
            if len(self.current_number.replace('.', '').replace('-', '')) >= 10:
                return # Max 10 digits
            self.current_number += char

        self.update_display()
    
    def on_operator_click(self, op):
        """
        Handles clicks on operator buttons (+, -, *, /).
        Stores the first operand and the operator.
        """
        if self.first_operand is not None and not self.is_new_number:
            # If an operation is already pending, calculate the intermediate result
            self.on_equals_click()
        
        try:
            self.first_operand = float(self.current_number)
            self.operator = op
            self.is_new_number = True
        except ValueError:
            self.is_error = True
        self.update_display()
        
    def on_equals_click(self):
        """
        Performs the calculation when the equals button is clicked.
        Handles division by zero and number overflow.
        """
        if self.first_operand is None or self.is_new_number:
            return

        try:
            second_operand = float(self.current_number)
            result = 0

            if self.operator == '+':
                result = self.first_operand + second_operand
            elif self.operator == '-':
                result = self.first_operand - second_operand
            elif self.operator == '*':
                result = self.first_operand * second_operand
            elif self.operator == '/':
                if second_operand == 0:
                    raise ZeroDivisionError
                result = self.first_operand / second_operand
            elif self.operator == '%':
                result = self.first_operand % second_operand

            # Check for result overflow
            result_str = str(result)
            if len(result_str.replace('.', '').replace('-', '')) > 10:
                self.is_error = True
            else:
                self.current_number = str(result)
                # Remove trailing .0
                if self.current_number.endswith('.0'):
                    self.current_number = self.current_number[:-2]
                self.first_operand = None
                self.operator = None
                self.is_new_number = True

        except (ZeroDivisionError, ValueError):
            self.is_error = True
        
        self.update_display()

    def on_clear_click(self):
        """Resets the calculator to its initial state."""
        self.current_number = "0"
        self.first_operand = None
        self.operator = None
        self.is_new_number = True
        self.is_error = False
        self.update_display()

    def on_sign_change_click(self):
        """Toggles the sign of the current number."""
        if self.current_number != "0" and not self.is_error:
            if self.current_number.startswith('-'):
                self.current_number = self.current_number[1:]
            else:
                self.current_number = '-' + self.current_number
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
