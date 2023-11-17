import pandas as pd
from pre_processing import remove_punctuation
from multi_word import multi_word
from phonetic_matching import process_word
from fuzzy_algo import fuzzy_calculation


# IDEA: do (1) basic hashing (2) soundex (3) leveshtein
# if 1 + (2 or 3), do both normally
# if a combo of 2 and 3 only do 3 is matching 2

def basic_hashing_moderation(words, bad_words):
    # first method is to take a set of unique words and parse through the words
    found_words = []
    leftover = []
    w = 0

    while w < len(words):
        word = words[w].lower()
        multi_check = multi_word(words, word, '', w)
        if multi_check in bad_words.index:
            found_words.append(multi_check)
            w += len(multi_check.split(' '))
        else:
            leftover.append(word)
            w += 1

    if len(found_words) > 0:
        return found_words, leftover
    return False, []


def soundex_hashing(split_words, bad_words):
    found_words = []
    leftover = []

    for word in split_words:
        soundex_val = process_word(word)
        if soundex_val in bad_words.values:
            found_words.append([word, soundex_val])
        else:
            leftover.append(word)

    return found_words, leftover


def levenshtein_hashing(split_words, bad_words):
    # Threshold is (0.75)
    flagged = []
    not_flagged = []
    for word in split_words:
        for index, row in bad_words.iterrows():
            lev_score = fuzzy_calculation(word, index)
            if lev_score >= 75:
                flagged.append(word)
                break
        if word not in flagged:
            not_flagged.append(word)
    return flagged, not_flagged


def lev_and_soundex(words, bad_words):
    # use first letter and do L distance between those and the flagged words
    flagged = []
    flagged_words = soundex_hashing(words, bad_words)[0]
    for word in flagged_words:
        matching_sdx = bad_words.loc[bad_words['soundex'] == word[1]]
        for index, row in matching_sdx.iterrows():
            lev_score = fuzzy_calculation(index, word[0])
            # Threshold here
            if lev_score >= 75:
                flagged.append(word[0])
                break
    not_flagged = list(set(words) - set(flagged))
    return flagged, not_flagged


''' Key:
    b = basic hashing,
    l = leventshein,
    s = soundex, 
    sl = soundex + levensthein,
    a = all,
'''


def hashing_algo(options, input_s):
    file = '../docs/bad_words.csv'
    bad_words = pd.read_csv(file)
    bad_words = bad_words.set_index('Words')

    processed_input = remove_punctuation(input_s)
    words = processed_input.split(' ')

    ret = []

    if options == 's':
        sdx = soundex_hashing(words, bad_words)
        flagged = [x[0] for x in sdx[0]]
        ret = [flagged, sdx[1]]

    if options == 'l':
        ret = levenshtein_hashing(words, bad_words)

    if options == 'b':
        ret = basic_hashing_moderation(words, bad_words)

    if options == 'sl':
        ret = lev_and_soundex(words, bad_words)

    if options == 'a':
        basic_hash = basic_hashing_moderation(words, bad_words)
        if not basic_hash[0]:
            ret = lev_and_soundex(words, bad_words)
        else:
            init_flagged = basic_hash[0]
            not_init = basic_hash[1]
            add_words = lev_and_soundex(not_init, bad_words)
            fnl_not_in = list(set(not_init) - set(add_words[0]))
            ret = init_flagged + add_words[0], fnl_not_in

    if not interpret_hashing(ret[0]):
        return False

    # TODO: if we want to do the score system, \
    #  how to do total score for non-perfect words, how do we know what word it is


    # for word in ret[0]:
    #     ttl_score += bad_words.loc[word]['ranking']

    return True, len(ret[0]), ret[0], ret[1]


def interpret_hashing(hash_result):
    if hash_result:
        if len(hash_result) > 0:
            return True
    else:
        return False


if __name__ == "__main__":
    path_to_file = '../docs/bad_words.csv'
    input_val = "You are a piece of shit. F*ck you slut."
    print("Input was: " + input_val)
    print("All: ", hashing_algo('a', input_val))
    print("Basic Hash Match: ", hashing_algo('b', input_val))
    print("Soundex Only: ", hashing_algo('s', input_val))
    print("Levenshtein only: ", hashing_algo('l', input_val))
    print("Soundex + Levenshtein: ", hashing_algo('sl', input_val))
