"""
Infinite loops
An infinite loop is a loop that never exits. This can happen for a few reasons:

The loop condition cannot possibly be false (e.g. while 1 != 2)

The logic of the loop prevents the loop condition from becoming false.

Example:

count = 10
while count > 0:
    count += 1 # Instead of count -= 1
Instructions
The loop in the editor has two problems: it's missing a colon (a syntax error) and count is never incremented (logical error). The latter will result in an infinite loop, so be sure to fix both before running!
"""


count = 0

while count < 10: # Add a colon
    print count
    count+=1# Increment count
