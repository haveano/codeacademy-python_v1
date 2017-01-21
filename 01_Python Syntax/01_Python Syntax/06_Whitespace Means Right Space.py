"""
Whitespace Means Right Space
Now let's examine the error from the last lesson:

IndentationError: expected an indented block
You'll get this error whenever your whitespace is off.

Instructions
Properly indent the code with four spaces before eggs on line 2 and another four before return on line 3.

You should indent your code with four spaces.
"""
def spam():
    eggs = 12
    return eggs

def spam2():
    eggs2 = 14
    return eggs2
   
print spam()

print spam2()

print spam2()-spam()
