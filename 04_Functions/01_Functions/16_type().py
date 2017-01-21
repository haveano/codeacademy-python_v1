"""
type()
Finally, the type() function returns the type of the data it receives as an argument. If you ask Python to do the following:

print type(42)
print type(4.2)
print type('spam')
Python will output:

<type 'int'>
<type 'float'>
<type 'str'>
Instructions
Have Python print out the type of an int, a float, and a str string in the editor. You can pick any values on which to call type(), so long as they produce one of each.
"""

# Print out the types of an integer, a float,
# and a string on separate lines below.

print type(-6)
print type(-5)
print type(0)
print type(256)
print type(259)
b=9223372036854775807
c=9223372036854775808
d=c-b
#https://en.wikipedia.org/wiki/9223372036854775807
print d
print type(b)
print type(c)
print type(d)
print type("trxt")
print type('trxt')
print type (0.0)
#print type('trxt")
#print type("trxt')
#print type(trxt)
