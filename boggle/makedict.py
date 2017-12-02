import string

DICT = '/usr/share/dict/american-english'
MIN_LENGTH = 3

def is_lower(word):
    for letter in word:
        if letter not in string.ascii_lowercase:
            return False
    return True

def read_dictionary(filename):
    words = []
    with open(filename, 'r', encoding='utf-8') as file:
        for word in file:
            word = word.rstrip()
            if MIN_LENGTH <= len(word) and is_lower(word):
                words.append(word)
    return words

def write_words(filename, words):
    with open(filename, 'w') as file:
        file.write("dictionary = (\n")
        for word in words:
            file.write("'{}',\n".format(word))
        file.write(")\n")

write_words('words.py', read_dictionary(DICT))
