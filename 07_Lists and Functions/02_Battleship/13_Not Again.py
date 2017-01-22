"""
Not Again!
Great! Now let's handle the second type of incorrect guess: the player guesses a location that was already guessed. How will we know that a location was previously guessed?

print board[guess_row][guess_col]
The example above will print an 'X' if already guessed or an 'O' otherwise.

Instructions
Add an elif to see if the guessed location already has an 'X' in it.
If it has, print "You guessed that one already."
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
#print ship_row
#print ship_col
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

# Write your code below!
if guess_row==ship_row and guess_col==ship_col:
    print "Congratulations! You sank my battleship!"
elif board[guess_row][guess_col]=="X":
    print "You guessed that one already."
else:
    if guess_row not in range(5) or guess_col not in range(5):
        print "Oops, that's not even in the ocean."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col]="X"
    print_board(board)
