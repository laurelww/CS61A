email = 'laurelw@berkeley.edu'

def elevator(office, drawer):
    """
    Write a function `elevator` that takes in two lists.
        `office` is a list of strings
        `drawer` is a list of integers

    It returns a new list where every element from `office` is copied the
    number of times as the corresponding element in `drawer`. If the number
    of times to be copied is negative (-k), then it removes the previous
    k elements added.

    Note 1: `office` and `drawer` do not have to be the same length, simply ignore
    any extra elements in the longer list.

    Note 2: you can assume that you will never be asked to delete more
    elements than exist


    >>> elevator(['a', 'b', 'c'], [1, 2, 3])
    ['a', 'b', 'b', 'c', 'c', 'c']
    >>> elevator(['a', 'b', 'c'], [3])
    ['a', 'a', 'a']
    >>> elevator(['a', 'b', 'c'], [0, 2, 0])
    ['b', 'b']
    >>> elevator([], [1,2,3])
    []
    >>> elevator(['a', 'b', 'c'], [1, -1, 3])
    ['c', 'c', 'c']
    """
    def elevator_helper(office, drawer, product):
        if not office or not drawer:
            return product
        if drawer[0] >= 0:
            product = product + [office[0]]*drawer[0]
        else:
            product = product[:len(product)+drawer[0]]
        return elevator_helper(office[1:], drawer[1:], product)
    return elevator_helper(office, drawer, [])

# ORIGINAL SKELETON FOLLOWS

# def elevator(office, drawer):
#     """
#     Write a function `elevator` that takes in two lists.
#         `office` is a list of strings
#         `drawer` is a list of integers

#     It returns a new list where every element from `office` is copied the
#     number of times as the corresponding element in `drawer`. If the number
#     of times to be copied is negative (-k), then it removes the previous
#     k elements added.

#     Note 1: `office` and `drawer` do not have to be the same length, simply ignore
#     any extra elements in the longer list.

#     Note 2: you can assume that you will never be asked to delete more
#     elements than exist


#     >>> elevator(['a', 'b', 'c'], [1, 2, 3])
#     ['a', 'b', 'b', 'c', 'c', 'c']
#     >>> elevator(['a', 'b', 'c'], [3])
#     ['a', 'a', 'a']
#     >>> elevator(['a', 'b', 'c'], [0, 2, 0])
#     ['b', 'b']
#     >>> elevator([], [1,2,3])
#     []
#     >>> elevator(['a', 'b', 'c'], [1, -1, 3])
#     ['c', 'c', 'c']
#     """
#     def elevator_helper(______, ______, ______):
#         if ______:
#             return ______
#         if ______:
#             ______ = ______
#         else:
#             ______ = ______[:______]
#         return ______
#     return ______
