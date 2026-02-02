import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGame:
    def __init__(self, master):
        """
        Initializes the main game window and all game components.
        Sets up the board, a list to track its state, and starts the game with
        the computer's first move.
        """
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.master.geometry("250x270")
        self.master.resizable(False, False)

        # Game state variables
        # Use a list of lists to represent the board's internal state
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X' # 'X' for computer, 'O' for user

        # Create and place the buttons for the game board
        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    self.master,
                    text='',
                    font=('Helvetica', 20, 'bold'),
                    width=4,
                    height=2
                )
                # Use a lambda to pass the row and col to the click handler
                btn.config(command=lambda r=row, c=col: self.handle_click(r, c))
                btn.grid(row=row, column=col, sticky="nsew")
                self.buttons[row][col] = btn

        # Configure row and column weights to make the grid expandable
        for i in range(3):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

        # The computer always makes the first move in the center
        self.computer_move()

    def handle_click(self, row, col):
        """Handles a user's click on a tile."""
        # Check if the tile is empty before allowing a move
        if self.board[row][col] == '':
            # User's turn: place 'O'
            self.buttons[row][col].config(text='O', fg='green')
            self.board[row][col] = 'O'
            self.current_player = 'X'
            
            # Check for a winner or a tie
            if not self.check_game_state():
                # If the game is not over, the computer makes its move
                self.master.after(500, self.computer_move) # Delay for better user experience

    def computer_move(self):
        """
        Generates a move for the computer ('X') and updates the board.
        Chooses a random available spot.
        """
        available_spots = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == '':
                    available_spots.append((r, c))
        
        if available_spots:
            # Randomly select an empty spot
            row, col = random.choice(available_spots)
            self.buttons[row][col].config(text='X', fg='red')
            self.board[row][col] = 'X'
            self.current_player = 'O'
            
            self.check_game_state()

    def check_game_state(self):
        """
        Checks for a win or a tie condition.
        Returns True if the game is over, False otherwise.
        """
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '':
                self.end_game(self.board[i][0])
                return True
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != '':
                self.end_game(self.board[0][i])
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            self.end_game(self.board[0][0])
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '':
            self.end_game(self.board[0][2])
            return True

        # Check for a tie (no more empty spaces)
        if all(self.board[r][c] != '' for r in range(3) for c in range(3)):
            self.end_game(None)
            return True
        
        return False

    def end_game(self, winner):
        """Displays a message box and disables all buttons to end the game."""
        for row in self.buttons:
            for btn in row:
                btn.config(state=tk.DISABLED)

        if winner:
            messagebox.showinfo("Game Over", f"The winner is {winner}!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
