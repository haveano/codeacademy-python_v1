"""
Sending a Letter
Great work!

Now let's write a get_letter_grade function that takes a number score as input and returns a string with the letter grade that that student should receive.

Instructions
Define a new function called get_letter_grade that has one argument called score. Expect score to be a number.
Inside your function, test score using a chain of if: / elif: / else: statements, like so:

If score is 90 or above: return "A"
Else if score is 80 or above: return "B"
Else if score is 70 or above: return "C"
Else if score is 60 or above: return "D"
Otherwise: return "F"

Finally, test your function! Call your get_letter_grade function with the result of get_average(lloyd). Print the resulting letter grade.
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

def get_average(student):
    homework=average(student["homework"])
    quizzes=average(student["quizzes"])
    tests=average(student["tests"])
    srednia=0.1*homework+0.3*quizzes+0.6*tests
    return srednia
def get_letter_grade(score):
    if score>=90 and score<=100:
        return "A"
    elif score>=80 and score<90:
        return "B"
    elif score>=70 and score<80:
        return "C"
    elif score>=60 and score<70:
        return "D"
    elif score>=0 and score<60:
        return "F"
    else:
        print "zle dane wejsciowe"
        return "-1"
#print get_average(lloyd)
#print get_letter_grade(80)
#print get_letter_grade(get_average(lloyd))
students=[lloyd,alice,tyler]
#print students

for x in students:
    print "srednia ucznia",x["name"],"to:",get_average(x)
    print "ocena ucznia",x["name"],"to:",get_letter_grade(get_average(x))
    #print x["name"]
    #print x["homework"]
    #print x["quizzes"]
    #print x["tests"]
