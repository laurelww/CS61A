"""
HOF Envirograms

"""

def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x

def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3

def make_adder(n):
    def adder(k):
        return k + n
    return adder


if __name__ == "__main__":
    # print(square(10))
    # print(apply_twice(square, 3))
    # print(square)
    repeat(g, 5)