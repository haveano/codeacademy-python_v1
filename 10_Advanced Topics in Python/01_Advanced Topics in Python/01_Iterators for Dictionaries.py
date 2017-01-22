"""
Iterators for Dictionaries
Let's start with iterating over a dictionary. Recall that a dictionary is just a collection of keys and values.

d = {
    "Name": "Guido",
    "Age": 56,
    "BDFL": True
}
print d.items()
# => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]
Note that the items() function doesn't return key/value pairs in any specific order. (For more on this, see the Hint.)

Instructions
Create your own Python dictionary, my_dict, in the editor to the right with two or three key/value pairs.
Then, print the result of calling the my_dict.items().
"""


my_dict={
    "VLAN1": "IP1",
    "VLAN2": "IP2",
    "VLAN3": "IP3",
    "VLAN4": "IP4",
    "VLAN5": "IP5"
}
print my_dict.items()
print my_dict
