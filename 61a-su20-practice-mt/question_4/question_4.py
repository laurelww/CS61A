
def sums(n, k):
    """
    Implement sums, which takes two positive integers n and k. It returns a list of lists containing all
    the ways that a list of k positive integers can sum to n. Results can appear in any order.

    Return the ways in which K positive integers can sum to N.
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
        return [[1 for _ in range(n)]]
    y = []
    for x in range(1, n+1):
        y.extend([s + [x] for s in sums(n-x, k-1)])
    return y

    curr_sum_call = f"sum({n}, {k})"
    print(f"> --- New call {curr_sum_call} ---")
    if k == n:
        print(f"> Returned base case {[[1 for _ in range(n)]]} when k=n={k}")
        return [[1 for _ in range(n)]]
    y = []
    for x in range(1, n+1):
        for s in sums(n-x, k-1):
            old_y = y[:]
            y.extend([s + [x]])
            print(f"> x={x} and s={s} in sumcall {curr_sum_call}")
            print(f"> Cat [s + x] to get new sumlist {[s + [x]]}")
            print(f"> Extended y={old_y} by {[s + [x]]} to get y={y}")
            print()
            print()
        # y.extend([s + [x] for s in sums(n-x, k-1)])
    return y


# ORIGINAL SKELETON FOLLOWS

# def sums(n, k):
#     """
#     Implement sums, which takes two positive integers n and k. It returns a list of lists containing all
#     the ways that a list of k positive integers can sum to n. Results can appear in any order.

#     Return the ways in which K positive integers can sum to N.
#     >>> sums(2, 2)
#     [[1, 1]]
#     >>> sums(2, 3)
#     []
#     >>> sums(4, 2)
#     [[3, 1], [2, 2], [1, 3]]
#     >>> sums(5, 3)
#     [[3, 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
#     """
#     if ______:
#         return ______
#     y = []
#     for x in ______:
#         y.extend([______ for s in sums(______)])
#     return y
