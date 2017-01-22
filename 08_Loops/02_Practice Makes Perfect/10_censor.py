"""
censor
You're doing great with these string function challenges. Last one!

Instructions
Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.

For example:

censor("this hack is wack hack", "hack") 
should return

"this **** is wack ****"
Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word.
"""


def censor2(text, fword):
    return text.replace(fword,"*"*len(fword))
#to lepsze, bo poniższe rozpoznaje tylko całe wyrazy
# i nie zadzaiała na motherfucker

def censor(text, fword):
    text=text.split()
    for x in text:
        if x==fword:
            text[text.index(x)]="*"*len(fword)
    return " ".join(text)

def censor3(text, word):
    text = text.split()
    #print text
    lst = []
    for i in text:
        if i == word:
            lst.append("*" * len(word)) 
        else:
            lst.append(i)
    return " ".join(lst)
"""
print censor3("what the fuck, motherfucker?!?!","fuck")
print censor2("what the fuck, motherfucker?!?!","fuck")
print censor("what the fuck, motherfucker?!?!","fuck")
"""
"""
print censor3("what the fuck motherfucker?!?!","fuck")
print censor2("what the fuck motherfucker?!?!","fuck")
print censor("what the fuck motherfucker?!?!","fuck")
"""
