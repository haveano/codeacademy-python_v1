"""
Modifying an element of a list in a function
Modifying an element in a list in a function is the same as if you were just modifying an element of a list outside a function.

def double_first(n):
    n[0] = n[0] * 2

numbers = [1, 2, 3, 4]
double_first(numbers)
print numbers
We create a list called numbers.
We use the double_first function to modify that list.
Finally, we print out [2, 2, 3, 4]
When we pass a list to a function and modify that list, like in the double_first function above, we end up modifying the original list.

Instructions
Change list_function so that:

Add 3 to the item at index one of the list.
Store the result back into index one.
Return the list.
"""

def list_function(x):
    x[1]=x[1]+3
    return x

n = [3, 5, 7]
print list_function(n)
