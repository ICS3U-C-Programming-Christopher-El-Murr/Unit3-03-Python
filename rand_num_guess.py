#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 10 16, 2025
# This program asks the user to guess the correct random generated number
import random


def main():
    # generate a random number between 1-9
    number_random = random.randint(0, 9)
    # have the user guess a random number between 1-9
    user_guess = int(input("Guess a number between 0 and 9: "))
    # if the guess = to the random number then display CORRECT! :)
    if user_guess == number_random:
        print("CORRECT! :)")
        # if the guess is not equal to the random number, then display "Guess again :(" and give the user the correct answer
    else:
        print(f"Guess again :(. The correct answer was: {number_random}")


if __name__ == "__main__":
    main()
