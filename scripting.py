import re
from collections import defaultdict
import time

def get_filtered_words():
    output = []
    for word in dictionary:
        if len(word) == square_size:
            if bool(re.match("^[a-z]+$", word)):
                output.append(word)
    output.sort()
    return output


def get_segment_dict():
    output = defaultdict(list)
    for word in words:
        for i in range(1,square_size+1):
            output[word[:i]].append(word)
    return output


def show_square(hori_words, vert_words):
    to_print = [["#" for j in range(square_size)] if i >= len(hori_words) else list(hori_words[i]) for i in range(square_size)]
    for i, e in enumerate(vert_words):
        for j in range(len(hori_words),square_size):
            to_print[j][i] = e[j]
    for e in to_print:
        print("".join(e))
    print(f'{round(time.time() - startTime, 2)}s')
    print("")


def tree_search(hori_words, vert_words):
    if len(hori_words) == square_size or len(vert_words) == square_size:
        show_square(hori_words, vert_words)
    else:
        if len(vert_words) > len(hori_words):
            temp = hori_words
            hori_words = vert_words
            vert_words = temp
        matching_index = len(vert_words)
        matching_word = ""
        for e in hori_words:
            matching_word += e[matching_index]
        if matching_word in segment_dict:
            options = segment_dict[matching_word]
            for e in options:
                if e not in hori_words and e not in vert_words:
                    isPossible = True
                    for i in range(len(hori_words), square_size):
                        search_term = ""
                        for vert in vert_words:
                            search_term += vert[i]
                        search_term += e[i]
                        if search_term not in segment_dict:
                            isPossible = False
                            break
                    if isPossible:
                        tree_search(hori_words, vert_words + [e])

startTime = time.time()
dictionaryFile = open("dictionary.txt", "r")
dictionary = dictionaryFile.read().split("\n")
dictionaryFile.close()
square_size = 6
words = get_filtered_words()
segment_dict = get_segment_dict()
print(f'Preprocessing: {round(time.time() - startTime, 2)}s')
for i, word in enumerate(words):
    print("---", word)
    tree_search([words[0]], [])