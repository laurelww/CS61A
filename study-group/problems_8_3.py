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
        (cond
            (null? (car lst) total)
            ((= (car lst) num) (helper (cdr lst) (+ 1 total)))
            (else (helper (cdr lst) total)))
        )
    )
    (helper lst 0) 
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
    >>> cs61a_plus.add_friend('Robert', 'Jeffrey')
    >>> cs61a_plus.friends['Robert']
    ['Jeffrey']
    >>> cs61a_plus.friends['Jeffrey']
    ['Robert']
    >>> cs61a_plus.add_friend('Jessica', 'Robert')
    >>> cs61a_plus.friends['Robert']
    ['Jeffrey', 'Jessica']
    >>> cs61a_plus.degrees('Robert', 'Yulin', 2) # Exactly 2 degrees
    True
    >>> cs61a_plus.degrees('Robert', 'Jessica', 2) # Less than 2 degrees
    True
    >>> cs61a_plus.degrees('Yulin', 'Robert', 1) # More than 1 degree
    False
    >>> cs61a_plus.degrees('Robert', 'Robert', 2) # 0 degrees
    True
    >>> cs61a_plus.degrees('Albert', 'Jessica', 10) # No friends!
    False
    """
    def __init__(self):
        self.friends = {} # Maps users to a list of their friends

    def add_friend(self, user1, user2):
        if user1 not in self.friends:
            self.friends[user1] = [user2]
        if user2 not in self.friends:
            self.friends[user2] = [user1]
        self.friends[user1] += [user2]
        self.friends[user2] += [user1]

    # PART 2
    """
    OOP P.2

    CS61A+ turns out to be unpopular. To attract more users, 
    the TAs want to implement a feature that checks if two users 
    have at most n degrees of separation. Consider the following 
    CS61A+ Network:

    self.friends = {'Robert': ['Jeffrey', 'Jessica'],
                    'Jeffrey': ['Robert', 'Jessica', 'Yulin'],
                    'Jessica': ['Robert', 'Jeffrey', 'Yulin'],
                    'Yulin': ['Jeffrey', 'Jessica'],
                    'Albert': []}

    • There are 0 degrees of separation between a person and themselves.
    • There is 1 degree of separation between Robert and Jeffrey, because they are direct friends.
    • There are 2 degrees of separation between Robert and Yulin (Robert → Jessica → Yulin)
    • The degree of separation between Albert and anyone else is undefined, since Albert has no friends.

    Implement degrees(user1, user2, n), which returns True if user1 and user2 
    are separated by at most n degrees (fewer degrees is okay). You can assume 
    that user1 and user2 are already in the Network.

    """
    def degrees(self, user1, user2, n):
        """In these doctests, assume cs61a_plus is a Network with the dictionary of friends described in the example.

        """
        if user1 == user2:
            return True
        elif n < 0:
            return False
        for friend in self.friends:
            if self.degrees(user1, friend, n-1):
                return True
        return False

# Original skeleton
# class Network:
#     """
#     >>> cs61a_plus = Network()
#     >>> cs61a_plus.add_friend('Robert', 'Jeffrey')
#     >>> cs61a_plus.friends['Robert']
#     ['Jeffrey']
#     >>> cs61a_plus.friends['Jeffrey']
#     ['Robert']
#     >>> cs61a_plus.add_friend('Jessica', 'Robert') >>> cs61a_plus.friends['Robert']
#     ['Jeffrey', 'Jessica']
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
#     self.friends = {'Robert': ['Jeffrey', 'Jessica'],
#                     'Jeffrey': ['Robert', 'Jessica', 'Yulin'],
#                     'Jessica': ['Robert', 'Jeffrey', 'Yulin'],
#                     'Yulin': ['Jeffrey', 'Jessica'],
#                     'Albert': []}
#
#     • There are 0 degrees of separation between a person and themselves.
#     • There is 1 degree of separation between Robert and Jeffrey, because they are direct friends.
#     • There are 2 degrees of separation between Robert and Yulin (Robert → Jessica → Yulin)
#     • The degree of separation between Albert and anyone else is undefined, since Albert has no friends.
#
#     Implement degrees(user1, user2, n), which returns True if user1 and user2
#     are separated by at most n degrees (fewer degrees is okay). You can assume
#     that user1 and user2 are already in the Network.
#
#     """
#     def degrees(self, user1, user2, n):
#         """In these doctests, assume cs61a_plus is a Network with the dictionary of friends described in the example.
#         >>> cs61a_plus.degrees('Robert', 'Yulin', 2) # Exactly 2 degrees
#         True
#         >>> cs61a_plus.degrees('Robert', 'Jessica', 2) # Less than 2 degrees
#         True
#         >>> cs61a_plus.degrees('Yulin', 'Robert', 1) # More than 1 degree
#         False
#         >>> cs61a_plus.degrees('Robert', 'Robert', 2) # 0 degrees
#         True
#         >>> cs61a_plus.degrees('Albert', 'Jessica', 10) # No friends!
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
        return [[]]
    without_first = subsequences(lst[1:])
    with_first = [[lst[0]] + rest for rest in subsequences(lst[1:])]
    return without_first + with_first

# Original skeleton
# def subsequences(lst):
#     """
#     >>> for subsequence in subsequences([1, 2, 3]):
#     ...    print(subsequence)
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
    doctest.run_docstring_examples(func_name, globals(), verbose=True)