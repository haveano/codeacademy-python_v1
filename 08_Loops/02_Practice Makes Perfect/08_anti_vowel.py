"""
anti_vowel
Nice work. Next up: vowels!

Instructions
Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return "Hy Y!".

Don't count Y as a vowel.
Make sure to remove lowercase and uppercase vowels.
"""


#vowels=["a","e","u","i","o"]
def anti_vowel(text):
    text2=list(text)
    text3=""
    for x in text2:
 #       if x.lower() not in vowels:
        if x.lower() not in "aeuio":
            text3=text3+x
    return text3

#print vowels
print anti_vowel("text--EXTY--eiutyt")
