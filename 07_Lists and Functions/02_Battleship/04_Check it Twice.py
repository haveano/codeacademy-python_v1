"""
Check it Twice
Great job! Now that we've built our board, let's show it off.

Throughout our game, we'll want to print the game board so that the player can see which locations they have already guessed. Regularly printing the board will also help us debug our program.

The easiest way to print the board would be to have Python display it for us using the print command. Let's give that a try and see what the results look like—is this a useful way to print our board for Battleship?

Instructions
Use the print command to display the contents of the board list.
"""

board=[]
for i in range(0,5,1):
    board.append(["O"]*5)
print board
