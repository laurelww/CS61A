"""
CS61A Study Group Pset #08

7/31/2020

SEE BOTTOM FOR DOCTEST INSTRUCTIONS
"""



"""
ITERATORS AND GENERATORS

You are in an apocalyptic society and have been charged with
making an n-gen, or a generator that computes all of the n-perfect
numbers. However, in this apocalyptic society, built-in AND
user-defined Python multiplication is forbidden in any form!

You have a blueprint for building a few n-gins from a natural
number generator:

A 2-gen:
1 2 3 4 5 6 7 8 9 ...
1   4   9   16  25 ...

A 3-gen:
1 2 3 4 5 6 7 8 9 ...
1 3   7 12 19 27 ...
1     8    27 ...

Hint: Here is how yield from works.
When used inside an iterable yield from
will issue each element from another
iterable as though it was issued from
the first iterable. The following code
is equivalent:

def generator1 ():
    for item in generator2 ():
        yield item
    # do more things in this generator

and

def generator1 ():
    yield from generator2 ()
    # more things on this generator

Now its your job to build the perfect n-gen
and power society out of the apocalypse! Good luck!
"""

def nats():
    """
    A generator that yields all natural numbers.
    Might be helpful!
    """
    curr = 0
    while True:
        curr += 1
        yield curr

def create_skip(n, gen ):
    if n == 1:

        yield from ___________________
    curr , skip = ________ , ________
    for elem in ____________:
        if skip == n:
            ___________________
        else:
            curr = __________________
            skip = _________________
            yield _________________


def perfect_ngen(n):
    """
    >>> two_gen = perfect_ngen(2)
    >>> next(two_gen)
    1
    >>> next(two_gen)
    4
    >>> next(two_gen)
    9
    >>> three_gen = perfect_ngen(3)
    >>> next(three_gen)
    1
    >>> next(three_gen)
    8
    >>> next(three_gen)
    27
    """
    gen = create_skip(____, _______)
    while _________________:
        n = _________________
        gen = create_skip(____, _______)
    return gen

# Original skeleton
# def create_skip(n, gen ):
#     if n == 1:
#
#         yield from ___________________
#     curr , skip = ________ , ________
#     for elem in ____________:
#         if skip == n:
#             ___________________
#         else:
#             curr = __________________
#             skip = _________________
#             yield _________________
#
#
# def perfect_ngen(n):
#     """
#     >>> two_gen = perfect_ngen(2)
#     >>> next(two_gen)
#     1
#     >>> next(two_gen)
#     4
#     >>> next(two_gen)
#     9
#     >>> three_gen = perfect_ngen(3)
#     >>> next(three_gen)
#     1
#     >>> next(three_gen)
#     8
#     >>> next(three_gen)
#     27
#     """
#     gen = create_skip(____, _______)
#     while _________________:
#         n = _________________
#         gen = create_skip(____, _______)
#     return gen


"""
TREE RECURSION

Ava suggests using a technique called binary search. 
Caleb’s first guess should still be the number in the 
middle of the range.
    • If the secret is lower than the guess, 
        Caleb performs binary search again on 
        a new range from low to guess.
    • If the secret is higher than the guess, 
        Caleb performs binary search again on 
        a new range from guess to high.
        
For example, suppose the range is 0 to 100 (inclusive). 
Caleb starts at 50. Ava responds with -1, indicating the 
secret is lower than 50. Caleb then performs binary search 
on the range 0 to 50 (inclusive); his next guess is 25. 
Ava now responds with 1, indicating the secret is higher 
than 25. Continuing with this process, Caleb makes 5 guesses 
in total (50, 25, 37, 43, 40).

Implement binary_search, which takes in a direction function 
(as returned by make_direction) and returns the number of guesses 
it takes for binary search to find the secret. binary_search 
should also print out the sequence of guesses.
"""

def binary_search(low, high, direction):
    """
    Guesses the secret number, as specified
    by direction, using binary search; returns
    the number of guesses made.
    >>> count1 = binary_search(0, 100, make_direction(50))
    50
    >>> count1
    1
    >>> count2 = binary_search(0, 100, make_direction(40))
    50
    25
    37
    43
    40
    >>> count2
    5
    """
    guess = (low + high) // 2 # midpoint
    ____________________________________
    sign = _____________________________
    if _________________________________:
        return 1
    elif sign < 0:
        return ______________________________________________
    else:
        return ______________________________________________

# Original skeleton
# def binary_search(low, high, direction):
#     """
#     Guesses the secret number, as specified
#     by direction, using binary search; returns
#     the number of guesses made.
#     >>> count1 = binary_search(0, 100, make_direction(50))
#     50
#     >>> count1
#     1
#     >>> count2 = binary_search(0, 100, make_direction(40))
#     50
#     25
#     37
#     43
#     40
#     >>> count2
#     5
#     """
#     guess = (low + high) // 2 # midpoint
#     ____________________________________
#     sign = _____________________________
#     if _________________________________:
#         return 1
#     elif sign < 0:
#         return ______________________________________________
#     else:
#         return ______________________________________________


"""
TREES
    
Given a binary search tree and an entry, return the path in 
order to reach the entry from the root in the form of a list.

The BinTree class is defined below.
"""

def pathfinder(bst, entry):
    """
    >>> bintree = BinTree(4, BinTree(2, BinTree(1)), BinTree(5))
    >>> pathfinder(bst, 2)
    [4, 2]
    >>> pathfinder(bst, 1)
    [4, 2, 1]
    """
    if __________________________________________:
        __________________________________________
    elif __________________________________________:
        __________________________________________
    elif __________________________________________:
        return __________________________________________
    else:
        return _________________________________________________

# Original skeleton
# def pathfinder(bst, entry):
#     """
#     >>> bintree = BinTree(4, BinTree(2, BinTree(1)), BinTree(5))
#     >>> pathfinder(bst, 2)
#     [4, 2]
#     >>> pathfinder(bst, 1)
#     [4, 2, 1]
#     """
#     if __________________________________________:
#         __________________________________________
#     elif __________________________________________:
#         __________________________________________
#     elif __________________________________________:
#         return __________________________________________
#     else:
#         return _________________________________________________


    # BinTree class
class BinTree:
    empty = ()
    def __init__(self, label, left=empty, right=empty):
        self.label = label
        self.left = left
        self.right = right



if __name__ == '__main__':
    import doctest

    # uncomment to test all funcs
    # doctest.testmod()

    # run doctests for a specific function by replacing func_name with the name of the func you want to test
    doctest.run_docstring_examples(func_name, globals(), verbose=True)