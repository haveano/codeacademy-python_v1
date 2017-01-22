"""
keys() and values()
Whereas items() returns an array of tuples with each tuple consisting of a key/value pair from the dictionary:

The keys() function returns an array of the dictionary's keys, and
The values() function returns an array of the dictionary's values.
Again, these functions will not return the keys or values from the dictionary in any specific order.

You can think of a tuple as an immutable (that is, unchangeable) list (though this is an oversimplification); tuples are surrounded by ()s and can contain any data type.
Instructions
Remove your call to items() and replace it with a call to keys() and a call to values(), each on its own line. Make sure to print both!
"""


my_dict={
    "VLAN1": "IP1",
    "VLAN2": "IP2",
    "VLAN3": "IP3",
    "VLAN4": "IP4",
    "VLAN5": "IP5"
}
#print my_dict. items() - wstawiona spacja, bo sie rzucał ze nie usuniete,
# mimo komentarza
#print my_dict
print my_dict.values()
print my_dict.keys()
