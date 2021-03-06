"""
Part of the Whole
Good! Now let's calculate the class average.

You need to get the average for each student and then calculate the average of those averages.

Instructions
Define a function called get_class_average that has one argument students. You can expect students to be a list containing your three students.
First, make an empty list called results.
For each student item in the class list, calculate get_average(student) and then call results.append() with that result.
Finally, return the result of calling average() with results.
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

def get_class_average(studenci):
    results=[]
    for x in studenci:
        results.append(get_average(x))
    return average(results)

students=[lloyd,alice,tyler]

for x in students:
    print "srednia ucznia",x["name"],"to:",get_average(x)
    print "ocena ucznia",x["name"],"to:",get_letter_grade(get_average(x))
    #print x["name"]
    #print x["homework"]
    #print x["quizzes"]
    #print x["tests"]
  
#print get_average(lloyd)
#print get_letter_grade(80)
#print get_letter_grade(get_average(lloyd))
