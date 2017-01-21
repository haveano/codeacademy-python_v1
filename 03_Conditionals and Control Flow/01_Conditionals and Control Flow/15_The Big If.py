"""
The Big If
Really great work! Here's what you've learned in this unit:

Comparators

3 < 4
5 >= 5
10 == 10
12 != 13
Boolean operators

True or False 
(3 < 4) and (5 >= 5)
this() and not that()
Conditional statements

if this_might_be_true():
    print "This really is true."
elif that_might_be_true():
    print "That is true."
else:
    print "None of the above."
Let's get to the grand finale.

Instructions
Write an if statement in the_flying_circus(). It must include:

if, elif, and else statements;
At least one of and, or, or not;
A comparator (==, !=, <, <=, >, or >=);
Finally, the_flying_circus() must return True when evaluated.
Don't forget to include a : after your if statements!
"""


# Make sure that the_flying_circus() returns True
"""
def the_flying_circus(a):
    if a>10:    # Start coding here!
        print a# Don't forget to indent
        return 1# the code inside this block!
    elif a<10:
        print a
        return -1
    else:
        print a
        return 0
        
        # Keep going here.
        # You'll want to add the else statement, too!

print the_flying_circus(11)
print the_flying_circus(10)
print the_flying_circus(9)
"""
def the_flying_circus():
    if True and False:    # Start coding here!
        print "a"# Don't forget to indent
        return False# the code inside this block!
    elif True or True:
        print "b"
        return True
    else:
        print "c"
        return 0
        
        # Keep going here.
        # You'll want to add the else statement, too!

print the_flying_circus()
