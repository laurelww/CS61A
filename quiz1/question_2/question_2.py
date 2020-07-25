email = 'laurelw@berkeley.edu'

def falconer(ruler, k):
    """
    Given a number `ruler`, finds the largest number of length `k` or fewer,
    composed of digits from `ruler`, in order.

    >>> falconer(1234, 1)
    4
    >>> falconer(32749, 2)
    79
    >>> falconer(1917, 2)
    97
    >>> falconer(32749, 18)
    32749
    """
    if ruler // 10 == 0:
        return ruler
    a = ruler % 10 * 10 ** k
    b = ruler // 10
    return falconer()

# ORIGINAL SKELETON FOLLOWS

# def falconer(ruler, k):
#     """
#     Given a number `ruler`, finds the largest number of length `k` or fewer,
#     composed of digits from `ruler`, in order.

#     >>> falconer(1234, 1)
#     4
#     >>> falconer(32749, 2)
#     79
#     >>> falconer(1917, 2)
#     97
#     >>> falconer(32749, 18)
#     32749
#     """
#     if ______:
#         return ______
#     a = ______
#     b = ______
#     return ______
