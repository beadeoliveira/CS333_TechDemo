word_map = {
    "wet": ["dream"],
    "yellow": ["shower", "showers"],
    "ball": ["licking", "sack", "sucking", "kicking", "gravy"],
    "barely": ["legal"],
    "beaver": ["cleaver", "lips"],
    "big": ["black", "breasts", "tits", "knockers"],
    "black": ['cock'],
    "blonde": ['action'],
    "blow": ["job", "your"],
    "your": ["load"],
    "blue": ["balls", "balled", "waffle"],
    "booty": ["call"],
    "brown": ["shower", "showers"],
    "camel": ["toe"],
    "chocolate": ["rosebuds"],
    "deep": ["throat"],
    "doggie": ["style"],
    "dog": ["style"],
    "double": ["penetration"],
    "dry": ["hump"],
    "eat": ["my"],
    "my": ["ass"],
    "female": ["squirting"],
    "foot": ["fetish"],
    "gang": ["bang"],
    "girl": ["on"],
    "golden": ["shower"],
    "group": ["sex"],
    "hand": ["job"],
    "how": ["to"],
    "to": ["murder", "kill", "fuck"],
    "jack": ["off"],
    "jail": ["bait"],
    "make": ["me"],
    "me": ["come"],
    "male": ["squirting"],
    "missionary": ["position"],
    "nig": ["nog"],
    "phone": ["sex"],
    "pleasure": ["chest"],
    "poop": ["shoot"],
    "raging": ["boner"],
    "reverse": ["cowgirl"],
    "shaved": ["beaver", "pussy"],
    "spread": ["legs"],
    "strap": ["on"],
    "strip": ["club"],
    "style": ["doggy"],
    "suicide": ["girls"],
    "tainted": ["love"],
    "tea": ["bagging"],
    "tub": ["girl"],
    "urethra": ["play"],
    "g": ["spot"],
    "white": ["power"],
    "piece": ["of"],
    "of": ["shit"],
}


def multi_word(phrase, word, cur, v):
    if word not in word_map and cur == "":
        return word
    if word not in word_map and cur != "":
        cur += word
        return cur
    if word in word_map:
        cur += word + " "
        if v + 1 < len(phrase) and phrase[v + 1] in word_map[word]:
            return multi_word(phrase, phrase[v + 1], cur, v + 1)
        else:
            return cur


if __name__ == '__main__':
    phrase = ["piece", "of", "shit"]
    print(multi_word(phrase, "piece", '', 0))
