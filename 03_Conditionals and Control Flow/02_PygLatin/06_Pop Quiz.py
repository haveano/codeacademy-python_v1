"""
Pop Quiz!
When you finish one part of your program, it's important to test it multiple times, using a variety of inputs.

Instructions
Take some time to test your current code. Try some inputs that should pass and some that should fail. Enter some strings that contain non-alphabetical characters and an empty string.

When you're convinced your code is ready to go, click Save & Submit to move forward!
"""
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("enter a word:")
if len(original)>0 and original.isalpha():
    print original
else:
    print "empty"
