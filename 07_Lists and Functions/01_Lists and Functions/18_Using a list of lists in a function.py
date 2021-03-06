"""
Using a list of lists in a function
Finally, this exercise shows how to make use of a single list that contains multiple lists and how to use them in a function.

list_of_lists = [[1,2,3], [4,5,6]]

for lst in list_of_lists:
    for item in lst:
        print item
In the example above, we first create a list containing two items, each of which is a list of numbers.
Then, we iterate through our outer list.
For each of the two inner lists (as lst), we iterate through the numbers (as item) and print them out.
We end up printing out:

1
2
3
4
5
6
Instructions
Create a function called flatten that takes a single list and concatenates all the sublists that are part of it into a single list.

On line 3, define a function called flatten with one argument called lists.
Make a new, empty list called results.
Iterate through lists. Call the looping variable numbers.
Iterate through numbers.
For each number, .append() it to results.
Finally, return results from your function.
"""


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
    results=[]
    for numbers in lists:
            for n in numbers:
                results.append(n)
    return results

print flatten(n)
