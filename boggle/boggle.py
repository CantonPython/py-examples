from __future__ import print_function
import string
import random
import words
import const

def new_board():
    board = []
    for die in const.dice:
        board.append(random.choice(die))
    random.shuffle(board)
    return board

def show(board):
    for i in range(0, 16, 4):
        print(' '.join(board[i:i+4]))

def make_index(board):
    index = {}
    for letter in string.ascii_lowercase:
        index[letter] = []
    for position,letter in enumerate(board):
        index[letter].append(position)
    return index

def search(word, index, path):
    if not word:
        return path
    for pos in index[word[0]]:
        if not path \
           or pos in const.adjacent[path[-1]] \
           and pos not in path:
            found = search(word[1:], index, path+[pos])
            if found:
                return found
    return None

def solve(board):
    index = make_index(board)
    found = {}
    for word in words.dictionary:
        path = search(word, index, [])
        if path:
            found[word] = path
    return found

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
