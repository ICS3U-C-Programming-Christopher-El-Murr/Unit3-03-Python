#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 10 16, 2025
# This program asks the user to guess the correct number
import constants


def main():
    # ask user for their number guess
    number_guess = int(input("Enter the number:"))
    # tell the user if the number is correct
    if number_guess == constants.number:
        print("CORRECT, THE NUMBER IS 9 :)")
    else:
        # tell the user to guess again
        print("Guess again :(")


if __name__ == "__main__":

    main()
