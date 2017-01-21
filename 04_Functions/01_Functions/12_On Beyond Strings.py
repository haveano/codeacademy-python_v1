"""
On Beyond Strings
Now that you understand what functions are and how to import modules, let's look at some of the functions that are built in to Python (no modules required!).

You already know about some of the built-in functions we've used with strings, such as .upper(), .lower(), str(), and len(). These are great for doing work with strings, but what about something a little more analytic?

Instructions
What do you think the code in the editor will do? Click Save & Submit Code when you think you have an idea.
"""
def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
