# def num_eights(x):
#     if x == 0:
#         return False
#     if x % 10 == 8:
#         return 1 + num_eights(x // 10)
#     return num_eights(x // 10)
# (lambda __g: [None for __g['num_eights'], num_eights.__name__ in [(lambda x: (lambda __l: [(lambda __after: False if (__l['x'] == 0) else __after())(lambda: (lambda __after: (1 + num_eights((__l['x'] // 10))) if ((__l['x'] % 10) == 8) else __after())(lambda: num_eights((__l['x'] // 10)))) for __l['x'] in [(x)]][0])({}), 'num_eights')]][0])(globals())

def list_change(n, denoms):
    """
    >>> for x in list_change(10, [25, 10, 5, 1]):
    ...    print(x)
    [10]
    [5, 5]
    [5, 1, 1, 1, 1, 1]
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    def helper(n, denoms, change):
        if sum(change) == n:
            return [change]
        if not denoms:
            return []
        if sum(denoms[:1]) > n:
            denoms = denoms[1:]
        with_first = helper(n, denoms, change + denoms[:1])
        without_first = helper(n, denoms[1:], change)
        return with_first + without_first
    return helper(n, denoms, [])
