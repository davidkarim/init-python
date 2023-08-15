#!/usr/bin/env python3

# Define variable holding random number between 1 and 10
# Ask user to guess random number

from random import randint

random_number = randint(1, 10)
print(random_number)
guess = int(input("Guess a number between 1 and 10: "))

# Give user 2 more chances to guess correctly
for i in range(2):
    if guess == random_number:
        print("You win!")
        break
    else:
        guess = int(input("Guess again: "))

# If user doesn't guess correctly after 3 tries, print "You lose!"
if guess != random_number:
    print("You lose!")
