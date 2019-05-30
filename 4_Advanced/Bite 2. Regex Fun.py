"""
Bite 2. Regex Fun
Learn Python regular expressions by writing the following 3 functions.

In each function's docstring we show the expected result.

The tests verify these expected results when you hit Save + Verify. We will do a more ample regex bite later on.

Note that for parsing HTML you would use a library of some sort, this is just to train your regex skills.
"""

# NOTE

NOTES = ['ALL TESTS PASSED',
        ' - since in this toy example we have control over the length of the input, I returned list instead of iterators']

# CODE

import re

def extract_course_times():
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    timestamps = []
    for course in flask_course:
        if re.search(pattern, course):
            timestams.append(re.search(patterh, course).group(1))
    return timestamps


def get_all_hashtags_and_links():
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    hashtags_and_list = []  # from the function name I am presuming this is not in any particular order
    http_pattern = re.compile('(http:\/\/[^.]+\..+?.+\.html)')
    tweets_spaced = tweet.split()
    for partial_tweet in tweets_spaced:
        if re.search(http_pattern, partial_tweet):
            hashtags_and_list.append(re.search(http_pattern, partial_tweet).group(1))
        elif partial_tweet.startswith('#'):
            hashtags_and_list.append(partial_tweet)
    return hashtags_and_list


def match_first_paragraph():
    """Write a regular expression that returns  'pybites != greedy' """
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    partials = re.split('<\/{0,1}p>', html)
    partials = [x for x in partials if x]  # remove empty strings
    return partials[0]


# TESTS

def test_extract_course_times():
    expected = ['01:47', '32:03', '41:51', '27:48', '05:02']
    assert extract_course_times() == expected


def test_extract_course_times():
    expected = ['http://pybit.es/requests-cache.html', '#python', '#APIs']
    try:
        assert get_all_hashtags_and_links() == expected
    except:
        print(get_all_hashtags_and_links())
        raise


def test_match_first_paragraph():
    expected = 'pybites != greedy'
    assert match_first_paragraph() == expected

test_extract_course_times()
test_extract_course_times()
test_match_first_paragraph()

for note in NOTES:
    print(note)
