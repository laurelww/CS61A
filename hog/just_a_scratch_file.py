import sys

GOAL = 100
SIDES = 6

sys.setrecursionlimit(3000)


def swine_flu(my_score, opponent_score):
    """
    SWINE FLU.

    """
    return optimal_num_dice(my_score, opponent_score)


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    return 10 - score % 10 + score // 10
    # END PROBLEM 2


def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped
    """
    # BEGIN PROBLEM 4
    abs_of_diff_of_ones_digits = abs(player_score % 10 - opponent_score % 10)
    tens_digit_of_opponent = opponent_score // 10 % 10

    return abs_of_diff_of_ones_digits == tens_digit_of_opponent
    # END PROBLEM 4


def cache(f):
    """A cache to store previous results of a function."""
    stored_results = {}
    def search(*args):
        key = (f, args)
        try:
            return stored_results[key]
        except KeyError:
            stored_results[key] = f(*args)
            return stored_results[key]
    return search


@cache
def chance_of_winning_given_num_rolls(my_score, opponent_score, num_rolls):
    """Returns a player's chance of winning given the number of dice they roll."""
    win_chance = 0
    if num_rolls == 0:
        # Free Bacon
        my_score += free_bacon(opponent_score)
        win_chance = chance_of_winning_given_scores(my_score, opponent_score)
    for score in range(1, (SIDES * num_rolls) + 1):
        chance_of_scoring_targ_ = chance_of_scoring_targ(score, num_rolls)
        win_chance_given_scores = chance_of_winning_given_scores(my_score + score, opponent_score)
        win_chance += chance_of_scoring_targ_ * win_chance_given_scores
    return win_chance


@cache
def chance_of_winning_given_scores(my_score, opp_score):
    """Returns a player's chance of winning based on the current scores."""
    if is_swap(my_score, opp_score):
        my_score, opp_score = opp_score, my_score
    if my_score >= GOAL:
        return 1
    if opp_score >= GOAL:
        return 0
    # Calculate the chance of the opponent winning, and subtract it from 100%
    opp_best_play = optimal_num_dice(opp_score, my_score)
    opp_win_chance = chance_of_winning_given_num_rolls(opp_score, my_score, opp_best_play)
    return 1 - opp_win_chance


@cache
def optimal_num_dice(my_score, opponent_score):
    """Returns the optimal number of dice to roll based on the current scores."""
    def optimal_num_dice_helper(highest_win_chance=0, optimal_num=1, num_dice=10):
        # Recurse until num_dice 0 -> 10 (inclusive) have been tested
        if num_dice + 1 == 0:
            return optimal_num
        curr_win_chance = chance_of_winning_given_num_rolls(my_score, opponent_score, num_dice)
        # Update the highest chance of winning when a new high is found
        if curr_win_chance > highest_win_chance:
            return optimal_num_dice_helper(curr_win_chance, num_dice, num_dice - 1)
        return optimal_num_dice_helper(highest_win_chance, optimal_num, num_dice - 1)

    return optimal_num_dice_helper(0, 1, 10)


def ways_to_score_targ(target_score, num_dice):
    """
    Returns the number of ways to make a score of target_score
    while rolling num_dice 6-sided dice.
    """
    if target_score == 1:
        # The probability of rolling at least one one is the probability of *not*
        #     rolling a one subtracted from 100%.
        return (SIDES - 1) ** num_dice

    # Ignores the Pig Out scenario (roll a 1)
    MIN_DIE_VAL = 2

    # Padding to make range bounds cleaner and inclusive
    target_score += 1
    num_dice += 1
    sides = SIDES + 1
    matrix = [[0 for _ in range(target_score)] for _ in range(num_dice)]

    for col in range(MIN_DIE_VAL, min(sides, target_score)):
        # Store data for one die
        matrix[1][col] = 1

    # The rows indicate the number of dice, and the columns indicate the score.
    for row in range(2, num_dice):
        for col in range(MIN_DIE_VAL, target_score):
            for decrement in range(MIN_DIE_VAL, min(sides, col)):
                matrix[row][col] += matrix[row - 1][col - decrement]

    return matrix[-1][-1]


@cache
def chance_of_scoring_targ(target_score, num_dice):
    """
    Returns the chance that you will roll your target score given num_dice dice.
    This assumes all dice have six sides.
    """
    if target_score == 1:
        return 1 - ways_to_score_targ(target_score, num_dice) / SIDES ** num_dice
    return ways_to_score_targ(target_score, num_dice) / SIDES**num_dice


if __name__ == "__main__":
    print(swine_flu(0, 0))
    print(swine_flu(0, 0))
    print(swine_flu(12, 34))
    print(swine_flu(12, 34))
    print(swine_flu(1, 3))
    print(swine_flu(78, 54))
    print(swine_flu(1, 99))
    # pass


    """
    Steps:
    . Test every option for num_rolls (0 -> 10, inclusive) to see which one
        yields the highest chance of achieving a win.
        . Chance of winning based on rolls is calculated by checking for
            Free Bacon, then comparing the score (with Free Bacon gains,
            if applicable) against all other scores for chance of winning.
            . Scores are checked for winning by simulating turns for the
                player and their opponent and calculating the chance that
                the player will beat their opponent (swaps are accounted for).

    General dice probabilities are calculated with the respective funcs and
        used as necessary within the primary strategic functions.

    free_bacon and is_swap are exactly as they appear in my hog.py file.
    """

