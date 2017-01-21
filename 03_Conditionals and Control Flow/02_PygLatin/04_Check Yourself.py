"""
Check Yourself!
Next we need to ensure that the user actually typed something.

empty_string = ""
if len(empty_string) > 0:
    # Run this block.
    # Maybe print something?
else:
    # That string must have been empty.
We can check that the user's string actually has characters!

Instructions
Write an if statement that verifies that the string has characters.

Add an if statement that checks that len(original) is greater than zero. Don't forget the : at the end of the if statement!
If the string actually has some characters in it, print the user's word.
Otherwise (i.e. an else: statement), please print "empty".
You'll want to run your code multiple times, testing an empty string and a string with characters. When you're confident your code works, continue to the next exercise.
"""
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("enter a word:")
if len(original)>0:
    print original
else:
    print "empty"
