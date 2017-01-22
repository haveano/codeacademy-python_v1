"""
For your hobbies
This kind of loop is useful when you want to do something a certain number of times, such as append something to the end of a list.

Instructions
Create a for loop that prompts the user for a hobby 3 times, then appends each one to hobbies.
"""


hobbies = []

# Add your code below!
#count =3
for count in range (3):
    hobbies.append(str(raw_input("Podaj swoje hobby: ")))
    #count=count-1
else:
    print "dxieki"
    print "twoje hobby to: ", hobbies
    print "twoje hobby to: ", hobbies[0],hobbies[1],hobbies[2]
