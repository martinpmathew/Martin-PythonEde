import tkinter as tk
import random

class TheClickerGame:
    def __init__(self, master):
        """Initializes the main game window and all game components."""
        self.master = master
        self.master.title("The Clicker")

        # Game state variables
        self.game_started = False
        self.time_elapsed = 0
        self.timer_id = None
        self.buttons = {}
        self.sorted_numbers = []
        self.next_number_to_click = 0

        # Create main frames
        self.main_frame = tk.Frame(self.master, padx=10, pady=10)
        self.main_frame.pack(expand=True)
        
        self.grid_frame = tk.Frame(self.main_frame)
        self.grid_frame.pack(pady=10)

        # Create the timer label
        self.timer_label = tk.Label(self.main_frame, text="Time: 0", font=("Helvetica", 16))
        self.timer_label.pack(pady=(10, 0))

        # Start the game setup
        self.setup_game_board()

    def setup_game_board(self):
        """
        Generates unique random numbers, creates the buttons, and binds them to the click event.
        """
        # Generate 25 unique random numbers between 1 and 999
        self.numbers = random.sample(range(1, 1000), 25)
        self.sorted_numbers = sorted(self.numbers)

        # Create and place the buttons in a 5x5 grid
        for i in range(5):
            for j in range(5):
                number = self.numbers[i * 5 + j]
                button = tk.Button(
                    self.grid_frame,
                    text=str(number),
                    width=6,
                    height=2,
                    font=("Helvetica", 12),
                    bg="#dcdcdc",  # Default button color
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                # Store the button reference keyed by its number for easy lookup
                self.buttons[number] = button
                # Bind the left mouse click event to the click handler
                button.bind("<Button-1>", self.on_button_click)
    
    def on_button_click(self, event):
        """
        Handles the button click event.
        Checks if the clicked button is the correct one in the sequence.
        """
        if not self.game_started:
            # Start the timer on the very first click
            self.game_started = True
            self.update_timer()

        # Get the number from the clicked button
        clicked_number_str = event.widget.cget("text")
        clicked_number = int(clicked_number_str)

        # Check if the clicked number is the next number in the sorted sequence
        if clicked_number == self.sorted_numbers[self.next_number_to_click]:
            # Correct click: disable the button and move to the next number
            event.widget.config(state=tk.DISABLED, relief=tk.SUNKEN)
            self.next_number_to_click += 1

            # Check if all buttons have been clicked
            if self.next_number_to_click == len(self.sorted_numbers):
                self.end_game()

    def update_timer(self):
        """
        Increments the timer every second and updates the label.
        Uses after() to schedule the next update.
        """
        if self.game_started:
            self.time_elapsed += 1
            self.timer_label.config(text=f"Time: {self.time_elapsed}")
            self.timer_id = self.master.after(1000, self.update_timer)

    def end_game(self):
        """
        Stops the timer and displays a final message.
        """
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
            self.timer_id = None
        
        self.game_started = False
        final_time = self.timer_label.cget("text").split(" ")[1]
        self.timer_label.config(text=f"Game Over! Final Time: {final_time} seconds", font=("Helvetica", 16, "bold"))
        print(f"Congratulations! You finished in {final_time} seconds.")

if __name__ == "__main__":
    root = tk.Tk()
    game = TheClickerGame(root)
    root.mainloop()
