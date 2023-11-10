import pandas as pd
from pre_processing import remove_punctuation
from multi_word import multi_word
from phonetic_matching import process_word
from fuzzy_algo import fuzzy_calculation


def hashing_moderation(input):
    # first method is to take a set of unique words and parse through the words
    bad_words = pd.read_csv('../docs/bad_words.csv')
    processed_input = remove_punctuation(input)
    split_input = processed_input.split(' ')
    words = list(split_input)
    found_words = []
    leftover = []
    print(words)
    for w in range(len(words)):
        word = words[w].lower()
        # TODO: how to avoid making it pickup multiple in a sequence
        multi_check = multi_word(words, word, '', w)
        if multi_check in bad_words.values:
            found_words.append(multi_check)
        else:
            leftover.append(word)
    if len(found_words) > 0:
        return True, found_words
    return False, []


if __name__ == "__main__":
    input_val = "You are a piece of shit. Fuck you slut."
    print(hashing_moderation(input_val))
