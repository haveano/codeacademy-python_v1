"""
For your lists
Perhaps the most useful (and most common) use of for loops is to go through a list.

On each iteration, the variable num will be the next value in the list. So, the first time through, it will be 7, the second time it will be 9, then 12, 54, 99, and then the loop will exit when there are no more values in the list.

Instructions
Write a second for loop that goes through the numbers list and prints each element squared, each on its own line.
"""

numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

# Add your loop below!
for x in numbers:
    print x*x
    
