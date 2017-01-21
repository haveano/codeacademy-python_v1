"""
Call and Response
After defining a function, it must be called to be implemented. In the previous exercise, spam() in the last line told the program to look for the function called spam and execute the code inside it.

Instructions
We've set up a function, square. Call it on the number 10 (by putting 10 between the parentheses of square()) on line 9!
"""
def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.

square(10)
