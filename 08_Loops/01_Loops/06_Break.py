"""
Break
The break is a one-line statement that means "exit the current loop." An alternate way to make our counting loop exit and stop executing is with the break statement.

First, create a while with a condition that is always true. The simplest way is shown.

Using an if statement, you define the stopping condition. Inside the if, you write break, meaning "exit the loop."

The difference here is that this loop is guaranteed to run at least once.

Instructions
See what the break does? Feel free to mess around with it (but make sure you don't cause an infinite loop)! Click Save & Submit Code when you're ready to continue.
"""


count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break
