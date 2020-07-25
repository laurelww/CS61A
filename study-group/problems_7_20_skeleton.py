"""
CS61A Study Group Pset #01

7/20/2020

SEE BOTTOM FOR DOCTEST INSTRUCTIONS
"""


"""
LAMBDAS

Implement the fset function, which returns two functions that
together represent a set. Both the add and has functions return
whether a value is already in the set. The add function also adds
its argument value to the set. You may assign to only one name in
the assignment statement. You may not use any built-in container,
such as a set or dictionary or list.
"""
def fset():
    """Return two functions that together represent a set.
    >>> add, has = fset()
    >>> [add(1), add(3)]        # Neither 1 nor 3 were already in the set
    [False, False]
    >>> [has(k) for k in range(5)]
    [False, True, False, True, False]
    >>> [add(3), add(2)]        # 3 was already in the set; 2 is added
    [True, False]
    >>> [has(k) for k in range(5)]
    [False, True, True, True, False]
    """

    items = lambda x: ____________________

    def add(y):
        ____________________
        f = items
        _______ = ____________________
        return ____________________

    return add, ____________________


"""
CONTROL

Definition. A palindrome is a sequence that has the same elements 
in normal and reverse order.

Implement pal, which takes a positive integer n and returns a positive 
integer with the digits of n followed by the digits of n in reverse order.

Important: You may not write str, repr, list, tuple, [, or ].
"""
def pal(n):
    """Return a palindrome starting with n.
    >>> pal(12430)
    1243003421
    """
    m = n

    while m:
        n, m = ____________________, ____________________

    return n


"""
LISTS

Implement winner, which takes a number price and returns a function. 
The function takes a list of numbers guesses and returns the largest 
guess that is less than or equal to the price.

Important: Fill each blank with only a single name. You may use built-in 
functions such as min; other built-in functions are listed on the front 
of the exam: min, max, pow, len, abs, sum, next, iter, list, sorted, 
             reversed, tuple, map, filter, zip, all, and any.
"""
def winner(price):
    """Return a function that takes a list and returns
    the largest element not above price.
    >>> ipad = winner(499) # the iPad actual price is $499
    >>> ipad([500, 600, 200, 1, 350, 299]) # the closest guess that doesn't go over is $350
    350
    """
    return lambda guesses: ________(________(lambda g: ________ <= ________, _____________))

if __name__ == '__main__':
    import doctest

    # uncomment to test all funcs
    # doctest.testmod()

    # run doctests for a specific function by replacing func_name with the name of the func you want to test
    doctest.run_docstring_examples(func_name, globals(), verbose=True)