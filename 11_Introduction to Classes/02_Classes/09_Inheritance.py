"""
Inheritance
One of the benefits of classes is that we can create more complicated classes that inherit variables or methods from their parent classes. This saves us time and helps us build more complicated objects, since these child classes can also include additional variables or methods.

We define a "child" class that inherits all of the variables and functions from its "parent" class like so:

class ChildClass(ParentClass):
    # new variables and functions go here
Normally we use object as the parent class because it is the most basic type of class, but by specifying a different class, we can inherit more complicated functionality.

Instructions
Create a class ElectricCar that inherits from Car. Give your new class an __init__() method of that includes a "battery_type" member variable in addition to the model, color and mpg.

Then, create an electric car named "my_car" with a "molten salt" battery_type. Supply values of your choice for the other three inputs (model, color and mpg).
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

my_car = ElectricCar("BMW", "black", 200, "molten salt")
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
print my_car.condition
my_car.drive_car()
print my_car.condition
