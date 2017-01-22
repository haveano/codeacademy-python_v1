"""
is_prime
A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. (Boy, that's a mouthful.)

In other words, if you want to test if a number in a variable x is prime, then no other number should go into x evenly besides 1 and x. So 2 and 5 and 11 are all prime, but 4 and 18 and 21 are not.

If there is a number between 1 and x that goes in evenly, then x is not prime.

Instructions
Define a function called is_prime that takes a number x as input.
For each number n from 2 to x - 1, test if x is evenly divisible by n.
If it is, return False.
If none of them are, then return True.
"""


def is_prime(x):
    if x<=1:
        return False
    else:
        znacznik=True
        for n in xrange(2, x):
            print n
            if x%n==0:
                print "print1",x,n
                return False
                break
            else:
                znacznik=True
        return znacznik
"""
print "dla 2:", is_prime(2)
print "dla 3:", is_prime(3)
print "dla 4:", is_prime(4)
print "dla 9:", is_prime(9)
"""
print "dla 11:", is_prime(11)
"""
for n in xrange (2,11):
    print n
"""
