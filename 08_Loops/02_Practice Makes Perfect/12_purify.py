"""
purify
Awesome! Now let's practice filtering a list.

Instructions
Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.

For example, purify([1,2,3]) should return [2].

Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.
"""


def purify(lst):
    lst2=[]
    for x in lst:
        if x%2==0:
            lst2.append(x)
    return lst2
    
print purify([1,2,3,4,5])
