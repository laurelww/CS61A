def final_strategy(score, opponent_score):
    return best_num_dice_to_roll(score, opponent_score)


import sys
from decimal import *
from hog import is_swap, free_bacon


# Tell the Decimal class to use 100 digits of precision
getcontext().prec = 100
MAX_DICE = 10
MAX_RECURSION_DPETH = 2000
GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


def memoized(f):
    data = {}

    def lookup(*args):
        key = (f, args)
        if not key in data:
            data[key] = f(*args)
        return data[key]

    return lookup


@memoized
def best_num_dice_to_roll(score, opponent_score):
    """ Returns the optimal number of dice to roll given score and opponent_score
    assuming it is the beginning of your turn.
    """
    if sys.getrecursionlimit() < MAX_RECURSION_DPETH:
        sys.setrecursionlimit(MAX_RECURSION_DPETH)
    if opponent_score == 1:
        # There is a good chance the opponent just hijinksed. Swap and pray!
        return -1
    score = Decimal(score)
    opponent_score = Decimal(opponent_score)
    best_probability, best_n = Decimal(0), 1
    # Iterate through each number of dice that can be rolled
    for n in range(0, MAX_DICE + 1):
        probability = probability_of_winning_by_rolling_n(score, opponent_score,
                                                          n)
        if probability > best_probability:
            best_probability, best_n = probability, n
    return best_n


@memoized
def probability_of_winning_by_rolling_n(score, opponent_score, n):
    """ Returns probability that you will win if you roll n dice assuming it is
    your turn now.
    """
    sides = 6
    # Hog wild
    # if hog_wild(score, opponent_score):
    #     sides = 4
    probability_of_winning = 0
    if n == 0:
        # Free Bacon
        turn_score = free_bacon(opponent_score)
        probability_of_winning = probability_of_winning_with_turn_end_scores(
            score + turn_score, opponent_score)
    else:
        # Iterate over each possible outcome for rolling n dice
        for possible_score in range(1, (sides * n) + 1):
            probability_of_winning += probability_of_scoring(possible_score, n,
                                                             sides) * probability_of_winning_with_turn_end_scores(
                score + possible_score, opponent_score)
    return probability_of_winning


@memoized
def probability_of_winning_with_turn_end_scores(score, opponent_score):
    """ Returns the chance that you will win the game if the scores are those
    passed in when your turn is complete.
    """
    # Swine swap
    if is_swap(score, opponent_score):
        score, opponent_score = opponent_score, score
    if score >= GOAL_SCORE:
        return 1
    elif opponent_score >= GOAL_SCORE:
        return 0
    opponent_num_rolls = best_num_dice_to_roll(opponent_score, score)
    probability_of_opponent_winning = probability_of_winning_by_rolling_n(
        opponent_score, score, opponent_num_rolls)
    return 1 - probability_of_opponent_winning


@memoized
def number_of_ways_to_score(k, n, s):
    """ Returns the number of ways that k can be scored by rolling n
    s sided dice without pigging out.

    k: goal score
    n: number of dice to use
    s: number of sides on dice

    >>> number_of_ways_to_score(4, 1, 6)
    1
    >>> number_of_ways_to_score(12, 2, 6)
    1
    >>> number_of_ways_to_score(11, 2, 6)
    2
    >>> number_of_ways_to_score(7, 3, 6)
    3
    >>> number_of_ways_to_score(8, 3, 4)
    6
    """
    if k < 0:
        return 0
    if k == 0 and n == 0:
        return 1
    if n == 0:
        return 0
    total = 0
    for i in range(2, s + 1):
        total += number_of_ways_to_score(k - i, n - 1, s)
    return total


@memoized
def probability_of_scoring(k, n, s):
    """ Returns the chance that at least k will be scored by rolling n s sided
    dice without pigging out.

    k: goal score
    n: number of dice to use
    s: number of sides on dice

    >>> almost_equal = lambda x, y: abs(x - y) < 1e-10
    >>> almost_equal(probability_of_scoring(4, 1, 6), 1/6)
    True
    >>> almost_equal(probability_of_scoring(7, 3, 6), 3/216)
    True
    >>> almost_equal(probability_of_scoring(1, 2, 6), 11/36)
    True
    >>> almost_equal(probability_of_scoring(2, 3, 6), 0)
    True
    >>> almost_equal(probability_of_scoring(11, 10, 6), 0)
    True
    """
    if k == 1:
        return Decimal(1) - Decimal((pow(s - 1, n) / pow(s, n)))
    return Decimal(number_of_ways_to_score(k, n, s)) / Decimal(pow(s, n))

if __name__ == "__main__":
    # print(ways_to_roll_score(1, 2, 6))
    # # 0
    # print(ways_to_roll_score(14, 6, 6))
    # # 21
    # print(ways_to_roll_score(1, 10, 6))
    # # 0
    # print(ways_to_roll_score(9, 3, 6))
    # # 10
    # print(ways_to_roll_score(50, 10, 6))
    # # 72403
    # print(ways_to_roll_score(5, 2, 6))
    # # 2

    # almost_equal = lambda x, y: abs(x - y) < 1e-10
    # print(almost_equal(chance_of_scoring_targ(4, 1), 1 / 6))
    # # True
    # print(almost_equal(chance_of_scoring_targ(7, 3), 3 / 216))
    # # True
    # print(almost_equal(chance_of_scoring_targ(1, 2), 11 / 36))
    # # True
    # print(almost_equal(chance_of_scoring_targ(2, 3), 0))
    # # True
    # print(almost_equal(chance_of_scoring_targ(11, 10), 0))
    # # True


    # import doctest
    # doctest.testmod()
    print("Fin: ", final_strategy(23, 24))
    # 10
    print("Fin: ", final_strategy(2, 24))
    # 0?