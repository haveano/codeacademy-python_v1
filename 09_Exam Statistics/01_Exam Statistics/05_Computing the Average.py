"""
Computing the Average
The average test grade can be found by dividing the sum of the grades by the total number of grades.

Luckily, we just created an awesome function, grades_sum() to compute the sum.

Instructions
Define a function grades_average(), below the grades_sum() function that does the following:

Has one argument, grades, a list
Calls grades_sum with grades
Computes the average of the grades by dividing that sum by float(len(grades)).
Returns the average.
Call the newly created grades_average() function with the list of grades and print the result.
"""


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    y=0
    for x in scores:
        y=y+x
    return y
print grades_sum(grades)

def grades_average(grades):
    return grades_sum(grades)/float(len(grades))
print grades_average(grades)
