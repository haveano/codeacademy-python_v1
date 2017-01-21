"""
Let's Check Out!
Perfect! You've done a great job with lists and dictionaries in this project. You've practiced:

Using for loops with lists and dictionaries
Writing functions with loops, lists, and dictionaries
Updating data in response to changes in the environment (for instance, decreasing the number of bananas in stock by 1 when you sell one).
Thanks for shopping at the Codecademy supermarket!

Instructions
Click Save & Submit Code to finish this course.
"""


shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total=0
    for x in food:
#        print x
        if x in stock and stock[x]>0:
            print "jest", stock[x], "sztuk", x
            total=total+prices[x]
            stock[x]=stock[x]-1
        else:
            print "nie ma",x
    return total

zakupy=["banana","gowno","kupa","apple"]
print stock
print compute_bill(zakupy),"$"
print compute_bill(shopping_list)
print stock
#print stock.keys()
