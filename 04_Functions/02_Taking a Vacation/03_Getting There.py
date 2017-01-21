"""
Getting There
You're going to need to take a plane ride to get to your location.

def fruit_color(fruit):
    if fruit == "apple":
        return "red"
    elif fruit == "banana":
        return "yellow"
    elif fruit == "pear":
        return "green"
The example above defines the function fruit_color that accepts a string as the argument fruit.
The function returns a string if it knows the color of that fruit.
Instructions
Below your existing code, define a function called plane_ride_cost that takes a string, city, as input.
The function should return a different price depending on the location, similar to the code example above. Below are the valid destinations and their corresponding round-trip prices.
"Charlotte": 183
"Tampa": 220
"Pittsburgh": 222
"Los Angeles": 475
"""

def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475
    else:
        return 0
