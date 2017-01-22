"""
Make a List
Good! Now we'll use a built-in Python function to generate our board, which we'll make into a 5 x 5 grid of all "O"s, for "ocean."

print ["O"] * 5
will print out ['O', 'O', 'O', 'O', 'O'], which is the basis for a row of our board.

We'll do this five times to make five rows. (Since we have to do this five times, it sounds like a loop might be in order.)

Instructions
Create a 5 x 5 grid initialized to all 'O's and store it in board.

Use range() to loop 5 times.
Inside the loop, .append() a list containing 5 "O"s to board, just like in the example above.
Note that these are capital letter "O" and not zeros.
"""

board=[]
for i in range(0,5,1):
    board.append(["O"]*5)
print board
