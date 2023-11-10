import pandas as pd
from pre_processing import remove_punctuation

# TODO: need to figure out how to control for multiple word bad words


def hashing_moderation(input):
    # first method is to take a set of unique words and parse through the words
    bad_words = pd.read_csv('../docs/bad_words.csv')
    processed_input = remove_punctuation(input)
    split_input = processed_input.split(' ')
    words = list(set(split_input))
    found_words = []
    for word in words:
        # TODO: control for punctuation
        word = word.replace('.', '')
        word = word.replace(',', '')
        word = word.replace(';', '')
        word = word.replace(':', '')
        if word.lower() in bad_words.values:
            found_words.append(word)
    if len(found_words) > 0:
        return True, found_words
    return False, []


if __name__ == "__main__":
    input_val = 'Throw a ball.'
    print(hashing_moderation(input_val))
