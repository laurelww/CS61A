HW_SOURCE_FILE=__file__


def pascal(row, column):
    """Returns a number corresponding to the value at that location
    in Pascal's Triangle.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 4 (1 3 3 1), 3rd entry
    3
    """
    if row == column:
        return 1
    elif row < column or row == 0:
        return 0
    return pascal(row - 1, column - 1) + pascal(row - 1, column)


def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of func (recursively!).

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    if n == 0:
        return lambda x: x
    if n == 1:
        return f
    return compose1(f, repeated(f, n - 1))


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if x == 0:
        return 0
    if x % 10 == 8:
        return 1 + num_eights(x // 10)
    return num_eights(x // 10)



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """

    def helper(x, inc, ping):
        if x == 0:
            return ping
        if x % 8 == 0 or num_eights(x) > 0:
            return helper(x - 1, -inc, ping) - inc
        return helper(x - 1, inc, ping) + inc

    return -helper(n, 1, 0)






