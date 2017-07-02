# Program that generates numbers 1-100/ High Low Game.
# 7-2-2017
# CTI-110 M5HW2 - Random Number Guessing Game
# Bobby McFadden

import random

rd = random.randint(1,100)
guess = 0
c = 0
while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 100:")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!")
        print("You took only", c, "tries!")
input()
