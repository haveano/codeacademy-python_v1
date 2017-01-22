"""
Using strings in lists in functions
Now let's try working with strings!

for item in list:
    print item

for i in range(len(list)):
    print list[i]
The example above is just a reminder of the two methods for iterating over a list.

Instructions
Create a function that concatenates strings.

Define a function called join_strings accepts an argument called words. It will be a list.
Inside the function, create a variable called result and set it to "", an empty string.
Iterate through the words list and append each word to result.
Finally, return the result.
Don't add spaces between the joined strings!
"""

n = ["Michael", "Lieberman"]
# Add your function here

def join_strings(words):
    result=""
    for w in words:
        result=result+w
    return result



print join_strings(n)
