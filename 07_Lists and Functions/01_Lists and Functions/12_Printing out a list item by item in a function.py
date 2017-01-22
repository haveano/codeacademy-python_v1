"""
Printing out a list item by item in a function
This exercise is to go over how to utilize every element in a list in a function. You can use the existing code to complete the exercise and see how running this operation inside a function isn't much different from running this operation outside a function.

Don't worry about the range function quite yet—we'll explain it later in this section.

Instructions
Define a function called print_list that has one argument called x.
Inside that function, print out each element one by one. Use the existing code as a scaffold.
Then call your function with the argument n.
"""


n = [3, 5, 7]

def print_list(x):
    for y in x:
        print y

print_list(n)

def print_list2(x):
    for i in range(0, len(x)):
        print x[i]

print_list2(n)