# import sys
#
# GOAL = 100
# SIDES = 6
#
# sys.setrecursionlimit(1500)
#
#
# def swine_flu(my_score, opponent_score):
#     """
#     SWINE FLU.
#
#     """
#     return optimal_num_dice(my_score, opponent_score)
#
#
# def free_bacon(score):
#     """Return the points scored from rolling 0 dice (Free Bacon).
#
#     score:  The opponent's current score.
#     """
#     assert score < 100, 'The game should be over.'
#     # BEGIN PROBLEM 2
#     return 10 - score % 10 + score // 10
#     # END PROBLEM 2
#
#
# def is_swap(player_score, opponent_score):
#     """
#     Return whether the two scores should be swapped
#     """
#     # BEGIN PROBLEM 4
#     abs_of_diff_of_ones_digits = abs(player_score % 10 - opponent_score % 10)
#     tens_digit_of_opponent = opponent_score // 10 % 10
#
#     return abs_of_diff_of_ones_digits == tens_digit_of_opponent
#     # END PROBLEM 4
#
#
# def cache(f):
#     """A cache to store previous results of a function."""
#     stored_results = {}
#     def search(*args):
#         key = (f, args)
#         try:
#             return stored_results[key]
#         except KeyError:
#             stored_results[key] = f(*args)
#             return stored_results[key]
#     return search
#
#
# @cache
# def chance_of_winning_given_num_rolls(my_score, opponent_score, num_rolls):
#     """Returns a player's chance of winning given the number of dice they roll."""
#     win_chance = 0
#     if num_rolls == 0:
#         # Free Bacon
#         my_score += free_bacon(opponent_score)
#         win_chance = chance_of_winning_given_scores(my_score, opponent_score)
#     for score in range(1, (SIDES * num_rolls) + 1):
#         chance_of_scoring_targ_ = chance_of_scoring_targ(score, num_rolls)
#         win_chance_given_scores = chance_of_winning_given_scores(my_score + score, opponent_score)
#         win_chance += chance_of_scoring_targ_ * win_chance_given_scores
#     return win_chance
#
#
# @cache
# def chance_of_winning_given_scores(my_score, opp_score):
#     """Returns a player's chance of winning based on the current scores."""
#     if is_swap(my_score, opp_score):
#         my_score, opp_score = opp_score, my_score
#     if my_score >= GOAL:
#         return 1
#     if opp_score >= GOAL:
#         return 0
#     # Calculate the chance of the opponent winning, and subtract it from 100%
#     opp_best_play = optimal_num_dice(opp_score, my_score)
#     opp_win_chance = chance_of_winning_given_num_rolls(opp_score, my_score, opp_best_play)
#     return 1 - opp_win_chance
#
#
# @cache
# def optimal_num_dice(my_score, opponent_score):
#     """Returns the optimal number of dice to roll based on the current scores."""
#     def optimal_num_dice_helper(highest_win_chance=0, optimal_num=1, num_dice=10):
#         # Recurse until num_dice 0 -> 10 (inclusive) have been tested
#         if num_dice + 1 == 0:
#             return optimal_num
#         curr_win_chance = chance_of_winning_given_num_rolls(my_score, opponent_score, num_dice)
#         # Update the highest chance of winning when a new high is found
#         if curr_win_chance > highest_win_chance:
#             return optimal_num_dice_helper(curr_win_chance, num_dice, num_dice - 1)
#         return optimal_num_dice_helper(highest_win_chance, optimal_num, num_dice - 1)
#
#     return optimal_num_dice_helper(0, 1, 10)
#
# @cache
# def ways_to_score_targ(target_score, num_dice):
#     """
#     Returns the number of ways to make a score of target_score
#     while rolling num_dice 6-sided dice.
#     """
#     if target_score == 1:
#         # The probability of rolling at least one one is the probability of *not*
#         #     rolling a one subtracted from 100%.
#         return (SIDES - 1) ** num_dice
#
#     # Ignores the Pig Out scenario (roll a 1)
#     MIN_DIE_VAL = 2
#
#     # Padding to make range bounds cleaner and inclusive
#     target_score += 1
#     num_dice += 1
#     sides = SIDES + 1
#     matrix = [[0 for _ in range(target_score)] for _ in range(num_dice)]
#
#     for col in range(MIN_DIE_VAL, min(sides, target_score)):
#         # Store data for one die
#         matrix[1][col] = 1
#
#     # The rows indicate the number of dice, and the columns indicate the score.
#     for row in range(2, num_dice):
#         for col in range(MIN_DIE_VAL, target_score):
#             for decrement in range(MIN_DIE_VAL, min(sides, col)):
#                 matrix[row][col] += matrix[row - 1][col - decrement]
#
#     return matrix[-1][-1]
#
#
# @cache
# def chance_of_scoring_targ(target_score, num_dice):
#     """
#     Returns the chance that you will roll your target score given num_dice dice.
#     This assumes all dice have six sides.
#     """
#     if target_score == 1:
#         return 1 - ways_to_score_targ(target_score, num_dice) / SIDES ** num_dice
#     return ways_to_score_targ(target_score, num_dice) / SIDES**num_dice
#
#
# if __name__ == "__main__":
#     # print(swine_flu(0, 0))
#     # print(swine_flu(0, 0))
#     # print(swine_flu(12, 34))
#     # print(swine_flu(12, 34))
#     # print(swine_flu(1, 3))
#     # print(swine_flu(78, 54))
#     # print(swine_flu(1, 99))
#     pass
