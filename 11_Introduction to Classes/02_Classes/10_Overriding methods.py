"""
Overriding methods
Since our ElectricCar is a more specialized type of Car, we can give the ElectricCar its own drive_car() method that has different functionality than the original Car class's.

Instructions
Inside ElectricCar add a new method drive_car() that changes the car's condition to the string "like new".
Then, outside of ElectricCar, print the condition of my_car
Next, drive my_car by calling the drive_car() function
Finally, print the condition of my_car again
"""



class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print "This is a %s %s with %d MPG." % (self.color, self.model, self.mpg)
    def drive_car(self):
        self.condition="used"

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type=battery_type
    def drive_car(self):
        self.condition="like new"

my_car = ElectricCar("BMW", "black", 200, "molten salt")
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
print my_car.condition
my_car.drive_car()
print my_car.condition
