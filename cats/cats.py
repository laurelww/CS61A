"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    options = [p for p in paragraphs if select(p)]

    if len(options) <= k:
        return ''
    else:
        return options[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def about_topic(paragraph):
        paragraph = remove_punctuation(lower(paragraph)).split()

        for word in topic:
            if word in paragraph:
                return True
        return False

    return about_topic
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    if typed_words == reference_words:
        return 100.0

    success = 0
    for i in range(min(len(typed_words), len(reference_words))):
        if typed_words[i] == reference_words[i]:
            success += 1

    total = len(typed_words)
    if total:
        return success/total * 100
    else:
        return 0.0
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    LEN_OF_A_WORD = 5
    part_of_a_minute = 60/elapsed
    return len(typed)/LEN_OF_A_WORD * part_of_a_minute
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    else:
        lowest_diff = (limit + 1, user_word)
        for word in valid_words:
            next_diff = (diff_function(user_word, word, limit), word)
            if next_diff[0] < lowest_diff[0]:
                lowest_diff = next_diff

        return user_word if lowest_diff[0] > limit else lowest_diff[1]
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def shifty_helper(temp_start, temp_goal, diff):
        if diff > limit:
            return limit + 1
        elif len(temp_start) == 0 or len(temp_goal) == 0:
            return diff + max(len(temp_start), len(temp_goal))
        elif temp_start[0] != temp_goal[0]:
            return shifty_helper(temp_start[1:], temp_goal[1:], diff + 1)
        else:
            return shifty_helper(temp_start[1:], temp_goal[1:], diff)

    if start == goal:
        return 0

    return shifty_helper(start, goal, 0)
    # END PROBLEM 6



def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    >>> big_limit = 10
    >>> meowstake_matches("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> meowstake_matches("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> meowstake_matches("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    # BEGIN PROBLEM 7
    if start == goal:
        return 0
    elif abs(len(start) - len(goal)) > limit:
        return float('inf')
    elif start == '' or goal == '':
        return max(len(start), len(goal))
    elif start[:1] == goal[:1]:
        return meowstake_matches(start[1:], goal[1:], limit)
    elif limit < 0:
        return float('inf')
    else:
        add_diff = 1 + meowstake_matches(start[1:], goal, limit - 1)
        remove_diff = 1 + meowstake_matches(start, goal[1:], limit - 1)
        substitute_diff = 1 + meowstake_matches(start[1:], goal[1:], limit - 1)
        
        return min([add_diff, remove_diff, substitute_diff])
    # END PROBLEM 7


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    d = {'progress': 0, 'id': id}
    i = 0
    while i < len(typed) and typed[i] == prompt[i]:
        d['progress'] += 1
        i += 1
    d['progress'] /= len(prompt)

    send(d)

    return d['progress']
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    def delta_btwn_pairs(itr):
        itr = iter(itr)
        last, curr = next(itr, None), next(itr, None)
        new_itr = []
        while curr is not None:
            new_itr.append(curr - last)
            last, curr = curr, next(itr, None)
        return new_itr

    times = [delta_btwn_pairs(player_times) for player_times in times_per_player]
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    words_results = [[] for _ in players]
    for word in words:
        competing_times = [time[word] for time in all_times(game)]
        words_results[competing_times.index(min(competing_times))] += [all_words(game)[word]]
    return words_results
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you

##########################
# Extra Credit #
##########################

key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""

    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase

    # BEGIN PROBLEM EC1
    if start == goal:
        return 0
    elif abs(len(start) - len(goal)) > limit:
        return float('inf')
    elif start == '' or goal == '':
        return max(len(start), len(goal))
    elif start[0] == goal[0]:
        return key_distance_diff(start[1:], goal[1:], limit)
    elif limit <= 0:
        return float('inf')
    else:
        distance_diff = key_distance[start[0], goal[0]]
        add_diff = 1 + key_distance_diff(start[1:], goal, limit - 1)
        remove_diff = 1 + key_distance_diff(start, goal[1:], limit - 1)
        substitute_diff = distance_diff + key_distance_diff(start[1:], goal[1:], limit - distance_diff)

        return min([add_diff, remove_diff, substitute_diff])
    # END PROBLEM EC1

def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""
    cache = {}
    def memoized(*args):
        if str(args) not in cache:
            cache[str(args)] = f(*args)
        return cache[str(args)]
    return memoized


key_distance_diff = count(memo(key_distance_diff))
def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""

    # BEGIN PROBLEM EC2
    return autocorrect(user_word, valid_words, diff_function, limit)
    # END PROBLEM EC2
faster_autocorrect = memo(faster_autocorrect)

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
