
#
# The program picks a random number between 1 and 10.
# You get three guesses to find the secret number. If
# your guess is wrong, the program let's you know if
# your guess was too low or too high.
#

import random
MIN = 1
MAX = 10

class QuitGame(Exception):
    pass

def number_prompt(msg):
    while True:
        try:
            guess = input(msg)
            if guess.lower() == 'quit' or guess.lower() == 'q':
                raise QuitGame
            guess = int(guess)
            if MIN <= guess <= MAX:
                return guess
        except ValueError:
            print("Please enter a number (or control-d to quit)")
        except EOFError:
            raise QuitGame

def question_prompt(msg):
    try:
        answer = input(msg).lower()
        if answer == 'yes' or answer == 'y':
            return True
        else:
            return False
    except EOFError:
        raise QuitGame

def play():
    secret = random.randint(1, 10)
    for trial in range(1, 4):
        guess = number_prompt("Guess a number between {0} and {1}: ".format(MIN,MAX))
        if guess < secret:
            print("Sorry, your guess was too low.")
        elif guess > secret:
            print("Sorry, your guess was too high.")
        else:
            print("You got it!")
            return
    print("Better luck next time.")

def main():
    try:
        while True:
            play()
            if not question_prompt("Play again? "):
                raise QuitGame
    except QuitGame:
        print()
        print("Thanks for playing.")

main()
