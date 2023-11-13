import pandas as pd
from pre_processing import remove_punctuation
from multi_word import multi_word
from phonetic_matching import process_word
from fuzzy_algo import fuzzy_calculation


def hashing_moderation(input):

    bad_words = pd.read_csv('../docs/bad_words.csv')
    bad_words = bad_words.set_index('Words')
    processed_input = remove_punctuation(input)
    split_input = processed_input.split(' ')
    words = list(split_input)
    found_words = []
    leftover = []
    w = 0
    avg = 0

    while w < len(words):
        word = words[w].lower()
        multi_check = multi_word(words, word, '', w)
        if multi_check in bad_words.index:
            found_words.append(multi_check)
            avg += bad_words.loc[multi_check]['ranking']
            w += len(multi_check.split(' '))
        else:
            leftover.append(word)
            w += 1

    if len(found_words) > 0:
        return True, found_words, avg/len(found_words), leftover
    return False, []


if __name__ == "__main__":
    input_val = "You are a piece of shit. F*ck you slut."
    print(hashing_moderation(input_val))
