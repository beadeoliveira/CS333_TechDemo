import pandas as pd


# df = pd.read_csv('../docs/bad_words.txt')
# # read_file.to_csv('../docs/bad_words.csv')
# # df = df.drop('Unamed: 0', axis = 'columns'
# df.rename(columns = {'2g1c':'Words'}, inplace = True)
# df.to_csv('../docs/bad_words.csv')
# print(df.head())

def hashing_moderation(input):
    # first method is to take a set of unique words and parse through the words
    bad_words = pd.read_csv('../docs/bad_words.csv')
    split_input = input.split(' ')
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
    input_val = 'F**k you.'
    print(hashing_moderation(input_val))
