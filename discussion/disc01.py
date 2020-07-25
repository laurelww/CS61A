# disc01

def wears_jacket_with(temp, raining):
    return temp < 60 or raining

# 1.2
"""
Runtime error, loops forever
"""

#1.3

def find_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

# 2.1

"""
GLOBAL FRAME:
    x = 2

    y = 2

    x = 4
"""

# 2.2
"""
a. func double(x) [p = Global]

b. func triple(x) [p = Global]

GLOBAL FRAME:
    double --> a.
    triple --> b.
    hat --> a.
    double --> b.
"""

# 2.3
a. double(x) [p = Global]

"""
GLOBAL FRAME:
    double --> a.
    hmm --> a.
    f1 (from wow)   
    double [p = Global]
        x [3
        return value [6
    wow = 6
    f2 (from hmm(wow)
    hmm(wow
    hmm(wow) = 12

"""

# 2.4
"""
a. func

GLOBAL FRAME

"""
