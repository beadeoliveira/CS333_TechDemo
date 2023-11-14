# Levenshein distance for word comparison, fuzzy algorithm complete

from fuzzywuzzy import fuzz
import numpy
import Levenshtein


def levenshteinMatrix(t1, t2):
    # create a distance matrix with the lenght of each word as the row and column size
    distances = numpy.zeros((len(t1) + 1, len(t2) + 1))

    for t1 in range(len(t1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(t2) + 1):
        distances[0][t2] = t2

    return distances


def calculate_l_vals(matrix, token1, token2):
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                matrix[t1][t2] = matrix[t1 - 1][t2 - 1]
            else:
                a = matrix[t1][t2 - 1]
                b = matrix[t1 - 1][t2]
                c = matrix[t1 - 1][t2 - 1]

                if a <= b and a <= c:
                    matrix[t1][t2] = a + 1
                elif b <= a and b <= c:
                    matrix[t1][t2] = b + 1
                else:
                    matrix[t1][t2] = c + 1

    return matrix[len(token1)][len(token2)]


def levenshtein_distance(word1, word2):
    matrix = levenshteinMatrix(word1, word2)
    calc_matrix = calculate_l_vals(matrix, word1, word2)
    return calc_matrix


def fuzzy_calculation(word1, word2):
    dist = levenshtein_distance(word1.lower(), word2.lower())
    # print(dist)
    l = max(len(word1), len(word2))
    ratio = dist / l
    score = (1 - ratio)*100
    return score


if __name__ == "__main__":
    print(fuzzy_calculation("kitten", "sitting"))
    # print(fuzz.ratio("wuzzy", "wuhzzy"))
    print(Levenshtein.distance("kitten", "sitting"))
    print(Levenshtein.ratio("kitten", "sitting"))