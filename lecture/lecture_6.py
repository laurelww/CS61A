def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

# Mutual recursion

def luhn(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return luhn_double(all_but_last) + last

def luhn_double(n):
    all_but_last, last = n // 10, n % 10
    luhn_digit = sum_digits_iter(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn(all_but_last) + luhn_digit

def sum_digits_iter(n):
    sum = 0
    while n > 0:
        sum, n = sum + n % 10, n // 10
    return sum

def cascade(n):
    # if n < 10:
    #     print(n)
    # else:
    #     print(n)
    #     cascade(n // 10)
    #     print(n)
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)



def f_then_g_then_h(f, g, h, x, y):
    if x and y:
        f(x)
        g(x, y)
        h(x)

def anon_fac(x):
    while x:
        gro(x)
        x -= 1


gro = lambda x: f_then_g_then_h(lambda p, q: p * q, print, gro, x, x - 1)



if __name__ == "__main__":
    # print(luhn(32))
    # print(luhn(5105105105105100))

    # cascade(3)
    # cascade(12345)
    # cascade(12345)
    # cascade(12345)
    # cascade(12345)

    # inverse_cascade(12345)

    print(anon_fac(5))
