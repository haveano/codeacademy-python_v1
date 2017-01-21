"""
String Looping
As we've mentioned, strings are like lists with characters as elements. You can loop through strings the same way you loop through lists! While we won't ask you to do that in this section, we've put an example in the editor of how looping through a string might work.

Instructions
Run the code to see string iteration in action!
"""

for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print "\n\n"

print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter
