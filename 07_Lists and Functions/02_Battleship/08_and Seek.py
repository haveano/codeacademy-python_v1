"""
...and Seek!
Good job! For now, let's store coordinates for the ship in the variables ship_row and ship_col. Now you have a hidden battleship in your ocean! Let's write the code to allow the player to guess where it is.

number = raw_input("Enter a number: ")
if int(number) == 0:
    print "You entered 0"
raw_input asks the user for input and returns it as a string. But we're going to want to use integers for our guesses! To do this, we'll wrap the raw_inputs with int() to convert the string to an integer.

Instructions
Create a new variable called guess_row and set it to int(raw_input("Guess Row: ")).
Create a new variable called guess_col and set it to int(raw_input("Guess Col: ")).
Click Save & Submit and then answer the prompts by typing in a number and pressing Enter (or Return on some computers).
"""

from random import randint

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row=int(raw_input("Guess Row: "))
guess_col=int(raw_input("Guess Col: "))

# Add your code below!
