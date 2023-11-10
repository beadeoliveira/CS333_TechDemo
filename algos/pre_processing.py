
def remove_punctuation(s):
    """ removes the punctuation in the sentence prior to processing """
    s = s.translate(str.maketrans('', '', ',:;!?.'))
    return s

#
# if __name__ == "__main__":
#     print(remove_punctuation("Hello, my name is bea. what's up."))
