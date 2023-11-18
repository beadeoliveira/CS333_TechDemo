# implementing the soundex algorithm to determine phonetic similarities

soundex_dict = {
    "b": '1',
    "f": '1',
    "p": '1',
    "v": '1',
    "c": '2',
    "j": '2',
    "g": '2',
    "k": '2',
    "s": '2',
    "x": '2',
    "z": '2',
    "d": "3",
    "t": '3',
    "l": '4',
    "m": '5',
    "n": '5',
    "r": '6',
    "$": '2',
}

vowels_plus = "aeiou*@"


def process_word(s):
    s = s.lower()
    if len(s) < 1:
        return ''
    new_s = s[0].upper()
    init_code = ''
    if s[0] in soundex_dict:
        init_code = soundex_dict[s[0]]
        # print(init_code)
    if len(s) > 1:
        for letter in s[1:]:
            if letter not in vowels_plus:
                if letter in soundex_dict:
                    if len(new_s) == 1:
                        if init_code != '':
                            if soundex_dict[letter] == init_code:
                                continue
                    code = soundex_dict[letter]
                    if code != new_s[-1]:
                        new_s += soundex_dict[letter]

    if len(new_s) >= 4:
        new_s = new_s[:4]
    else:
        zeros = 4 - len(new_s)
        new_s = new_s + ('0'*zeros)

    return new_s

#
# if __name__ == "__main__":
#
#     input_val = 'A'
#     iv = 'F*ck'
#     print(process_word(input_val))
#     print(process_word(iv))
