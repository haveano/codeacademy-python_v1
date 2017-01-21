"""
Stocking Out
Now you need your compute_bill function to take the stock/inventory of a particular item into account when computing the cost.

Ultimately, if an item isn't in stock, then it shouldn't be included in the total. You can't buy or sell what you don't have!

Instructions
Make the following changes to your compute_bill function:

While you loop through each item of food, only add the price of the item to total if the item's stock count is greater than zero.
If the item is in stock and after you add the price to the total, subtract one from the item's stock count.
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
        if stock[x]>0:
            print "jest", x
            total=total+prices[x]
            stock[x]=stock[x]-1
        else:
            print "nie ma", x
    return total

zakupy=["banana","gowno","kupa","apple"]
#compute_bill(zakupy)
print stock
#print compute_bill(shopping_list)
print stock


