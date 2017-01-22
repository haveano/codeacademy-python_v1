"""
Iterating over a list in a function
Now that we've learned about range, we have two ways of iterating through a list.

Method 1 - for item in list:

for item in list:
    print item
Method 2 - iterate through indexes:

for i in range(len(list)):
    print list[i]
Method 1 is useful to loop through the list, but it's not possible to modify the list this way. Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed. Since we aren't modifying the list, feel free to use either one on this lesson!

Instructions
Create a function that returns the sum of a list of numbers.

On line 3, define a function called total that accepts one argument called numbers. It will be a list.
Inside the function, create a variable called result and set it to zero.
Using one of the two methods above, iterate through the numbers list.
For each number, add it to result.
Finally, return result.
Create a function called total that adds up all the elements of an arbitrary list and returns that count, using the existing code as a hint. Use a for loop so it can be used for any size list.
"""


n = [3, 5, 7]

def total(numbers):
    result=0
    for i in numbers:
        result=result+i
    return result
print total(n)
