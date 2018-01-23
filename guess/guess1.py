
#
# The program picks a random number between 1 and 10.
# You get three guesses to find the secret number. If
# your guess is wrong, the program let's you know if
# your guess was too low or too high.
#

import random

secret = random.randint(1, 10)
trial = 1
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret:
        print("You got it!")
        break
    if trial == 3:
        print("Better luck next time.")
        break
    if guess < secret:
        print("Your guess was too low.")
    elif guess > secret:
        print("Your guess was too high.")
    trial += 1
