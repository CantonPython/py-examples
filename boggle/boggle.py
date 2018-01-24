from __future__ import print_function
import string
import random
import words

# 4 x 4 adjacency table
#   0   1   2   3
#   4   5   6   7
#   8   9  10  11
#  12  13  14  15
adjacent = {
    0: (1, 4, 5),
    1: (0, 2, 4, 5, 6),
    2: (1, 3, 5, 6, 7),
    3: (2, 6, 7),
    4: (0, 1, 5, 8, 9),
    5: (0, 1, 2, 4, 6, 8, 9, 10),
    6: (1, 2, 3, 5, 7, 9, 10, 11),
    7: (2, 3, 6, 10, 11),
    8: (4, 5, 9, 12, 13),
    9: (4, 5, 6, 8, 10, 12, 13, 14),
    10: (5, 6, 7, 9, 11, 13, 14, 15),
    11: (6, 7, 10, 14, 15),
    12: (8, 9, 13),
    13: (8, 9, 10, 12, 14),
    14: (9, 10, 11, 13, 15),
    15: (10, 11, 14),
}

# boggle dice. (Note 'q' should imply 'qu'.)
dice = [
    'ednosw', 'aaciot', 'acelrs', 'ehinps',
    'eefhiy', 'elpstu', 'acdemp', 'gilruw',
    'egkluy', 'ahmors', 'abilty', 'adenvz',
    'bfiorx', 'dknotu', 'abjmoq', 'egintv',
]

def new_board():
    random.shuffle(dice)
    board = []
    for d in dice:
        board.append(random.choice(d))
    return board

def show(board):
    # assumes 4x4
    for i in range(0, 16, 4):
        print(' '.join(board[i:i+4]))

def make_index(board):
    index = {}
    for letter in string.ascii_lowercase:
        index[letter] = []
    for i,letter in enumerate(board):
        index[letter].append(i)
    return index

def find_word(index, word):
    assert(word)
    first,rest = word[0],word[1:]
    for i in index[first]:
        found = find_subword(index, [i], rest)
        if found:
            return found
    return None

def find_subword(index, path, word):
    assert(path)
    if not word:
        return path
    tail = path[-1]
    first,rest = word[0],word[1:]
    for i in index[first]:
        if i in adjacent[tail] and i not in path:
            found = find_subword(index, path+[i], rest)
            if found:
                return found
    return None

def solve(board):
    solution = {}
    index = make_index(board)
    for word in words.dictionary:
        path = find_word(index, word)
        if path:
            solution[word] = path
    return solution

if __name__ == '__main__':
    board = new_board()
    show(board)
    guess = set()
    print('? = show board, . = quit')
    while True:
        w = input("boggle> ").strip()
        if w == '.':
            break
        elif w == '?':
            show(board)
        else:
            guess.add(w)
    solution = set(solve(board).keys())
    print("found: ", guess & solution)
    print("missed: ", solution - guess)
