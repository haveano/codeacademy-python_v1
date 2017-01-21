"""
Word Up
Let's simplify things by making the letters in our word lowercase.

the_string = "Hello"
the_string = the_string.lower()
The .lower() function does not modify the string itself, it simply returns a lowercase-version. In the example above, we store the result back into the same variable.

We also need to grab the first letter of the word.

first_letter  = the_string[0]
second_letter = the_string[1]
third_letter  = the_string[2]
Remember that we start counting from zero, not one, so we access the first letter by asking for [0].

Instructions
Inside your if statement:

Create a new variable called word that holds the .lower()-case conversion of original.
Create a new variable called first that holds word[0], the first letter of word.
"""
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word=original.lower()
    first=word[0]
    
else:
    print 'empty'
