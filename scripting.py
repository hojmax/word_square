import re


def create_character_tree(dictionary):
    root = {}

    for word in dictionary:
        current = root
        for letter in word:
            current = current.setdefault(letter, {})

    return root


def isFlippable(word, dictionary):
    return word[::-1] in dictionary


def get_filtered_dictionary(dictionary, word_length):
    lookup = set(dictionary)

    def is_valid(word):
        return len(word) == word_length and isFlippable(word, lookup) and re.match("^[a-z]+$", word)

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
        print(word)
    print()


def get_possible_words(word_square, character_tree, square_size):
    column_possibilities = []
    for x in range(square_size):
        column_possibilities.append(
            get_column_possibilities(
                character_tree,
                word_square,
                x
            )
        )
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
    square_size
):
    if len(word_square) == square_size:
        return print_word_square(word_square)

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
            square_size
        )


if __name__ == "__main__":
    square_size = 6
    dictionary = get_dictionary("dictionary.txt")
    dictionary = get_filtered_dictionary(dictionary, square_size)
    character_tree = create_character_tree(dictionary)
    tree_search(
        dictionary,
        character_tree,
        [],
        square_size
    )
