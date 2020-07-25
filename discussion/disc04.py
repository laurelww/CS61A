def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if m < 0 or n < 0:
        return -multiply(m, n)
    if n == 1:
        return m
    else:
        return m + multiply(m, n - 1)
    
def mul(m,n):
    """
    >>> mul(5, 3)
    15
    >>> mul(8, 4)
    not 120
    """
    if m == 1 or n==1:         
        return 1          
    else:         
        return mul(m-1,n) + mul(m, n-1)

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(n, factor):
        if n == 1 or n % factor == 0:
            return False
        elif factor > n**0.5:
            return True
        else:
            return prime_helper(n, factor + 1)
    return prime_helper(n, 2)

def count_stair_ways(n):
    """
    >>> count_stair_ways(4)
    5
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1 + count_stair_ways(n - 1)
    # elif n == 0:
    #     return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def max_product(s):
    """
    >>> max_product([10, 3, 1, 9, 2])
    90
    >>> max_product([5, 10, 5, 10, 5])
    125

    :param s:
    :return:
    """
    options = []
    for idx in range(len(s)):
        options.append(s[idx])
        options.append([s[x] for x in range(len(s)) if abs(x - idx) > 1])
    products = []
    for list in options:
        products.append()

def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    """
    if len(str(n)) == 3:
        return n % 10 > n//10 %10 and n//100 %10 > n//10 %10
    return check_hole_number(int(str(n)[1:-1]))