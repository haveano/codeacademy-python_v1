"""
Move it on Back
Now that we have the first letter stored, we need to add both the letter and the string stored in pyg to the end of the original string.

Remember how to concatenate (i.e. add) strings together?

greeting = "Hello "
name = "D. Y."
welcome = greeting + name
Instructions
On a new line after where you created the first variable:

Create a new variable called new_word and set it equal to the concatenation of word, first, and pyg.
"""
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word=original.lower()
    first=word[0]
    new_word=word+first+pyg
    
else:
    print 'empty'
