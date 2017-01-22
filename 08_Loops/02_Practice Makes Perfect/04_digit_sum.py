"""
digit_sum
Awesome! Now let's try something a little trickier. Try summing the digits of a number.

Instructions
Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.

For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.

(Assume that the number you are given will always be positive.)

Check the hint if you need help!
"""


def digit_sum_pomocnicza(k):
    z=0
    for i in str(k):
        z=z+int(i)
    return z

def digit_sum(x):
    z=0
    if x>=0:
        z=digit_sum_pomocnicza(x)
    else:
        z=digit_sum_pomocnicza(x*-1)*-1
    return z

"""
print digit_sum(12)
print digit_sum(-212)
print digit_sum_pomocnicza(12)
print digit_sum_pomocnicza(212)
"""
