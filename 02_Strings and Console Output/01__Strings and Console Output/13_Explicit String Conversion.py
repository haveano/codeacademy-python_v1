"""
Explicit String Conversion
Sometimes you need to combine a string with something that isn't a string. In order to do that, you have to convert the non-string into a string.

print "I have " + str(2) + " coconuts!"
This will print I have 2 coconuts!.

The str() method converts non-strings into strings. In the above example, you convert the number 2 into a string and then you concatenate the strings together just like in the previous exercise.

Now try it yourself!

Instructions
Run the code as-is. You get an error!
Use str() to turn 3.14 into a string. Then run the code again.
"""
# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)
print "3.14"

a = str(3.14)
b = "3.14"

if a == b:
    print "True1"
else:
    print "False1"

if a is b:
    print "True2"
else:
    print "False2"
