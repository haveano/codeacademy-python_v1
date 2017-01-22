"""
Condition
The condition is the expression that decides whether the loop is going to be executed or not. There are 5 steps to this program:

The loop_condition variable is set to True

The while loop checks to see if loop_condition is True. It is, so the loop is entered.

The print statement is executed.

The variable loop_condition is set to False.

The while loop again checks to see if loop_condition is True. It is not, so the loop is not executed a second time.

Instructions
See how the loop checks its condition, and when it stops executing? When you think you've got the hang of it, click Save & Submit Code to continue.
"""

loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False
