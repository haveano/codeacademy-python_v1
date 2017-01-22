"""
Modifying each element in a list in a function
This exercise shows how to modify each element in a list. It is useful to do so in a function as you can easily put in a list of any length and get the same functionality. As you can see, len(n) is the length of the list.

Instructions
Create a function called double_list that takes a single argument x (which will be a list) and multiplies each element by 2 and returns that list. Use the existing code as a scaffold.
"""

n = [3, 5, 7]


def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    # Don't forget to return your new list!
    return x

print double_list(n)
