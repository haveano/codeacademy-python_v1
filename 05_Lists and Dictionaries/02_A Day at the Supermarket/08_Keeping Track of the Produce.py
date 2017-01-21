"""
Keeping Track of the Produce
Now that you have all of your product info, you should print out all of your inventory information.

once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
    print "Once: %s" % once[key]
    print "Twice: %s" % twice[key]
In the above example, we create two dictionaries, once and twice, that have the same keys.
Because we know that they have the same keys, we can loop through one dictionary and print values from both once and twice.
Instructions
Loop through each key in prices.
Like the example above, for each key, print out the key along with its price and stock information. Print the answer in the following format:
apple
price: 2
stock: 0
Like the example above, because you know that the prices and stock dictionary have the same keys, you can access the stock dictionary while you are looping through prices.

When you're printing, you can use the syntax from the example above.
"""


prices={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for y in prices:
    print y
    print "price: %s" % prices[y]
    print "stock: %s" % stock[y]
