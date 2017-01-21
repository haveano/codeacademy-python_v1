"""
Pull it Together
Great! Now that you've got your 3 main costs figured out, let's put them together in order to find the total cost of your trip.

def double(n):
    return 2 * n
def triple(p):
    return 3 * p

def add(a, b):
    return double(a) + triple(b)
We define two simple functions, double(n) and triple(p) that return 2 times or 3 times their input. Notice that they have n and p as their arguments.
We define a third function, add(a, b) that returns the sum of the previous two functions when called with a and b, respectively.
Instructions
Below your existing code, define a function called trip_cost that takes two arguments, city and days.
Like the example above, have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.
It is completely valid to call the hotel_cost(nights) function with the variable days. Just like the example above where we call double(n) with the variable a, we pass the value of days to the new function in the argument nights.
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

def rental_car_cost(days):
    cost=40*days
    if days>=7:
        return cost-50
    elif days<7 and days>=3:
        return cost-20
    else:
        return cost

def trip_cost(city,days):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)

print trip_cost("Los Angeles",7)
