"""
And Now, For Something Completely Familiar
Great job! You've learned a lot in this unit, including:

Three ways to create strings

'Alpha'
"Bravo"
str(3)
String methods

len("Charlie")
"Delta".upper()
"Echo".lower()
Printing a string

print "Foxtrot"
Advanced printing techniques

g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)
Instructions
Let's wrap it all up!

On line 3, create the variable my_string and set it to any string you'd like.
On line 4, print the length of my_string.
On line 5, print the .upper() case version of my_string.
"""
my_string = raw_input("Wpisz jakis text")
print "\nwpisany tekst to: \"%s\"" % (my_string)
print "\n", len(my_string)
print "\ndlugosc wpisanego tekstu to: %s" % (len(my_string))
print "\n", my_string.upper()
print "\nzapisany duzymi wyglada tak: %s" % (my_string.upper())
