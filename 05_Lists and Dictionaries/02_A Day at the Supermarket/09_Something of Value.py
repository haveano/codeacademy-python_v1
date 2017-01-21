"""
Something of Value
For paperwork and accounting purposes, let's record the total value of your inventory. It's nice to know what we're worth!

Instructions
Let's determine how much money you would make if you sold all of your food.

Create a variable called total and set it to zero.
Loop through the prices dictionaries.
For each key in prices, multiply the number in prices by the number in stock. Print that value into the console and then add it to total.
Finally, outside your loop, print total.
"""

prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}
total=0
for x in prices:
#    print key
#    print "price: %s" % prices[x]
#    print "stock: %s" % stock[x]
    print total
    total=total+prices[x]*stock[x]
print "calosc: %s" % total
