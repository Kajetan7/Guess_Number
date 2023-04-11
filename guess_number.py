# Guess Number Game
# Author: Kajetan Mroske

import random

computer_number = random.randint(1, 100)  # Computer picks random integer from 1 to 100

while True:  # Loop which can be broken only when player wins.
    user_number = input("Guess the number: ")  # Player picks number and approve it with enter.
    try:
        user_number = int(user_number)  # User input is string - needs conversion for logical operations.
        if user_number > computer_number:
            print("Too big!")
        elif user_number < computer_number:
            print("Too small!")
        else:
            print("You win!")
            break
    except (ValueError, TypeError):
        print("It's not an integer number!")  # If number is not an integer - error occurs.
