"""
Passing a range into a function
Okay! Range time. The Python range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.

range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
The range function has three different versions:

range(stop)
range(start, stop)
range(start, stop, step)
In all cases, the range() function returns a list of numbers from start up to (but not including) stop. Each item increases by step.

If omitted, start defaults to zero and step defaults to one.

Instructions
On line 6, replace the ____ with a range() that returns a list containing [0, 1, 2].
"""


def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

n=[0,1,2]
print my_function(n) # Add your range between the parentheses!
