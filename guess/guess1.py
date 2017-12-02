
#
# The program picks a random number between 1 and 10.
# You get three guess to find the secret number. If
# your guess is wrong, the program let's you know if
# your guess was too low or too high.
#

import random

secret = random.randint(1, 10)

for trial in range(1, 4):
    guess = int(input("Pick a number between 1 and 10: "))
    if guess < secret:
        print("Sorry, your guess was too low.")
    elif guess > secret:
        print("Sorry, your guess was too high.")
    else:
        break

if guess == secret:
    print("You got it!")
else:
    print("Better luck next time (loser)")
