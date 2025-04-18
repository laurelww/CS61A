"""
CS61A Study Group Pset #10

8/3/2020

SEE BOTTOM FOR DOCTEST INSTRUCTIONS
"""



"""
TAIL RECURSION

Implement a tail-recursive Scheme function called count, 
which takes in a number and a well-formed Scheme list of 
numbers. count returns the number of times the number 
appears in the list.

scm> (count 3 (1 2 3 4 3)) 
2
scm> (count 42 (3 4 2))
0

Remember, your solution must be tail recursive. A reasonable 
solution uses 3 to 4 additional lines of code, but you can 
use fewer or more if you want. Make sure to fill in the blanks 
in the second-to-last line.
"""
"""
(define (count num lst)
    (define (helper lst total)




    )
    (helper ____________ ____________)
)
"""

# Original skeleton
# """
# (define (count num lst)
#     (define (helper lst total)
#
#
#
#
#     )
#     (helper ____________ ____________)
# )
# """



"""
OOP

The TAs are building a social networking website called CS61A+. 
The TAs plan to represent the network in a class called Network 
that supports the following method:
    • add_friend(user1, user2): adds user1 and user2 to each other's 
        friends lists. If user1 or user2 are not in the Network, add them 
        to the dictionary of friends. You may assume user1 and user2 are 
        not already friends.
Help the TAs implement these two methods to make their social 
networking website popular!
"""
class Network:
    """
    >>> cs61a_plus = Network()
    >>> cs61a_plus.add_friend('Roy', 'Charles')
    >>> cs61a_plus.friends['Roy']
    ['Charles']
    >>> cs61a_plus.friends['Charles']
    ['Roy']
    >>> cs61a_plus.add_friend('William', 'Roy')
    >>> cs61a_plus.friends['Roy']
    ['Charles', 'William']
    """
    def __init__(self):
        self.friends = {} # Maps users to a list of their friends

    def add_friend(self, user1, user2):
        if __________________________________________________:
            _________________________________________________
        if __________________________________________________:
            _________________________________________________
        _____________________________________________________
        _____________________________________________________

    # PART 2
    """
    OOP P.2

    CS61A+ turns out to be unpopular. To attract more users, 
    the TAs want to implement a feature that checks if two users 
    have at most n degrees of separation. Consider the following 
    CS61A+ Network:

    self.friends = {'Roy': ['Charles', 'William'],
                    'Charles': ['Roy', 'William', 'Emma'],
                    'William': ['Roy', 'Charles', 'Emma'],
                    'Emma': ['Charles', 'William'],
                    'Oski': []}

    • There are 0 degrees of separation between a person and themselves.
    • There is 1 degree of separation between Roy and Charles, because they are direct friends.
    • There are 2 degrees of separation between Roy and Emma (Roy → William → Emma)
    • The degree of separation between Oski and anyone else is undefined, since Oski has no friends.

    Implement degrees(user1, user2, n), which returns True if user1 and user2 
    are separated by at most n degrees (fewer degrees is okay). You can assume 
    that user1 and user2 are already in the Network.
    """
    def degrees(self, user1, user2, n):
        """In these doctests, assume cs61a_plus is a Network with the
        dictionary of friends described in the example.
        >>> cs61a_plus = Network()
        >>> cs61a_plus.friends = {'Roy': ['Charles', 'William'],
        ...                'Charles': ['Roy', 'William', 'Emma'],
        ...                'William': ['Roy', 'Charles', 'Emma'],
        ...                'Emma': ['Charles', 'William'],
        ...                'Oski': []}
        >>> cs61a_plus.degrees('Roy', 'Emma', 2) # Exactly 2 degrees
        True
        >>> cs61a_plus.degrees('Roy', 'William', 2) # Less than 2 degrees
        True
        >>> cs61a_plus.degrees('Emma', 'Roy', 1) # More than 1 degree
        False
        >>> cs61a_plus.degrees('Roy', 'Roy', 2) # 0 degrees
        True
        >>> cs61a_plus.degrees('Oski', 'William', 10) # No friends!
        False
        """
        if ______________________________________:
            return ___________
        elif ____________________________________:
            return ___________
        for friend in _______________________________:
            if ______________________________________:
                return True
        return ______________________________________

