"""
Functions Calling Functions
We've seen functions that can print text or do simple arithmetic, but functions can be much more powerful than that. For example, a function can call another function:

def fun_one(n):
    return n * 5

def fun_two(m):
    return fun_one(m) + 7
Instructions
Let's look at the two functions in the editor: one_good_turn (which adds 1 to the number it takes in as an argument) and deserves_another (which adds 2).

Change the body of deserves_another so that it always adds 2 to the output of one_good_turn.
"""
def one_good_turn(n):
    print "text1: ",n
    return n + 1
    
    
def deserves_another(n):
    print "text2: ",n
    #return n + 2
    return one_good_turn(n) + 2

print "text3: ", one_good_turn(8)
print "text4: ", deserves_another(8)
