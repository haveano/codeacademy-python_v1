"""
Hide...
Excellent! Now, let's hide our battleship in a random location on the board.

Since we have a 2-dimensional list, we'll use two variables to store the ship's location, ship_row and ship_col.

from random import randint
coin = randint(0, 1)
dice = randint(1, 6)
In the above example, we first import the randint(low, high) function from the random module.
Then, we generate either zero or one and store it in coin.
Finally, we generate a number from one to six inclusive.
Let's generate a random_row and random_col from zero to four!

Instructions
Define two new functions, random_row and random_col, that each take board as input.
These functions should return a random row index and a random column index from your board, respectively. Use randint(0, len(board) - 1).
Call each function on board.
"""

from random import randint 

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# Add your code below!
def random_row(board):
    return randint(0,len(board)-1)
def random_col(board):
    return randint(0,len(board)-1)
print random_row(board)
print random_col(board)
