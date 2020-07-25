"""
Upcoming assignments:

modulo 10 will be useful.

"""

"""
    >>> 123456 % 1
    0
    >>> 123456 % 10
    6
    >>> 123456 % 100
    56
    >>> 123456 % 1000
    456
    >>> 123456 % 10000
    3456
    >>> 123456 % 100000
    23456
    >>> 123456 % 1000000
    123456
    >>> 123456 % 10000000
    123456
"""

def fib(n):
    k = 0
    last, next = 1, 0
    while k < n:
        last , next = next, last + next
        k += 1
    return next

print(fib(0))

def term(n, term):
    for x in str(n)[::-1]:
        if x == str(term):
            print(x)
            return
        else:
            print(x)

# term(123456, 2)

def better_term(n, term):
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if last == term:
            return

better_term(123456, 2)