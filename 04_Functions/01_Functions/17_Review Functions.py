"""
Review: Functions
Okay! Let's review functions.

def speak(message):
    return message

if happy():
    speak("I'm happy!")
elif sad():
    speak("I'm sad.")
else:
    speak("I don't know what I'm feeling.")
Again, the example code above is just there for your reference!

Instructions
First, def a function, shut_down, that takes one argument s. Don't forget the parentheses or the colon!
Then, if the shut_down function receives an s equal to "yes", it should return "Shutting down"
Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted".
Finally, if shut_down gets anything other than those inputs, the function should return "Sorry"
"""

#def speak(message)
#    return message

def shut_down(s):
    if s=="yes":
        return "Shutting down"
    elif s=="no":
        return "Shutdown aborted"
    else:
        return "Sorry"

print shut_down("yes")
print shut_down("no")
print shut_down("yno")
