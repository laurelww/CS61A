def close(n, smallest=10, d=10):
    """ A sequence is near increasing if each element but the last two is smaller than all elements
    following its subsequent element. That is, element i must be smaller than elements i + 2, i + 3, i + 4, etc.
    Implement close, which takes a non-negative integer n and returns the largest near increasing sequence
    of digits within n as an integer. The arguments smallest and d are part of the implementation; you must
    determine their purpose. The only values you may use are integers and booleans (True and False) (no lists, strings, etc.).
    Return the longest sequence of near-increasing digits in n.
    >>> close(123)
    123
    >>> close(153)
    153
    >>> close(1523)w
    153
    >>> close(15123)
    1123
    >>> close(11111111)
    11
    >>> close(985357)
    557
    >>> close(14735476)
    143576
    >>> close(812348567)
    1234567
    """
    if n == 0:
      return ______
    no = close(n//10, smallest, d)
    if smallest > ______:
        yes = ______
        return ______(yes, no)
    return ______

def subsets(lst, n):
    """
    >>> three_subsets = subsets(list(range(5)), 3)
    >>> print(three_subsets)
    """
    if n == 0:
        return [[]]
    elif len(lst) == n:
        return [lst]
    else:
        with_elem = [lst[:1] + s for s in subsets(lst[1:], n-1)]
        without_elem = subsets(lst[1:], n)
        # print(with_elem, without_elem)
    return  with_elem + without_elem

    # [0, 1, 2]
    # [0, 1, 3]
    # [0, 1, 4]
    # [0, 2, 3]
    # [0, 2, 4]
    # [0, 3, 4]
    # [1, 2, 3]
    # [1, 2, 4]
    # [1, 3, 4]
    # [2, 3, 4]

def can_win(number):
    """Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game
    from an invalid game state.

    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    """
    if number < 0:
        return False
    elif number <= 3:
        return True
    else:
        take_one = can_win(number - 1)
        take_two = can_win(number - 2)
        take_three = can_win(number - 3)
        return not any([take_one, take_two, take_three])

def scurry(f, n):
    """
    >>> scurry(sum, 4)(1)(1)(3)(2)
    7
    >>> scurry(len, 3)(7)([8])(-9)
    3
    """
    def h(k, args_so_far):
        if k == 0:
            return f(args_so_far)
        return lambda x: h(k-1, args_so_far+[x])
    return h(n, [])


def factorize(n, k=2):
    """
    >>> factorize(7)
    1
    >>> factorize(12)
    4
    >>> factorize(36)
    9
    """
    # print(f"n={n} k={k}")
    if k == n:
        return 1
    elif k > n:
        return 0
    elif n % k > 0:
        # print(n, k)
        return factorize(n, k+1) # without k
    # print(n, k)
    return factorize(n//k, k) + factorize(n, k+1) # with k


def plus(n):
    """
    >>> plus(123456)
    102
    >>> plus(1604)
    65
    >>> plus(160450)
    115
    """
    # with two digits
    # with one digit
    if n:
        return max(n - n//100 * 100 + plus(n//100), n%10 + plus(n//10))
    return 0

def plusses(n, cap):
    """
    >>> plusses(123, 16)
    2
    >>> plusses(2018, 38)
    4
    >>> plusses(1, 2)
    1
    """
    if cap > n and n//10 == 0:
        return 1
    elif not n or not cap:
        return 0
    else:
        return plusses(n//100, cap - (n - n//100 * 100)) + plusses(n//10, cap - n%10)


def runts(t):
    """
    Every label is different
    """
    result = []

    def g(node):

        if not node.is_leaf:
            result.append(min([b.label for b in node.brances]))

    apply_to_nodes(g, t) # returns nothing

    return [t.label] + result


def apply_to_nodes(f, t):
    f(t)
    for b in t.branches:
        apply_to_nodes(f, b)


def sums(n, k):
    """
    >>> sums(2, 2)
    [[1, 1]]
    >>> sums(2, 3)
    []
    >>> sums(4, 2)
    [[3, 1], [2, 2], [1, 3]]
    >>> sums(5, 3)
    [[3, 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
    """
    if k == n:
        return [[1 for _ in range(k)]]
    y = []
    for x in range(1, n+1):
        y.extend([s + [x] for s in sums(n-x, k-1)])
    return y

def is_sorted(n):
    """
    >>> is_sorted(4)
    True
    >>> is_sorted(55555)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    if n//10 == 0:
        return True
    elif not n % 10 <= n//10 %10:
        return False
    else:
        return is_sorted(n//10)

def foo(lst):
    """
    >>> lst = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    >>> foo(lst)
    5
    [[10, 9], [8, 7], [6, 5], [4, 3], [2, 1]]
    [2, 4]
    """
    print(lst[2][0])
    print([[y, x] for x, y in lst][::-1])
    print([x[1] for x in lst if x[1] == 2] + [x[1] for x in lst if x[1] == 4])

def aggregate(fn, seq, pred):
    """
    >>> is_even = lambda x: x%2 == 0
    >>> sum_plus_one = lambda x, y: x+y+1
    >>> aggregate(sum_plus_one, [2, 4, 6], is_even)
    14
    >>> aggregate(sum_plus_one, [1, 3, 5, 7, 9], is_even)
    >>>
    >>> aggregate(sum_plus_one, [1, 2, 3], is_even)
    2
    """
    result = None
    valid_seq = [x for x in seq if pred(x)]
    def apply_to_all(f, lst):
        return lst[0] if len(lst) <= 1 else f(lst[0], apply_to_all(f, lst[1:]))
    if valid_seq:
        result = apply_to_all(fn, valid_seq)
    # _____
    # _____
    return result

def luhn_sum(n):
    """
    >>> luhn_sum(135)
    12
    >>> luhn_sum(185)
    13
    >>> luhn_sum(138743)
    30
    """
    def luhn_digit(digit):
        x = digit * multiplier
        return (x//10) + x%10

    total, multiplier = 0, 1

    while n:
        n, last = n//10, n%10
        total = total + luhn_digit(last)
        multiplier = 3 - multiplier
    return total

def decompose1(f, h):
    """
    >>> add_one = lambda x: x + 1
    >>> square_then_add_one = lambda x: (x * x) + 1
    >>> g = decompose1(add_one, square_then_add_one)
    >>> g(5)
    25
    >>> g(10)
    100
    """
    def g(x):
        def r(y):
            if h(x) == f(y):
                return y
            else:
                return r(y+1)
        return r(0)
    return g