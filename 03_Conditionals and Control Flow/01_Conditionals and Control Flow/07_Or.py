"""
Or
The boolean operator or returns True when at least one expression on either side of or is true. For example:

1 < 2 or 2 > 3 is True;
1 > 2 or 2 > 3 is False.
Instructions
Time to practice with or!

Set bool_one equal to the result of 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'
Set bool_two equal to the result of True or False
Set bool_three equal to the result of 100**0.5 >= 50 or False
Set bool_four equal to the result of True or True
Set bool_five equal to the result of 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
"""
bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'
print bool_one
bool_two = True or False
print bool_two
bool_three = 100**0.5 >= 50 or False
print bool_three
bool_four = True or True
print bool_four
bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
print bool_five
