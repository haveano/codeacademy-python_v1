"""
This and That (or This, But Not That!)
Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.
For example, True or not False and False returns True. If this isn't clear, look at the Hint.

Parentheses () ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.
"""
bool_one = False or not True and True
print bool_one
bool_two = False and not True or True
print bool_two
bool_three = True and not (False or False)
print bool_three
bool_four = not not True or False and not True
print bool_four
bool_five = False or not (True and True)
print bool_five
