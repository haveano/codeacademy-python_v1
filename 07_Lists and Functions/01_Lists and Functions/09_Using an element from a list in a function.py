"""
Using an element from a list in a function
Passing a list to a function will store it in the argument (just like with a string or a number!)

def first_item(items):
    print items[0]

numbers = [2, 7, 9]
first_item(numbers)
In the example above, we define a function called first_item. It has one argument called items.
Inside the function, we print out the item stored at index zero of items.
After the function, we create a new list called numbers.
Finally, we call the first_item function with numbers as its argument, which prints out 2.
Instructions
Change line 2 so that list_function returns only the item stored in index one of x, rather than the entire x list.
"""

def list_function(x):
    return x[1]

n = [3, 5, 7]
print list_function(n)
