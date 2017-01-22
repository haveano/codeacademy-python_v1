"""
factorial
All right! Now we're cooking. Let's try a factorial problem.

To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example:

factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
factorial(1) would equal 1.
factorial(3) would equal 3 * 2 * 1, which is 6.
Instructions
Define a function factorial that takes an integer x as input.

Calculate and return the factorial of that number.
"""

def factorial(x):
    y=x
    while x>=2:
        y=y*(x-1)
        x=x-1
    return y
print factorial(3)
print factorial(7)
