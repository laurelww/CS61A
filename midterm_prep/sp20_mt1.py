def same_digits(a, b):
    """

    >>> same_digits(2002200, 2202000)
    True
    >>> same_digits(20, 20)
    True
    >>> same_digits(220202200, 2202002200)
    True
    >>> same_digits(21, 12)
    False
    >>> same_digits(12, 2212)
    False
    >>> same_digits(2020, 20)
    False
    """
    while a and b:
        if a != b:
            end = a % 10
            if end != b % 10:
                a = a // 10
            else:
                b = b // 10
        else:
            return True
    return False

def compose(n):
    """
    >>> add1 = lambda y: y + 1
    >>> compose(3)(abs)(add1)(add1)(-4)
    2
    >>> compose(3)(add1)(add1)(abs)(-4)
    6
    >>> compose(1)(abs)(-4)
    4
    """
    if n == 1:
        return lambda f: lambda n: f(n)
    def call(f):
        def on(g):
            return compose(n-1)(lambda x: f(g(x)))
        return on
    return call

from operator import add
c = lambda f: lambda x: lambda y: f(x, y)
twice = lambda z: 2*z
print(compose(3)(twice)(c(add)(10))(c(pow)(10))(3))


def ups(k):
    def f(left, right):
        return ups(k-1 if left < right else k)
    return f, lambda: k == 0


def is_subseq(w1, w2):
    """
    >>> is_subseq("word", "word")
    True
    >>> is_subseq("compute", "computer")
    True
    >>> is_subseq("put", "computer")
    True
    >>> is_subseq("computer", "put")
    False
    >>> is_subseq("sin", "science")
    True
    >>> is_subseq("nice", "science")
    False
    >>> is_subseq("boot", "bottle")
    False
    """
    if w1 in w2:
        return True
    elif w2 < w1:
        return False
    else:
        with_elem = w1[0] in w2 and is_subseq(w1[1:], w2[1:])
        without_elem = is_subseq(w1[1:], w2[1:])
        return with_elem or without_elem