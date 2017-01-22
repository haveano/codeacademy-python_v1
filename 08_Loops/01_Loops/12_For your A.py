"""
For your A
String manipulation is useful in for loops if you want to modify some content in a string.

word = "Marble"
for char in word:
    print char,
The example above iterates through each character in word and, in the end, prints out M a r b l e.

The , character after our print statement means that our next print statement keeps printing on the same line.

Instructions
Let's filter out the letter 'A' from our string.

Do the following for each character in the phrase.
If char is an 'A' or char is an 'a', print 'X', instead of char. Make sure to include the trailing comma.
Otherwise (else:), please print char, with the trailing comma.
"""


phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char=="A" or char=="a":
        print "X",
    else:
        print char,


#Don't delete this print statement!
print
