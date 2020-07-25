"""
Tree recursion
"""
from ucb2 import trace

@trace
def fib(n):
    """
    Not a great way to count fib numbers!

    :param n:
    :return:
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

def paths(m, n):
    """
    Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m - 1, n) + paths(m, n - 1)

def knapsack(n, k):
    if n == 0:
        return k == 0
    with_last = knapsack(n // 10, k - n % 10)
    without_last = knapsack(n // 10, k)
    return with_last or without_last

def count_partitions(n, m):
    """
    Count the number of partitions of a positive integer N,
    using parts up to size K.

    - Include at least one k
    - Don't include k

    Base cases:
    n or k == 0

    Recursive cases:
    (n - k, k)
    (n, k - 1)

    :return:
    """
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
    return with_m + without_m

def all_nums(k):
    """
    Print all numbers length K containing digits 0 or 1.

    >>> all_nums(3)
    0
    1
    10
    11
    100
    101
    110
    111

    """
    def h(k, prefix):
        if k == 0:
            print(prefix)
            return

        h(k - 1, prefix * 10)
        h(k - 1, prefix * 10 + 1)
    h(k, 0)

"""
Implementing functions
"""

def remove(n, digit):
    """
    remove(231, 3)

    n = 23, last = 1
        kept = 1 *10**0 + 0 = 1
        digits = 1
    n = 2, last = 3
    n = 0, last = 2 # n == 0, so why doesn't the loop break?
        kept = 2 * 10**1 + 1 = 21
        digits = 2
    # now n == 0 is recognized so the while loop ends
    return 21

    """

    kept, digits = 0, 0
    while n != 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = last * 10 ** digits + kept
            digits = digits + 1
    return kept


if __name__ == "__main__":
    # print(fib(20))
    # fib(35)
    # print(paths(2, 2))
    # print(paths(5, 7))
    # print(knapsack(689, 15))
    # print(knapsack(689, 16))
    # print(count_partitions(2, 2))
    print(all_nums(2))
    print(remove(231, 3))
    print(remove(243132, 2))