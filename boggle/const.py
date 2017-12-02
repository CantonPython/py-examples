
#
# 4 x 4 adjacency table
#
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

# 16 boggle dice. Note q implies qu
dice = (
    'ednosw', 'aaciot', 'acelrs', 'ehinps',
    'eefhiy', 'elpstu', 'acdemp', 'gilruw',
    'egkluy', 'ahmors', 'abilty', 'adenvz',
    'bfiorx', 'dknotu', 'abjmoq', 'egintv',
)
