#Python Project by FArhan Shariar
import tkinter as tk
from tkinter import messagebox
#Done By Farhan Shariar
# Initialize main game window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("300x350")
root.resizable(False, False)

# Game variables
current_player = "X"  # "X" starts the game
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 board
buttons = []  # Store buttons on grid
score = {"X": 0, "O": 0}  # Scoreboard

# Functions
def on_button_click(i, j):
    global current_player

    # If cell is already taken, do nothing
    if board[i][j] != "":
        return

    # Mark cell for the current player
    board[i][j] = current_player
    # Set color based on player
    color = "blue" if current_player == "X" else "green"
    buttons[i][j].config(text=current_player, state="disabled", disabledforeground=color)

    # Check for a win or tie
    if check_win(current_player):
        score[current_player] += 1
        update_scoreboard()
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        reset_game()
    elif check_tie():
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()
    else:
        # Switch players
        current_player = "O" if current_player == "X" else "X"
        turn_label.config(text=f"Turn: Player {current_player}")

def check_win(player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_tie():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")
    turn_label.config(text="Turn: Player X")

def update_scoreboard():
    score_label.config(text=f"Score - X: {score['X']} | O: {score['O']}")
#Done By Farhan Shariar
# UI Elements
# Scoreboard and turn display
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

score_label = tk.Label(frame_top, text=f"Score - X: {score['X']} | O: {score['O']}", font=("Helvetica", 12))
score_label.pack(side="left", padx=10)

turn_label = tk.Label(frame_top, text="Turn: Player X", font=("Helvetica", 12))
turn_label.pack(side="right", padx=10)

# Game grid
frame_grid = tk.Frame(root)
frame_grid.pack()

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(
            frame_grid, text="", width=5, height=2, font=("Helvetica", 16, "bold"),
            command=lambda i=i, j=j: on_button_click(i, j),
            bg="lightgray", relief="solid", borderwidth=2
        )
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)
#Done By Farhan Shariar
# Reset button
reset_btn = tk.Button(root, text="New Game", command=reset_game, font=("Helvetica", 12), bg="lightblue")
reset_btn.pack(pady=15)
#Done By Farhan Shariar
# Start the game
root.mainloop()
#Done By Farhan Shariar
