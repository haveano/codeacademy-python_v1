"""
Simple errors
A common application of a while loop is to check user input to see if it is valid. For example, if you ask the user to enter y or n and they instead enter 7, then you should re-prompt them for input.

Instructions
Fill in the loop condition so the user will be prompted for a choice over and over while choice does not equal 'y' and choice does not equal 'n'.
"""

choice = raw_input('Enjoying the course? (y/n)')

while choice!="n" and choice!="y":  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

