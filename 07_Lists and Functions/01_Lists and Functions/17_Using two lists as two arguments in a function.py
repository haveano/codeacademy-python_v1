"""
Using two lists as two arguments in a function
Using multiple lists in a function is no different from just using multiple arguments in a function!

a = [1, 2, 3]
b = [4, 5, 6]
print a + b
# prints [1, 2, 3, 4, 5, 6]
The example above is just a reminder of how to concatenate two lists.

Instructions
Create a function that joins two lists together.

On line 4, define a function called join_lists that has two arguments, x and y. They will both be lists.
Inside that function, return the result of concatenating x and y together.
"""


m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!

def join_lists(x,y):
    return x+y



print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]
