def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1: same as successor(zero)"""
    return lambda f: lambda x: f(zero(f)(x))

def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    return lambda f: lambda x: f(one(f)(x))

three = successor(two)
four = successor(three)

print(four)
print(three)
print(two)
print(one)