# Original skeleton
# class Network:
#     """
#     >>> cs61a_plus = Network()
#     >>> cs61a_plus.add_friend('Roy', 'Charles')
#     >>> cs61a_plus.friends['Roy']
#     ['Charles']
#     >>> cs61a_plus.friends['Charles']
#     ['Roy']
#     >>> cs61a_plus.add_friend('William', 'Roy')
#     >>> cs61a_plus.friends['Roy']
#     ['Charles', 'William']
#     """
#     def __init__(self):
#         self.friends = {} # Maps users to a list of their friends
#
#     def add_friend(self, user1, user2):
#         if __________________________________________________:
#             _________________________________________________
#         if __________________________________________________:
#             _________________________________________________
#         _____________________________________________________
#         _____________________________________________________
#
#     # PART 2
#     """
#     OOP P.2
#
#     CS61A+ turns out to be unpopular. To attract more users,
#     the TAs want to implement a feature that checks if two users
#     have at most n degrees of separation. Consider the following
#     CS61A+ Network:
#
#     self.friends = {'Roy': ['Charles', 'William'],
#                     'Charles': ['Roy', 'William', 'Emma'],
#                     'William': ['Roy', 'Charles', 'Emma'],
#                     'Emma': ['Charles', 'William'],
#                     'Oski': []}
#
#     • There are 0 degrees of separation between a person and themselves.
#     • There is 1 degree of separation between Roy and Charles, because they are direct friends.
#     • There are 2 degrees of separation between Roy and Emma (Roy → William → Emma)
#     • The degree of separation between Oski and anyone else is undefined, since Oski has no friends.
#
#     Implement degrees(user1, user2, n), which returns True if user1 and user2
#     are separated by at most n degrees (fewer degrees is okay). You can assume
#     that user1 and user2 are already in the Network.
#     """
#     def degrees(self, user1, user2, n):
#         """In these doctests, assume cs61a_plus is a Network with the
#         dictionary of friends described in the example.
#         >>> cs61a_plus = Network()
#         >>> cs61a_plus.friends = {'Roy': ['Charles', 'William'],
#         ...                'Charles': ['Roy', 'William', 'Emma'],
#         ...                'William': ['Roy', 'Charles', 'Emma'],
#         ...                'Emma': ['Charles', 'William'],
#         ...                'Oski': []}
#         >>> cs61a_plus.degrees('Roy', 'Emma', 2) # Exactly 2 degrees
#         True
#         >>> cs61a_plus.degrees('Roy', 'William', 2) # Less than 2 degrees
#         True
#         >>> cs61a_plus.degrees('Emma', 'Roy', 1) # More than 1 degree
#         False
#         >>> cs61a_plus.degrees('Roy', 'Roy', 2) # 0 degrees
#         True
#         >>> cs61a_plus.degrees('Oski', 'William', 10) # No friends!
#         False
#         """
#         if ______________________________________:
#             return ___________
#         elif ____________________________________:
#             return ___________
#         for friend in _______________________________:
#             if ______________________________________:
#                 return True
#         return ______________________________________


"""
LISTS

Implement a Python function called subsequences(lst), which 
takes in a Python list of unique numbers. subsequences returns 
a list of all subsequences of lst.

A list A is a subsequence of list B if A contains zero or more 
elements of B in the same order that they appear in B.

See the doctests for expected behavior. We will not penalize you 
for returning the subsequences in a different order than the doctests. 
However, the order of elements within a subsequence must be correct.
"""
def subsequences(lst):
    """
    >>> result = subsequences([1, 2, 3])
    >>> for subsequence in subsequences([1, 2, 3]):
    ...     print(subsequence)
    []
    [3]
    [2]
    [2, 3]
    [1]
    [1, 3]
    [1, 2]
    [1, 2, 3]
    """
    if lst == []:
        return ____________
    without_first = ____________________________________________
    with_first = [____________________ for ________ in ___________________]
    return ________________________________________

# Original skeleton
# def subsequences(lst):
#     """
#     >>> result = subsequences([1, 2, 3])
#     >>> for subsequence in subsequences([1, 2, 3]):
#     ...     print(subsequence)
#     []
#     [3]
#     [2]
#     [2, 3]
#     [1]
#     [1, 3]
#     [1, 2]
#     [1, 2, 3]
#     """
#     if lst == []:
#         return ____________
#     without_first = ____________________________________________
#     with_first = [____________________ for ________ in ___________________]
#     return ________________________________________



if __name__ == '__main__':
    import doctest

    # uncomment to test all funcs
    # doctest.testmod()

    # run doctests for a specific function by replacing func_name with the name of the func you want to test
    # to run degrees, use name Network.degrees
    doctest.run_docstring_examples(func_name, globals(), verbose=True)