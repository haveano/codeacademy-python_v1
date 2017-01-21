"""
Check Yourself... Some More
Now we know we have a non-empty string. Let's be even more thorough.

x = "J123"
x.isalpha()  # False
In the first line, we create a string with letters and numbers.

The second line then runs the function isalpha() which returns False since the string contains non-letter characters.

Let's make sure the word the user enters contains only alphabetical characters. You can use isalpha() to check this! For example:

Instructions
Use and to add a second condition to your if statement. In addition to your existing check that the string contains characters, you should also use .isalpha() to make sure that it only contains letters.

Don't forget to keep the colon at the end of the if statement!
"""
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("enter a word:")
if len(original)>0 and original.isalpha():
    print original
else:
    print "empty"
