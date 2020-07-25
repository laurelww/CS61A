# def switch(s, t, k):
#     """
#     >>> switch([1, 2, 7], [3, 4, 5], 0)
#     [1, 2, 7]
#     >>> switch([1, 2, 7], [3, 4, 5], 1)
#     [3, 4, 5]
#     >>> switch([1, 2, 7], [3, 4, 5], 2)
#     [3, 4, 7]
#     >>> switch([1, 2, 7], [3, 4, 5], 3)
#     [3, 4, 7]
#     """
#     pass
#
# def max_tree(t, key):
#     pass
#
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
    >>> close(1523)
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
    pass
    # if n == 0:
    #   return ______
    # no = close(n//10, smallest, d)
    # if smallest > ______:
    #     yes = ______
    #     return max(yes, no)
    # return ______

def repeated_digits(n):
    """
    >>> repeated_digits(1234)
    11223344
    """
    last, rest = n%10, n//10
    if not rest:
        return n * 11
    return repeated_digits(rest)* 10**2 + last*11


def eight_path(t):
    """
    >>> t1 = tree(5, [tree(2), tree(1, [tree(3), tree(2)])])
    >>> eight_path(t1)
    [5, 1, 2]
    >>> t2 = tree(9, [t1])
    >>> eight_path(t2)
    [9, 5, 2]
    """
    """
    with =
    Got:
    [5]
    [5, 2]
    [5, 1]
    [5, 1, 3]
    [5, 1, 2]
    [5, 1, 2]
    """
    """
    with +=
    Got:
    [5]
    [5, 2]
    [5, 2, 1]
    [5, 2, 1, 3]
    [5, 2, 1, 3, 2]
    """
    def helper(t, path_so_far):
        path_so_far = path_so_far + [label(t)]
        # path_so_far += [label(t)]
        # print(path_so_far)
        if is_leaf(t) and sum(path_so_far) % 8 == 0:
            return path_so_far
        for b in branches(t):
            result = helper(b, path_so_far)
            if result:
                return result
    return helper(t, [])


def sabacc_winner(cards, player0, player1):
    """
    >>> sabacc_winner(0, 'Han', 'Lando')
    'Han'
    >>> sabacc_winner(1, 'Han', 'Lando')
    'Lando'
    >>> sabacc_winner(2, 'Han', 'Lando')
    'Han'
    >>> sabacc_winner(3, 'Han', 'Lando')
    'Han'
    >>> sabacc_winner(4, 'Han', 'Lando')
    'Lando'
    """
    if cards == 0:
        return player0
    if cards < 2:
        return player1
    take_one = sabacc_winner(cards - 1, player1, player0)
    take_two = sabacc_winner(cards - 2, player1, player0)
    if take_one == player0 or take_two == player0:
        return player0
    return player1


def thanos_messenger(word):
    """
    >>> thanos_messenger("I")("don't")("feel")("so")("good")(".")
    'I feel good.'
    >>> thanos_messenger("Thanos")("always")("kills")("half")(".")
    'Thanos kills.'
    """

    def make_new_messenger(message, skip_next):
        def new_messenger(word):
            if word == ".":
                return message + word
            if skip_next:
                return make_new_messenger(message, not skip_next)
            return make_new_messenger(message + ' ' + word, not skip_next)
        return new_messenger
    return make_new_messenger(word, True)


def tree(label, branches=[]):
    return [label] + list(branches)

def is_leaf(t):
    return not branches(t)

def label(t):
    return t[0]

def branches(t):
    return t[1:]

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def factor_tree(n):
    for i in range(n//2, 2, -1):
        if n % i == 0:
            return tree(n, sum([[factor_tree(i), factor_tree(y)] for y in range(n//2) if i*y == n], []))
    return tree(n)

print_tree(factor_tree(2))
print_tree(factor_tree(6))
print_tree(factor_tree(12))
