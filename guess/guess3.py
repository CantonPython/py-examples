#!/usr/bin/python3
#
# The program picks a random number from 1 to 10 (inclusive). You get three
# guesses to find the secret number. If your guess is wrong, the program let's
# you know if your guess was too low or too high.
#

import random

min_secret = 1
max_secret = 10
max_guesses = 3

def get_guess():
    prompt = "Guess a number from {0} to {1}: ".format(min_secret, max_secret)
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number (or control-d to quit).")

def play():
    secret = random.randint(min_secret, max_secret)
    for trial in range(1, max_guesses+1):
        if trial > 1:
            if guess < secret:
                print("Your guess was too low.")
            else:
                print("Your guess was too high.")
        guess = get_guess()
        if guess == secret:
            print("You won!")
            return
    print("Sorry, better luck next time.")

def ask(msg):
    answer = input(msg).lower()
    if answer == 'y' or answer == 'yes':
        return True
    else:
        return False

def main():
    while True:
        try:
            play()
            if not ask("Play again? (y/n) "):
                break
        except (EOFError, KeyboardInterrupt):
            break
    print("Thanks for playing.")

if __name__ == '__main__':
    main()

