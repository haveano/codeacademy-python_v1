"""
You win!
Okay—now for the fun! We have the actual location of the ship and the player's guess so we can check to see if the player guessed right.

For a guess to be right, guess_col should be equal to ship_col and guess_row should be equal to ship_row.

if guess_col == 0 and guess_row == 0:
    print "Top-left corner."
The example above is just a reminder about if statements.

Instructions
On line 29, add an if guess_row equals ship_row and guess_col equals ship_col.
If that is the case, please print out "Congratulations! You sank my battleship!"
"""

from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

# Write your code below!
if guess_row==ship_row and guess_col==ship_col:
    print "Congratulations! You sank my battleship!"
