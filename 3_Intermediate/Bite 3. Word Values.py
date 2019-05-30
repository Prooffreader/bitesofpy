"""Bite 3. Word Values
Calculate the dictionary word that would have the most value in Scrabble.

There are 3 tasks to complete for this Bite:

First write a function to read in dictionary.txt (DICTIONARY constant) and return a list of words.
Second write a function that receives a word and calculates its value. Use the scores stored in LETTER_SCORES.
With these two pieces in place, write a third function that takes a list of words and returns the word with the highest value."""

# PROGRAMMER'S NOTE

NOTES = ['ALL TESTS PASSED.',
         ' - As the problem was stated and the tests were formulated, the case where there '
         'was a tie was not addressed.',
         '   - Thus there is little point in downloading the scrabble dictionary except to '
         'make the test pass']

# CODE

import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
if not os.path.isfile(DICTIONARY):
    urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
with open(DICTIONARY, 'r') as f:
    TEXT = f.read()
# In my opinoin, scrabble_scores should be an upper-case constant
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}
# Instead of dealing with .upper() and lower() all over the place which could easily be fragile,
# I made the (veru small) dict accommodate lowercae latters.
LETTER_SCORES.update({letter.lower(): score for score, letters in scrabble_scores
                 for letter in letters.split()})

# ACTUAL FUNCTIONS

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    return [x for x in TEXT.split('\n') if x]  # in case blank lines

VALID_WORDS = load_words()

def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    # In my opinion, words should return 0 if they are not in dictonary.
    # The tests were not set up this wa;.
    # The code would be the next two linkes:
    #if word not in VALID_WORDS:
    #    return 0
    total_score = 0
    for letter in word:
        total_score += LETTER_SCORES.get(letter, 0)
    return total_score

def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    if not words:
        return None
    best_words = []
    max_value = 0
    for word in words:
        # I have added the providion to return a list if there is a tie,
        # but this possibility is not provided in the tests.
        score = calc_word_value(word)
        if score == max_value:
            best_words.append(word)
        elif score > max_value:
            best_words = [word]
            max_value = max(max_value, score)

    if len(best_words) > 1:
        return best_words  # if there are ties
    else:
        return best_words[0]

# TESTS

words = load_words()


def test_load_words():
    assert len(words) == 235886
    assert words[0] == 'A'
    assert words[-1] == 'Zyzzogeton'
    assert ' ' not in ''.join(words)


def test_calc_word_value():
    assert calc_word_value('bob') == 7
    assert calc_word_value('JuliaN') == 13
    assert calc_word_value('PyBites') == 14
    assert calc_word_value('benzalphenylhydrazone') == 56


def test_max_word_value():
    test_words = ('bob', 'julian', 'pybites', 'quit', 'barbeque')
    assert max_word_value(test_words) == 'barbeque'
    assert max_word_value(words[20000:21000]) == 'benzalphenylhydrazone'


def test_non_scrabble_characters():
    # thanks Joakim
    assert max_word_value(["a", "åäö"]) == "a"

test_load_words()
test_calc_word_value()
test_max_word_value()
test_non_scrabble_characters()

# print notes
for note in NOTES:
    print(note)

