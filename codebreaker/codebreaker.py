#
# Codebreaker game (aka cows and bulls)
#

import random

digits = ['0','1','2','3','4','5','6','7','8','9']
random.shuffle(digits)
code = digits[0:4]

print("""
Try to find the secret code in time (4 digits, all different).
I will print an 'x' for each correct digit in the correct position
and will print an 'o' for each correct digit but in the wrong position.
""")
for trial in range(9, 0, -1):
    guess = list(input("({0}) > ".format(trial)))
    if guess == code:
        break
    if len(guess) != len(code):
        print("enter 4 digits")
        continue
    hits = ''
    misses = ''
    for i,d in enumerate(guess):
        if d == code[i]:
            hits += 'x'
        elif d in code:
            misses += 'o'
    print(' '*12 + ''.join((hits, misses)))

if guess == code:
    print("Success")
else:
    print("Times up. code was", code)
