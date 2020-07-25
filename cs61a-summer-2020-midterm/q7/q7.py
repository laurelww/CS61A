email = 'laurelw@berkeley.edu'

"""
Let a `painting` be a self-referential function that
    - takes in one integer
    - returns two values, another painting and well as an integer

For an example see the function `identity_painting` below.

You have two tasks in this assignment, to implement the functions `microscope`
and `footstool`. Both have their behavior defined by their doctests.

It is not necessary to implement `microscope` correctly to get the points for
`footstool`. However, the ok test cases for `footstool` will fail if you have not correctly
implemented `microscope`.
"""

def identity_painting(x):
    return identity_painting, x

def microscope(a=0, s=1):
    """
    This function returns a painting function that processes a sequence
    of integers, and returns the alternating sum of all integers seen thus
    far (see doctest for an example).

    >>> painting_a = microscope()
    >>> painting_b, x = painting_a(2)
    >>> x                                   # 2
    2
    >>> painting_c, x = painting_b(8)
    >>> x                                   # 2 - 8
    -6
    >>> painting_d, x = painting_c(12)
    >>> x                                   # 2 - 8 + 12
    6
    >>> painting_e, x = painting_d(30)
    >>> x                                   # 2 - 8 + 12 - 30
    -24
    >>> painting_b_again, x = painting_a(100)
    >>> x                                   # 100 [note that we are using painting_a not painting_d here]
    100
    """
    def painting(x):
        return microscope(a+s*x, -s), a+s*x
    return painting

def footstool(painting, items):
    """
    The function `footstool` takes in a `painting` and a nonempty list of `items` and
    runs the given `painting` on each of the `items` in turn, returning the final
    numeric result.

    For example, on the items [1, 2, 3, 4, 5] with the painting microscope
    we return 1 - 2 + 3 - 4 + 5 = 3

    >>> footstool(microscope(), [1, 2, 3, 4, 5])
    3
    >>> footstool(microscope(), [4000])
    4000
    >>> footstool(microscope(), [2, 90])
    -88
    >>> footstool(identity_painting, [2, 90])
    90
    """
    painting, x = painting(items[0])[0], items[1:]
    if len(x) <= 1:
        return painting(x[0])[1] if x else items[0]
    return footstool(painting, x)


# ORIGINAL SKELETON FOLLOWS

# """
# Let a `painting` be a self-referential function that
#     - takes in one integer
#     - returns two values, another painting and well as an integer

# For an example see the function `identity_painting` below.

# You have two tasks in this assignment, to implement the functions `microscope`
# and `footstool`. Both have their behavior defined by their doctests.

# It is not necessary to implement `microscope` correctly to get the points for
# `footstool`. However, the ok test cases for `footstool` will fail if you have not correctly
# implemented `microscope`.
# """

# def identity_painting(x):
#     return identity_painting, x

# def microscope(a=0, s=1):
#     """
#     This function returns a painting function that processes a sequence
#     of integers, and returns the alternating sum of all integers seen thus
#     far (see doctest for an example).

#     >>> painting_a = microscope()
#     >>> painting_b, x = painting_a(2)
#     >>> x                                   # 2
#     2
#     >>> painting_c, x = painting_b(8)
#     >>> x                                   # 2 - 8
#     -6
#     >>> painting_d, x = painting_c(12)
#     >>> x                                   # 2 - 8 + 12
#     6
#     >>> painting_e, x = painting_d(30)
#     >>> x                                   # 2 - 8 + 12 - 30
#     -24
#     >>> painting_b_again, x = painting_a(100)
#     >>> x                                   # 100 [note that we are using painting_a not painting_d here]
#     100
#     """
#     def painting(x):
#         return ______, ______
#     ______

# def footstool(painting, items):
#     """
#     The function `footstool` takes in a `painting` and a nonempty list of `items` and
#     runs the given `painting` on each of the `items` in turn, returning the final
#     numeric result.

#     For example, on the items [1, 2, 3, 4, 5] with the painting microscope
#     we return 1 - 2 + 3 - 4 + 5 = 3

#     >>> footstool(microscope(), [1, 2, 3, 4, 5])
#     3
#     >>> footstool(microscope(), [4000])
#     4000
#     >>> footstool(microscope(), [2, 90])
#     -88
#     >>> footstool(identity_painting, [2, 90])
#     90
#     """
#     painting, x = ______
#     if ______:
#         return ______
#     return ______

