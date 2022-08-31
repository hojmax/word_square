from pickle import GLOBAL
import re
import numpy as np


def create_character_tree(dictionary):
    root = {}

    for word in dictionary:
        current = root
        for letter in word:
            current = current.setdefault(letter, {})

    return root


def get_top_words(amount, filename):
    data = np.genfromtxt(
        filename,
        dtype=str,
        delimiter=',',
        skip_header=1
    )
    data = data.astype('object')

    return data[:amount, 0]


def is_flippable(word, dictionary):
    return word[::-1] in dictionary


def get_filtered_dictionary(dictionary, word_length):
    lookup = set(dictionary)

    def is_valid(word):
        return len(word) == word_length and re.match("^[a-z]+$", word) and is_flippable(word, lookup)

    return list(filter(is_valid, dictionary))


def get_dictionary(filename):
    with open(filename) as f:
        return f.read().splitlines()


def get_column_possibilities(character_tree, word_square, x):
    current = character_tree

    for word in word_square:
        if word[x] not in current:
            return []

        current = current[word[x]]

    return current.keys()


def restricted_word_search(partial_word, character_restrictions, character_tree, container, square_size):
    if len(partial_word) == square_size:
        return container.append(partial_word)

    for character in character_restrictions[len(partial_word)]:
        if character in character_tree:
            restricted_word_search(
                partial_word + character,
                character_restrictions,
                character_tree[character],
                container,
                square_size
            )


def print_word_square(word_square):
    for word in word_square:
        print(' '.join(list(word.upper())))
    print()


def get_possible_words(word_square, character_tree, square_size):
    column_possibilities = [
        get_column_possibilities(
            character_tree,
            word_square,
            x
        ) for x in range(square_size)
    ]
    possible_words = []
    restricted_word_search(
        '',
        column_possibilities,
        character_tree,
        possible_words,
        square_size
    )

    return possible_words


def tree_search(
    dictionary,
    character_tree,
    word_square,
    square_size,
    container
):
    if len(word_square) == square_size:
        return container.append(word_square)

    possible_words = (
        dictionary
        if len(word_square) == 0
        else get_possible_words(
            word_square, character_tree, square_size
        )
    )

    for word in possible_words:
        tree_search(
            dictionary,
            character_tree,
            word_square + [word],
            square_size,
            container
        )


def get_halfable_words(dictionary, half_dictionary, square_size):
    lookup = set(half_dictionary)

    def is_valid(word):
        return word[:square_size//2] in lookup and word[square_size//2:] in lookup

    return list(filter(is_valid, dictionary))


if __name__ == "__main__":
    all_solutions = []
    square_size = 4
    dictionary = get_dictionary("dictionary1.txt")
    dictionary_half = [
        'AA',
        'AB',
        'AD',
        'AE',
        'AG',
        'AH',
        'AI',
        'AL',
        'AM',
        'AN',
        'AR',
        'AS',
        'AT',
        'AW',
        'AX',
        'AY',
        'BA',
        'BE',
        'BI',
        'BO',
        'BY',
        'DA',
        'DE',
        'DO',
        'ED',
        'EF',
        'EH',
        'EL',
        'EM',
        'EN',
        'ER',
        'ES',
        'ET',
        'EW',
        'EX',
        'FA',
        'FE',
        'GI',
        'GO',
        'HA',
        'HE',
        'HI',
        'HM',
        'HO',
        'ID',
        'IF',
        'IN',
        'IS',
        'IT',
        'JO',
        'JA',
        'KA',
        'KI',
        'LA',
        'LI',
        'LO',
        'MA',
        'ME',
        'MI',
        'MM',
        'MO',
        'MU',
        'MY',
        'NA',
        'NE',
        'NO',
        'NU',
        'OD',
        'OE',
        'OF',
        'OH',
        'OI',
        'OK',
        'OM',
        'ON',
        'OP',
        'OR',
        'OS',
        'OW',
        'OX',
        'OY',
        'PA',
        'PE',
        'PI',
        'PO',
        'QI',
        'RE',
        'SH',
        'SI',
        'SO',
        'TA',
        'TE',
        'TI',
        'TO',
        'UH',
        'UM',
        'UN',
        'UP',
        'US',
        'UT',
        'WE',
        'WO',
        'XI',
        'XU',
        'YA',
        'YE',
        'YO',
        'ZA',
        'ZE',
        'ZO'
    ]
    dictionary_half = list(map(lambda x: x.lower(), dictionary_half))
    dictionary = get_filtered_dictionary(
        get_top_words(28500, 'word_freq.csv'),
        square_size
    )
    print('Dictionary size:', len(dictionary))
    dictionary = get_halfable_words(dictionary, dictionary_half, square_size)
    character_tree = create_character_tree(dictionary)
    print('Dictionary size:', len(dictionary))
    tree_search(
        dictionary,
        character_tree,
        [],
        square_size,
        all_solutions
    )
    # print('Amount of solutions:', len(
    #     list(filter(
    #         lambda word_square: len(set(word_square)) == square_size,
    #         all_solutions
    #     ))
    # ))
    for solution in all_solutions:
        if len(set(solution)) == square_size:
            print_word_square(solution)
