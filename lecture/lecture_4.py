"""
Lecture 4 notes

"""

def area_square(r, shape_constant):
    assert r > 0 # prevents negative side length vlas
    return r * r * shape_constant

def make_adder(n):
    def adder(k):
        return k + n
    return adder

def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def curry_two(f):
    return lambda f: lambda x: lambda y: f(x, y)

# Currying -- transforming a multi arg func into a single arg HOF.

"""
Functional abstraction


"""



if __name__ == "__main__":
    from operator import add

    print(square(5))
    print(triple(5))
    squiple = compose1(square, triple)
    print(squiple(5))
    tripare = compose1(triple, square)
    print(tripare(5))
    squadder = compose1(square, make_adder(2))
    print(squadder(3))

    m = curry2(add)
    add_three = m(3)
    print(add_three(2))
