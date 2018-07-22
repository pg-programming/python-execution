#!/usr/bin/env python


# import some modules so that we get some extra functionality
# (don't worry about this yet)
import os
import sys
from datetime import datetime

# clear the console screen
os.system('clear')

# print the message
# the comma at the end ensures that we don't get a newline after the message
print('Hello, what is your name? ', end='')

# collect the user input into a variable
name = input()

# print the response using string concatenation
# the \n is the special character for a newline
print('\nIt is a pleasure to meet you ' + name + '!\n')

# tell the user how long the name is
print('Your name is ' + str(len(name)) + ' characters long\n')

print('How old are you? ', end='')

# convert the input to a number (this could fail if the input isn't a number)
age = int(input())

print('\nAnd have you already had a birthday this year (y/n)? ', end='')

# get the answer concerning the past birthday and save it as a boolean
past_birthday = input()

# change the 'y' or 'n' to a True or False
if past_birthday == 'y':
    # go ahead and use the same variable if you want. Just don't get mixed up
    past_birthday = True
elif past_birthday == 'n':
    past_birthday = False
else:
    # make sure that you use the right quotes (' vs ")
    print("\nI didn't understand your response.")
    input('\nPress enter to quit...')
    # clear the console screen
    os.system('clear')
    # exit the program
    sys.exit()

# calculate the year
# an 'if' statement can be on a single line like this
# The parentheses are to enforce a specific order of operations. Without them
# this expression will not evaluate correctly.
year = datetime.now().year - age - (0 if past_birthday else 1)

# I used datetime to get the current year but you don't need to be so fancy

# convert the number back to a string. You can't add a number and a string
print('\nI know what year you were born in. It was ' + str(year) + '.')

# wait for the user to press enter to quit
input('\nPress enter to quit...')

# clear the console screen
os.system('clear')
