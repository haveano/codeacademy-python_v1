"""
Generic Imports
Did you see that? Python said: "NameError: name 'sqrt' is not defined." Python doesn't know what square roots are—yet.

There is a Python module named math that includes a number of useful variables and functions, and sqrt() is one of those functions. In order to access math, all you need is the import keyword. When you simply import a module this way, it's called a generic import.

Instructions
You'll need to do two things here:

Type import math on line 2 in the editor.
Insert math. before sqrt() so that it has the form math.sqrt(). This tells Python not only to import math, but to get the sqrt() function from within math.
Then hit Save & Submit to see what Python now knows.
"""
# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)
