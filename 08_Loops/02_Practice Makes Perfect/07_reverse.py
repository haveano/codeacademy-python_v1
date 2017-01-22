"""
reverse
Great work so far! Let's practice writing some functions that work with strings.

Instructions
Define a function called reverse that takes a string textand returns that string in reverse.

For example: reverse("abcd") should return "dcba".

You may not use reversed or [::-1] to help you with this.
You may get a string containing special characters (for example, !, @, or #).
"""


def reverse(text):
    x=len(str(text))
    n=0
    text2=list(text)
    text3=""

    for n in range(x):
        text3=text3+text2[x-n-1]
        n=n+1
    return text3
        
print reverse("abc@$%^$&**")
#text3="avc"
#print text3[2]
