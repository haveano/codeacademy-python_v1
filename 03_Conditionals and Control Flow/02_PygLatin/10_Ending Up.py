"""
Ending Up
Well done! However, now we have the first letter showing up both at the beginning and near the end.

s = "Charlie"

print s[0]
# will print "C"

print s[1:4]
# will print "har"
First we create a variable s and give it the string "Charlie"
Next we access the first letter of "Charlie" using s[0]. Remember letter positions start at 0.
Then we access a slice of "Charlie" using s[1:4]. This returns everything from the letter at position 1 up till position 4.
We are going to slice the string just like in the 3rd example above.

Instructions
Set new_word equal to the slice from the 1st index all the way to the end of new_word. Use [1:len(new_word)] to do this.
"""
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word=original.lower()
    first=word[0]
    new_word=word[1:len(word)]+first+pyg
    print new_word
    
else:
    print 'empty'
