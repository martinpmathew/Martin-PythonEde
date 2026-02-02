import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the game board
        game_frame = tk.Frame(self.root)
        game_frame.pack()

        # Create buttons for the 3x3 grid
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    game_frame,
                    text='',
                    font=('Arial', 24, 'bold'),
                    width=4,
                    height=2,
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
        
        # Create a label to display the game status
        self.status_label = tk.Label(
            self.root,
            text=f"Player {self.current_player}'s turn",
            font=('Arial', 16)
        )
        self.status_label.pack(pady=10)

        # Create a reset button
        reset_button = tk.Button(
            self.root,
            text="Reset Game",
            font=('Arial', 12),
            command=self.reset_game
        )
        reset_button.pack(pady=5)

    def on_click(self, row, col):
        if self.board[row][col] == '':
            # Update the board and button with the current player's mark
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            # Check for a winner or a draw
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                # Switch to the other player's turn
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        
        return False

    def check_draw(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.status_label.config(text=f"Player {self.current_player}'s turn")
        
        # Clear the text from all buttons
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()