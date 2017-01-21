"""
Plan Your Trip!
Nice work! Now that you have it all together, let's take a trip.

What if we went to Los Angeles for 5 days and brought an extra 600 dollars of spending money?

Instructions
After your previous code, print out the trip_cost( to "Los Angeles" for 5 days with an extra 600 dollars of spending money.

Don't forget the closing ) after passing in the 3 previous values!
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

def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)\
    +plane_ride_cost(city)+spending_money

print trip_cost("Los Angeles",5,600)
