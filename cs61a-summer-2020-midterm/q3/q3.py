email = 'laurelw@berkeley.edu'

def tape(password, limit):
    """ Write a higher-order function `tape` that returns a one-argument
    function `attempt`. Every time `attempt` is called, it checks to see if its argument
    matches the password at the corresponding index.

    If the password entirely matches, return a success string. If more than `limit`
    number of incorrect hacks are attempted, you should return an error string.
    For details, see the doctest.


    Note: to comment out a blank that covers an entire line, just put down 'unnecessary' (with quotes)

    >>> hacker = tape([1,2], 2)
    >>> hacker(1)
    >>> hacker(2)
    'Successfully unlocked!'
    >>> hacker = tape([1,2], 1)
    >>> hacker(1)
    >>> hacker(3) # used up attempts to gain access
    >>> hacker(2) # correct attempt to gain access, but already locked
    'Security has been notified!'
    >>> hacker = tape([1,2], 2)
    >>> hacker(1)
    >>> hacker(3) # 1 attempt left to gain access
    >>> hacker(2) # correct attempt to gain access
    'Successfully unlocked!'
    """
    password = password
    limit = limit
    def attempt(digit):
        nonlocal password
        nonlocal limit
        if [digit] == password and limit > 0:
            return 'Successfully unlocked!'
        if digit != password[0] or limit <= 0:
            limit = limit - 1
            if limit < 0:
                return 'Security has been notified!'
        else:
            password = password[1:]
    return attempt

# ORIGINAL SKELETON FOLLOWS

# def tape(password, limit):
#     """ Write a higher-order function `tape` that returns a one-argument
#     function `attempt`. Every time `attempt` is called, it checks to see if its argument
#     matches the password at the corresponding index.

#     If the password entirely matches, return a success string. If more than `limit`
#     number of incorrect hacks are attempted, you should return an error string.
#     For details, see the doctest.


#     Note: to comment out a blank that covers an entire line, just put down 'unnecessary' (with quotes)

#     >>> hacker = tape([1,2], 2)
#     >>> hacker(1)
#     >>> hacker(2)
#     'Successfully unlocked!'
#     >>> hacker = tape([1,2], 1)
#     >>> hacker(1)
#     >>> hacker(3) # used up attempts to gain access
#     >>> hacker(2) # correct attempt to gain access, but already locked
#     'Security has been notified!'
#     >>> hacker = tape([1,2], 2)
#     >>> hacker(1)
#     >>> hacker(3) # 1 attempt left to gain access
#     >>> hacker(2) # correct attempt to gain access
#     'Successfully unlocked!'
#     """
#     ______
#     ______
#     def attempt(digit):
#         ______
#         ______
#         if ______:
#             return ______
#         if ______:
#             ______
#             if ______:
#                 return ______
#         else:
#             ______
#     return ______
