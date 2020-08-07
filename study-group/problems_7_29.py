"""
CS61A Study Group Pset #06

7/29/2020

SEE BOTTOM FOR DOCTEST INSTRUCTIONS
"""



"""
SCHEME

Uh oh! Someone evaluated (define * +). 
Now (* 3 2) evaluates to 5 instead of 6! 
Let’s fix it.

Important: Answer all questions on this page without 
calling the built-in multiplication procedure.

Implement mulxy, which multiplies integers x and y. 
Hint: (- 2) evaluates to -2.

NOTE: you will want to either run scheme with the 
interpreter given in lab10 OR use scheme.cs61a.org. 
I will look into a cleaner setup for next time.

Alternatively, you can treat this as a pencil-and-paper 
problem for now and check your answers with the interpreter later.
"""

# mulxy
'''
;; multiply x by y (without using the * operator).
;; (mulxy 3 4) -> 12 ; 12 = 3 + 3 + 3 + 3
;; (mulxy (- 3) (- 4)) -> 12 ; 12 = - ( -3 + -3 + -3 + -3 )
(define (mulxy x y)
    (cond ((< y 0) (- (mulxy x (- y)) ))
        ((= y 0) 0)
        (else ( + x (mulxy x (- y 1) )))))
'''

# Original skeleton
# '''
# ;; multiply x by y (without using the * operator).
# ;; (mulxy 3 4) -> 12 ; 12 = 3 + 3 + 3 + 3
# ;; (mulxy (- 3) (- 4)) -> 12 ; 12 = - ( -3 + -3 + -3 + -3 )
# (define (mulxy x y)
#     (cond ((< y 0) (- ____________________ ))
#         ((= y 0) 0)
#         (else ( ____________________ x (mulxy x ____________________ )))))
# '''




"""
LINKED LISTS

Implement outer, a helper function for palinkdrome. 
The palinkdrome function takes a positive integer n 
and returns a one-argument function that, when called 
repeatedly n times, returns a Link containing the 
sequence of arguments to the repeated calls followed 
by that sequence in reverse order. 

The Link class appears below.
"""

def palinkdrome(n):
    """Return a function that returns a palindrome
    starting with the args of n repeated calls.
           >>> print(palinkdrome(3)(5)(6)(7)) # <5 6 7 7 6 5>
           Link(5, Link(6, Link(7, Link(7, Link(6, Link(5))))))
           >>> print(palinkdrome(1)(4)) # <4 4>
           Link(4, Link(4))

    """
    return outer(Link.empty, n)

def outer(r, n):
    def inner(k):
        s = Link(k, ____________________)
        if n == 1:
            t = ____________________
            while s is not Link.empty:
                t, s = Link(____________________, ____________________) , ____________________
            return t
        else:
            return ____________________
    return ____________________

# Original skeleton
# def palinkdrome(n):
#     """Return a function that returns a palindrome
#     starting with the args of n repeated calls.
#            >>> print(palinkdrome(3)(5)(6)(7))
#            <5 6 7 7 6 5>
#            >>> print(palinkdrome(1)(4))
#            <4 4>
#     """
#     return outer(Link.empty, n)
#
# def outer(r, n):
#     def inner(k):
#         s = Link(k, ____________________)
#         if n == 1:
#             t = ____________________
#             while s is not Link.empty:
#                 t, s = Link(____________________, ____________________) , ____________________
#                 return t
#         else:
#             return ____________________
#         return ____________________


# Linked List class as seen in lecture
class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link) # also True is rest is an instc of a subclass of Link
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = f", {repr(self.rest)}"
        else:
            rest_str = ''
        return f"Link({self.first}{rest_str})"

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value



"""
HOF

Write three_sum_budget, which takes in three nonempty lists 
of positive numbers and a number n. This function should return 
the maximum sum less than or equal to n of one element from each 
of lst1, lst2, and lst3. If staying less than or equal to n is 
not possible, return 0.
"""
def three_sum_budget(lst1, lst2, lst3, n):
    """Find the maximum sum <= n of one element from each of lst1, lst2, and lst3.
    >>> three_sum_budget([1, 2, 3], [6, 8, 10], [4], 100)
    17
    >>> three_sum_budget([1, 2, 4], [6, 8, 10], [2], 15)
    14
    >>> three_sum_budget([1, 2, 3], [4, 5, 6], [1, 2, 4], 6)
    6
    """
    def helper(lst1, lst2, lst3, total):
        if ____________________:
            return 0
        elif lst1 == "done":
            return ____________________
        options = []
        for item in lst1:
            options.append(____________________)
        return ____________________
    return helper(lst1, lst2, lst3, 0)

# Original skeleton
# def three_sum_budget(lst1, lst2, lst3, n):
#     """Find the maximum sum <= n of one element from each of lst1, lst2, and lst3.
#     >>> three_sum_budget([1, 2, 3], [6, 8, 10], [4], 100)
#     17
#     >>> three_sum_budget([1, 2, 4], [6, 8, 10], [2], 15)
#     14
#     >>> three_sum_budget([1, 2, 3], [4, 5, 6], [1, 2, 4], 6)
#     6
#     """
#     def helper(lst1, lst2, lst3, total):
#         if ____________________:
#             return 0
#         elif lst1 == "done":
#             return ____________________
#         options = []
#         for item in lst1:
#             options.append(____________________)
#         return ____________________
#     return helper(lst1, lst2, lst3, 0)



"""
RECURSION

A sequence is near increasing if each element but the last two is 
smaller than all elements following its subsequent element. That is, 
element i must be smaller than elements i + 2, i + 3, i + 4, etc.

Implement near, which takes a non-negative integer n and returns the 
largest near increasing sequence of digits within n as an integer. 
The arguments smallest and d are part of the implementation; you must 
determine their purpose. You may not call is_near or fast_near. You 
may not use any values except integers and booleans (True and False) 
in your solution (no lists, strings, etc.).

NOTE: yes, we have all seen (and struggled with) this problem before!
See if you can get it this time!
"""
def near(n, smallest=10, d=10):
    """Return the longest sequence of near-increasing digits in n.
           >>> near(123)
           123
           >>> near(153)
           153
           >>> near(1523)
           153
           >>> near(15123)
           1123
           >>> near(11111111)
           11
           >>> near(985357)
           557
           >>> near(14735476)
           143576
           >>> near(812348567)
           1234567
    """
    if n == 0:
        return ____________________
    no = near(n//10, smallest, d)
    if smallest > ____________________:
        yes = ____________________
        return ____________________(yes, no)
    return ____________________


# Original skeleton
# def near(n, smallest=10, d=10):
#     """Return the longest sequence of near-increasing digits in n.
#            >>> near(123)
#            123
#            >>> near(153)
#            153
#            >>> near(1523)
#            153
#            >>> near(15123)
#            1123
#            >>> near(11111111)
#            11
#            >>> near(985357)
#            557
#            >>> near(14735476)
#            143576
#            >>> near(812348567)
#            1234567
#     """
#     if n == 0:
#         return ____________________
#     no = near(n//10, smallest, d)
#     if smallest > ____________________:
#         yes = ____________________
#         return ____________________(yes, no)
#     return ____________________



if __name__ == '__main__':
    import doctest

    # uncomment to test all funcs
    # doctest.testmod()

    # run doctests for a specific function by replacing func_name with the name of the func you want to test
    doctest.run_docstring_examples(func_name, globals(), verbose=True)