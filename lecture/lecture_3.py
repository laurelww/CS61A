"""
Lecture 3 notes

"""

def search(f):
    """Iterate through values of x until one returns True for f."""
    x = 0
    while not f(x):
        x += 1
    return x

def square(x):
    return x ** 2

def inverse(f):
    """Return g(y) such that f(g(y)) == x."""

    def g(y):
        x = 0
        while not f(x) == y:
            x += 1
        return x
    return g

    # return lambda y: search(lambda x: f(x) == y)

sqrt = inverse(square)
print(square(16))
print(sqrt(256))
