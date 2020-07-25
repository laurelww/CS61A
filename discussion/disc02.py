def print_delayed(x):
    def delayed_print(y):
        print(x)
        return print_delayed(y)
    return delayed_print

def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n + k)
    return next_sum

def print_n(n):
    def inner_print(x):
        if n == 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print




if __name__ == "__main__":
    f = print_delayed(1)
    f = f(2)
    f = f(3)
    f = f(4)
    f = f(5)
    print("next")
    g = print_sums(5)
    g = g(4)
    g = g(3)
    print("next")
    h = print_n(2)
    h = h("one")
    h = h("two")
    h = h("three")