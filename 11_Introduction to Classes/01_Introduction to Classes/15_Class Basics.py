"""
Class Basics
First things first: let's create a class to work with.

Instructions
Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the __init__() method (see the Hint for more).
"""



class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3

