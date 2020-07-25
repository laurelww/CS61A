"""
CS61A Study Group Pset #02

7/22/2020

SEE BOTTOM FOR DOCTEST INSTRUCTIONS
"""

"""
HOF

Definition. An (n)-repeater for a single-argument function f takes a single argument x, calls f(x) n times,
then returns an (n + 1)-repeater for f.

Implement repeater, which takes a single-argument function f and a positive integer n. It returns
an (n)-repeater for f. Also implement the helper function repeat.
"""
def repeater(f, n):
    """Return an (n)-repeater for f.
    >>> r = repeater(print, 2)
    >>> s = r('CS')
    CS
    CS
    >>> t = s('CS')
    CS
    CS
    CS
    """
    def g(x):
        repeat(f, x, n)
        return repeater(f, n+1)
    return g

def repeat(f, x, n):
    """Call f(x) n times.

    >>> repeat(print, 'Hello', 3)
    Hello
    Hello
    Hello
    """
    if n > 0:
        for _ in range(n):
            f(x)



# ORIGINAL SKELETON FOLLOWS
# def repeater(f, n):
#     """Return an (n)-repeater for f.
#     >>> r = repeater(print, 2)
#     >>> s = r('CS')
#     CS
#     CS
#     >>> t = s('CS')
#     CS
#     CS
#     CS
#     """
#     def g(x):
#         ____________________
#         return ____________________
#     return ____________________
#
# def repeat(f, x, n):
#     """Call f(x) n times.
#
#     >>> repeat(print, 'Hello', 3)
#     Hello
#     Hello
#     Hello
#     """
#     if ____________________:
#         ____________________
#         ____________________



"""
RECURSION

Definition. For n > 1, an order n function takes one argument and returns an order n−1 function.
An order 1 function is any function that takes one argument.

Implement scurry, which takes a function f and a positive integer n. f must 
be a function that takes a list as its argument. Scurry returns an order n 
function that, when called successively n times on a sequence of values 
x1, x2, . . . xn, returns the result of calling f on a list containing 
x1, x2, . . . xn.
"""
def scurry(f, n):
    """Return a function that calls f on a list of arguments after being called n times.
    >>> scurry(sum, 4)(1)(1)(3)(2) # equivalent to sum([1, 1, 3, 2])
    7
    >>> scurry(len, 3)(7)([8])(-9) # equivalent to len([7, [8], -9])
    3
    """
    def h(k, args_so_far):
        if k == 0:
            return f(args_so_far)
        return lambda x: h(k-1, args_so_far + [x])
    return h(n, [])



# ORIGINAL SKELETON FOLLOWS
# def scurry(f, n):
#     """Return a function that calls f on a list of arguments after being called n times.
#     >>> scurry(sum, 4)(1)(1)(3)(2) # equivalent to sum([1, 1, 3, 2])
#     7
#     >>> scurry(len, 3)(7)([8])(-9) # equivalent to len([7, [8], -9])
#     3
#     """
#     def h(k, args_so_far):
#         if k == 0:
#             return ____________________
#         return ____________________
#     return ____________________



if __name__ == '__main__':
    import doctest

    # uncomment to test all funcs
    # doctest.testmod()

    # run doctests for a specific function by replacing func_name with the name of the func you want to test
    doctest.run_docstring_examples(func_name, globals(), verbose=True)