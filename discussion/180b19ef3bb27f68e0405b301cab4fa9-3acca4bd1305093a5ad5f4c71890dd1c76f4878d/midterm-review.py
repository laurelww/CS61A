import doctest
import sys
import argparse

"""
---USAGE---

python3 midterm-review.py <name_of_function>
e.g python3 midterm-review.py make_alternator

---NOTES---

- if you pass all the doctests, you will get no terminal output
    - if you want to see the verbose output (all output shown even if the function is correct), run this:
    python3 midterm-review.py <name_of_function> -v
- if you want to test all of your functions, run this:
    python3 midterm-review.py all
"""

### Midterm Review Session ###

# make_interval = lambda low, up: lambda x: low <= x <= up

################
###   HoFs   ###
################

def make_alternator(f, g):
    """
    >>> a = make_alternator(lambda x: x * x, lambda x: x + 4)
    >>> a(5)
    1
    6
    9
    8
    25
    >>> b = make_alternator(lambda x: x * 2, lambda x: x + 2)
    >>> b(4)
    2
    4
    6
    6
    """
    def alternate(x):
        for i in range(1, x+1):
            if i % 2 == 0:
                print(g(i))
            else:
                print(f(i))

    return alternate
    
    
    
def print_sum(a):
    """ 
    >>> f = print_sum(1)
    >>> g = f(2) # 1 * 2 => 1 + 2
    3
    >>> h = g(4) # (1 + 2) * 4 => 1 + 2 + ... + 11 + 12
    78
    >>> i = h(5) # (3 + 4) * 5 => 1 + 2 + ... + 34 + 35
    630
    """
    def helper(b):
        i, total = 1, 0
        while i <= a*b:
            # ______
            i, total = i + 1, total + i
        print(total)
        return print_sum(a + b)
    return helper
    
    
    
####################################
###   Recursion/Tree Recursion   ###
####################################

def ways(start, end, k, actions):
    """Return the number of ways of reaching end from start by taking up to k actions.

    >>> ways(-1, 1, 5, [abs, lambda x: x + 2])
    2
    >>> ways(1, 10, 5, [lambda x: x + 1, lambda x: x + 4])
    3
    >>> ways(1, 20, 5, [lambda x: x + 1, lambda x: x + 4])
    0
    >>> ways([3], [2, 3, 2, 3], 4, [lambda x: [2] + x, lambda x: 2 * x, lambda x: x[:-1]])
    3
    """  
    if start == end:
        return 1
    elif k == 0:
        return 0
    return sum([ways(f(start), end, k-1, actions) for f in actions])



##############################
###   Lists & Mutability   ###
##############################

def splice(a, b, k):
    """Return a list of the first k elements of a, then all of b, then the rest of a.
    
    >>> splice([2, 3, 4, 5], [6, 7], 2)
    [2, 3, 6, 7, 4, 5]
    """
    return ___________________________________________

def all_splice(a, b, c):
    """Return a list of all k such that splicing b into a at position k gives c.
    
    >>> all_splice([1, 2], [3, 4], [1, 3, 4, 2])
    [1]
    >>> all_splice([1, 2, 1, 2], [1, 2], [1, 2, 1, 2, 1, 2])
    [0, 2, 4]
    """
    return ___________________________________________



####################
###   Nonlocal   ###
####################

def quota(f, limit):
    values = []
    def limited(n):
        nonlocal limit
        y = f(n)
        count = len(values)
        values.append(y)
        if count < limit:
            return quota(f, limit)
        limit = limit - 1
        return 'Over quota! Limit is now' + limit
    return limited



#####################
###   ADT Trees   ###
#####################

def pile(t):
    """Return a dict that contains every path from a leaf to the root of tree t.
    
    >>> pile(tree(5, [tree(3, [tree(1), tree(2)]), tree(6, [tree(7)])]))
    {1: (3, (5, ())), 2: (3, (5, ())), 7: (6, (5, ()))}
    """
    p = {}
    def gather(u, path):
        if is_leaf(u):
            p[label(u)] = path
        for b in branches(u):
            gather(b, (label(u), path))
    gather(t, ())
    return p



def count_ways(t, total):
    """ Return the number of ways that any sequence of consecutive nodes in a root-to-leaf path can sum to total.
    
    >>> t1 = tree(5, [tree(1, [tree(2, [tree(1)]), tree(1, [tree(4, [tree(2, [tree(2)])])])]), tree(3, [tree(2, [tree(2), tree(3)])]), tree(3, [tree(1, [tree(3)])])])
    >>> count_ways(t1, 7)
    4
    >>> t2 = tree(2, [tree(-10, [tree(12)]), tree(1, [tree(1), tree(-1, [tree(2)])])])
    >>> count_ways(t2, 2)
    6
    """
    def paths(t, total, can_skip):
        ways = 0 
        if total == label(t):
            ways += 1
        ways += sum([paths(b, total-label(t), False) for b in branches(t)], [])
        if can_skip:
            ways += sum([paths(b, total, True) for b in branches(t)], [])
        return ways
    return paths(t, total, True)





# Tree ADT

# Constructor
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selector
def label(tree):
    """Return the label value of a tree."""
    return tree[0]

# Selector
def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

# For convenience
def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise."""
    return not branches(tree)



### For running tests only. Not part of discussion content ###

parser = argparse.ArgumentParser(description="Test your work")
parser.add_argument("func", metavar="function_to_test", help="Function to be tested")
parser.add_argument("-v", dest="v", action="store_const", const=True, default=False, help="Verbose output")
args = parser.parse_args()
try:
    if args.func == "all":
        if args.v:
            doctest.testmod(verbose=True)
        else:
            doctest.testmod()
    else:
        if args.v:
            doctest.run_docstring_examples(globals()[args.func], globals(), verbose=True, name=args.func)
        else:
            doctest.run_docstring_examples(globals()[args.func], globals(), name=args.func)
except:
    sys.exit("Invalid Arguments")