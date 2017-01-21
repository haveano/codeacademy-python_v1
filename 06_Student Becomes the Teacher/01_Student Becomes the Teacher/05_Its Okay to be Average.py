"""
It's Okay to be Average
When teaching a class, it's important to take the students' averages in order to assign grades.

5 / 2
# 2

5.0 / 2
# 2.5

float(5) / 2
# 2.5
The above example is a reminder of how division works in Python.

When you divide an integer by another integer, the result is always an integer (rounded down, if needed).
When you divide a float by an integer, the result is always a float.
To divide two integers and end up with a float, you must first use float() to convert one of the integers to a float.
Instructions
Write a function average that takes a list of numbers and returns the average.

Define a function called average that has one argument, numbers.
Inside that function, call the built-in sum() function with the numbers list as a parameter. Store the result in a variable called total.
Like the example above, use float() to convert total and store the result in total.
Divide total by the length of the numbers list. Use the built-in len() function to calculate that.
Return that result.
"""


lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total=float(sum(numbers))/len(numbers)
    #total=sum(numbers)
    #total=float(total)/len(numbers)
    return total
    
