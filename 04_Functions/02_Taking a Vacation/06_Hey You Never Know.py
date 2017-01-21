"""
Hey, You Never Know!
You can't expect to only spend money on the plane ride, hotel, and rental car when going on a vacation. There also needs to be room for additional costs like fancy food or souvenirs.

Instructions
Modify your trip_cost function definition. Add a third argument, spending_money.
Modify what the trip_cost function does. Add the variable spending_money to the sum that it returns.
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

print trip_cost("Los Angeles",7,678)
