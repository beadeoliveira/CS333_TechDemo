# NOTE: THIS PY FILE IS JUST TO EDIT THE CSV - NOT USEABLE

import pandas as pd
from fuzzy_algo import fuzzy_calculation
from phonetic_matching import process_word

bad_words = pd.read_csv('../docs/bad_words.csv')
soundex = []

for index, row in bad_words.iterrows():
    s = process_word(row['Words'])
    soundex.append(s)

# print(soundex)
# 
# bad_words['soundex'] = soundex
# 
# print(bad_words)

# bad_words.to_csv('../docs/bad_words.csv')
