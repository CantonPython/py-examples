from __future__ import print_function
import random
import words

def sig(word):
    return ''.join(sorted(list(word)))

def make_index():
    index = {}
    for word in words.dictionary:
        index.setdefault(sig(word), []).append(word)
    return index

def jumble(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def unjumble(index, word):
    return index.get(sig(word))

def new_puzzle():
    return jumble(random.choice(words.dictionary))

index = make_index()
def solve(jumbled):
    words = unjumble(index, jumbled)
    if not words:
        print("Could not find word for jumble", jumbled)
    elif len(words) > 1:
        print("Found words:", ", ".join(words))
    else:
        print("Found word:", words[0])
