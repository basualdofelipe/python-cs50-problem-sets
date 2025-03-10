#https://cs50.harvard.edu/python/2022/psets/4/game/

import random


def main():
    level = input_number("Level: ")
    secret_number = random.randint(1, level)
    while True:
        guess = input_number("Guess: ")

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break


def input_number(text):
    while True:
        try:
            number = int(input(text))
            break
        except ValueError:
            pass
    return number


main()