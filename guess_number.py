# Guess Number Game
# Author: Kajetan Mroske

import random

computer_number = random.randint(1, 100)

while True:
    user_number = input("Guess the number: ")
    try:
        user_number = int(user_number)
        if user_number > computer_number:
            print("Too big!")
        elif user_number < computer_number:
            print("Too small!")
        else:
            print("You win!")
            break
    except (ValueError, TypeError):
        print("It's not an integer number!")
