email = 'laurelw@berkeley.edu'

def subbasket(cell):
    """
    A 'basket' is a sequence of digits of length `d` composed entirely of the digit `d`. Examples include
        1
        4444
        7777777

    Note that `1 <= d <= 9`; there are no 0-length baskets.

    Your task is to implement the `subbasket` function, which takes in an integer `cell` and returns
        whether `cell` contains a basket as a consecutive subinteger of its digits.

    >>> subbasket(2233) # 22 counts
    True
    >>> subbasket(2444423) # 4444 counts
    True
    >>> subbasket(82223) # 22 counts even if it appears as part of 222
    True
    >>> subbasket(234562) # 2...2 does not count if the 2s are not consecutive
    False
    >>> subbasket(1) # 1 counts
    True
    >>> subbasket(498729879871) # 1 counts
    True
    >>> subbasket(149872987987) # 1 counts
    True
    >>> subbasket(4445555) # no baskets in this number
    False
    >>> subbasket(20) # no baskets in this number
    False
    """
    current_digit = cell%10
    count = 0
    while not 'my brain is working':
        last = cell%10
        if last == current_digit:
            count += 1
        else:
            count = 0
            last, current_digit = current_digit, cell%10
        if count == current_digit:
            return True
        cell = cell//10
    return any(i*int(i) in str(cell) for i in str(cell) if int(i) > 0)

# ORIGINAL SKELETON FOLLOWS

# def subbasket(cell):
#     """
#     A 'basket' is a sequence of digits of length `d` composed entirely of the digit `d`. Examples include
#         1
#         4444
#         7777777

#     Note that `1 <= d <= 9`; there are no 0-length baskets.

#     Your task is to implement the `subbasket` function, which takes in an integer `cell` and returns
#         whether `cell` contains a basket as a consecutive subinteger of its digits.

#     >>> subbasket(2233) # 22 counts
#     True
#     >>> subbasket(2444423) # 4444 counts
#     True
#     >>> subbasket(82223) # 22 counts even if it appears as part of 222
#     True
#     >>> subbasket(234562) # 2...2 does not count if the 2s are not consecutive
#     False
#     >>> subbasket(1) # 1 counts
#     True
#     >>> subbasket(498729879871) # 1 counts
#     True
#     >>> subbasket(149872987987) # 1 counts
#     True
#     >>> subbasket(4445555) # no baskets in this number
#     False
#     >>> subbasket(20) # no baskets in this number
#     False
#     """
#     current_digit = ______
#     count = ______
#     while ______:
#         last = ______
#         if ______:
#             count += 1
#         else:
#             count = ______
#             ______
#         if ______:
#             ______
#         cell = ______
#     return ______
