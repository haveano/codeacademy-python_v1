"""
is_int
An integer is just a number without a decimal part (for instance, -17, 0, and 42 are all integers, but 98.6 is not).

For the purpose of this lesson, we'll also say that a number with a decimal part that is all 0s is also an integer, such as 7.0.

This means that, for this lesson, you can't just test the input to see if it's of type int.

If the difference between a number and that same number rounded down is greater than zero, what does that say about that particular number?

Instructions
Define a function is_int that takes a number x as an input.
Have it return True if the number is an integer (as defined above) and False otherwise.
For example:

is_int(7.0)   # True
is_int(7.5)   # False
is_int(-1)    # True      
"""


import math
def is_int(x):
    #if type(x)==int:
    #if math.floor(x)==x: # też działa, ale math.trunc() lub inc() jest lepsze
    if math.trunc(x)==x:
    #if int(x)==x:
        return True
    else:
        return False


print is_int(-2.3)
print is_int(-2.7)
print is_int(1.9999999999999999) # HAHAHA
"""
print math.trunc(-2.3)
print math.trunc(-2.7)
print math.floor(-2.3)
print math.floor(-2.7)
print int(-2.9)
print int(-2.1)
"""
