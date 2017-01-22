"""
Custom Print
Now we can see the contents of our list, but clearly it would be easier to play the game if we could print the board out like a grid with each row on its own line.

We can use the fact that our board is a list of lists to help us do this. Let's set up a for loop to go through each of the elements in the outer list (each of which is a row of our board) and print them.

Instructions
First, delete your existing print statement.
Then, define a function named print_board with a single argument, board.
Inside the function, write a for loop to iterates through each row in board and print it to the screen.
Call your function with board to make sure it works.
"""

board=[]
for i in range(0,5,1):
    board.append(["O"]*5)

def print_board(board):
    for i in board:
        print i
    return 0
print print_board(board)
