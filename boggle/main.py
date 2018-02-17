import string
import boggle

def make_index(board):
    index = {}
    for letter in string.ascii_lowercase:
        index[letter] = []
    for i,letter in enumerate(board):
        index[letter].append(i)
    return index

def find_word(index, word):
    first = word[0]
    rest = word[1:]
    for i in index[first]:
        found = find_subword(index, [i], rest)
        if found:
            return found
    return None

def find_subword(index, path, word):
    if not word:
        return path
    first = word[0]
    rest = word[1:]
    tail = path[-1]
    adjacent = boggle.adjacent[tail]
    for i in index[first]:
        if i in adjacent and i not in path:
            found = find_subword(index, path+[i], rest)
            if found:
                return found
    return None

def solve(board):
    solution = {}
    index = make_index(board)
    for word in boggle.words:
        path = find_word(index, word)
        if path:
            solution[word] = path
    return solution

def main():
    board = boggle.new_board()
    boggle.show_board(board)
    guess = set()
    print('? = show board, . = quit')
    while True:
        w = input("boggle> ").strip()
        if w == '.':
            break
        elif w == '?':
            boggle.show_board(board)
        else:
            guess.add(w)
    solution = set(solve(board).keys())
    print("found: ", guess & solution)
    print("missed: ", solution - guess)

if __name__ == '__main__':
    main()
