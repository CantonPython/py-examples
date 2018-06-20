"""
Boggle word game.
"""

import random
import string

class Boggle:

    # Note: 'q' implies 'qu'.
    DICE = [
        'ednosw', 'aaciot', 'acelrs', 'ehinps',
        'eefhiy', 'elpstu', 'acdemp', 'gilruw',
        'egkluy', 'ahmors', 'abilty', 'adenvz',
        'bfiorx', 'dknotu', 'abjmoq', 'egintv',
    ]

    # Adjacency table for a 4 by 4 board. This should
    # be generated for an arbitrary sized board.
    ADJACENT = {
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

    def __init__(self):
        """Create a new board."""
        self.roll_dice()
        self.make_index()

    def roll_dice(self):
        """Roll the dice to make a new random board."""
        dice = self.DICE[:]
        random.shuffle(dice)
        self.board = []
        for die in dice:
            letter = random.choice(die)
            self.board.append(letter)

    def make_index(self):
        """Generate the index table for find_word."""
        self.index = {}
        for letter in string.ascii_lowercase:
            self.index[letter] = []
        for i,letter in enumerate(self.board):
            self.index[letter].append(i)

    def __repr__(self):
        """Text representation of the board."""
        rows = []
        for i in range(0, 16, 4):
            row = self.board[i:i+4]
            rows.append(' '.join(row))
        return "\n".join(rows)

    def find_word(self, word):
        """Find the word on the board if it exists."""
        first = word[0]
        rest = word[1:]
        for i in self.index[first]:
            found = self.find_subword([i], rest)
            if found:
                return found
        return None

    def find_subword(self, path, word):
        """Find the remaining letters of a word on the board."""
        if not word:
            return path
        first = word[0]
        rest = word[1:]
        tail = path[-1]
        adjacent = self.ADJACENT[tail]
        for i in self.index[first]:
            if i in adjacent and i not in path:
                found = self.find_subword(path+[i], rest)
                if found:
                    return found
        return None

    def solve(self):
        """Find all the words on the board."""
        self.solution = {}
        with open('words.txt') as words:
            for word in words:
                word = word.strip()
                path = self.find_word(word)
                if path:
                    self.solution[word] = path
        return self.solution

def main():
    """Test driver for the boggle game."""
    boggle = Boggle()
    solution = boggle.solve()
    words = set(solution.keys())
    guessed = set()
    print(boggle)
    print("Type words or 'q' to quit.")
    while True:
        word = input("boggle> ").strip().lower()
        if word == 'q':
            break
        guessed.add(word)
    print("found:  ", words & guessed)
    print("missed: ", words - guessed)

if __name__ == '__main__':
    main()
