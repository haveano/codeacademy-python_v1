"""
Testing, Testing, is This Thing On?
Yay! You should have a fully functioning Pig Latin translator. Test your code thorougly to be sure everything is working smoothly.

You'll also want to take out any print statements you were using to help debug intermediate steps of your code. Now might be a good time to add some comments too! Making sure your code is clean, commented, and fully functional is just as important as writing it in the first place.

Instructions
When you're sure your translator is working just the way you want it, click Save & Submit Code to finish this project.
"""
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word=original.lower()
    print word
    first=word[0]
    print first
    new_word=word[1:len(word)]+first+pyg
    print new_word
    
else:
    print 'empty'
