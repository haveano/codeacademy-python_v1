"""
List Slicing Syntax
Sometimes we only want part of a Python list. Maybe we only want the first few elements; maybe we only want the last few. Maybe we want every other element!

List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

[start:end:stride]
Where start describes where the slice starts (inclusive), end is where it ends (exclusive), and stride describes the space between items in the sliced list. For example, a stride of 2 would select every other item from the original list to place in the sliced list.

Instructions
We've generated a list with a list comprehension in the editor to the right, and we're about to print a selection from the list using list slicing. Can you guess what will be printed out? Click Save & Submit Code when you think you know!
"""


l = [i ** 2 for i in range(1, 11)]
k = [i ** 2 for i in range(1, 15)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#k = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
print l[2:9:2]
print k[2:13:2]
