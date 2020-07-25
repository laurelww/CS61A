"""
CS61A Study Group Pset #03

7/24/2020

SEE BOTTOM FOR DOCTEST INSTRUCTIONS
"""



"""
ITERATORS AND GENERATORS

Implement rev, a generator function that takes a Link instance and yields the elements of that linked
list in reverse order.

See below for Linked List class.
"""

def rev(s):
    """Yield the elements in Link instance s in reverse order.
         >>> list(rev(Link(1, Link(2, Link(3)))))
         [3, 2, 1]
         >>> next(rev(Link(2, Link(3))))
         3
    """
    if ____________________:
        ____________________
    yield ____________________

# Original skeleton
# def rev(s):
#     """Yield the elements in Link instance s in reverse order.
#          >>> list(rev(Link(1, Link(2, Link(3)))))
#          [3, 2, 1]
#          >>> next(rev(Link(2, Link(3))))
#          3
#     """
#     if ____________________:
#         ____________________
#     yield ____________________

# Linked List class as seen in lecture
class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link) # also True is rest is an instc of a subclass of Link
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = f", {repr(self.rest)}"
        else:
            rest_str = ''
        return f"Link({self.first}{rest_str})"

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value




"""
Tree Recursion

A rook is a piece in the game of chess that can move any number of squares
vertically or horizontally. We put a rook somewhere on integer coordinates
in the first quadrant (0 <= x <= inf, 0 <= y <= inf) and put a spell on it 
so that it can only move toward the origin (i.e., either down or left).

Complete the function paths2D(x, y) to calculate how many different paths 
there are to get home at (0, 0) given a starting point (x, y). E.g, the 
rook at (3, 2) could get back to (0, 0) any one of 10 ways, and the number 
of paths for each starting square in  (0 <= x <= 3, 0 <= y <= 2) is shown 
below.

Some example paths a rook can take from (2, 3) to (0, 0) are marked by dots.

2  | | |R            2 .|.|.|R        2  | |.|R
  -+-+-+-              -+-+-+-          -+-+-+-
1  | | |  has paths  1 .| | |    or   1 .|.|.|  or ...
  -+-+-+-              -+-+-+-          -+-+-+-
0  | | |             0 .| | |         0 .| | |
  0 1 2 3              0 1 2 3          0 1 2 3
  
Overall, the number of times 
each square is traveled on 
over *all possible paths*:

2 1|3|6|10
  -+-+-+-
1 1|2|3|4
  -+-+-+-
0 1|1|1|1
  0 1 2 3 

"""

def paths2D(x, y):
    """
    >>> paths(3, 2)
    10
    """
    if ____________________:
        return ____________________
    else:
        return ____________________

# Original skeleton
# def paths2D(x, y):
#     """
#     >>> paths(3, 2)
#     10
#     """
#     if ____________________:
#         return ____________________
#     else:
#         return ____________________



"""
Trees

Fill in the function prune below so that given a Tree with integer labels, 
it (destructively) deletes all nodes whose label is strictly less than that 
of their parent if their parent is at even depth, or whose label is strictly 
greater that that of their parent if their parent is at odd depth. Deleting a 
node deletes the entire subtree below it. The root of the entire tree is at 
depth 0. For example, given the tree on the left, your function should produce 
the tree on the right without creating any new Tree nodes. The function prune 
does not return a value.

     5              5
   / | \            /\ 
  3  9  7    -->   9  7
 /\    /|\            /\
2  4  6 1 8          6  1

"""

def prune(t):
    """
    >>> t = Tree(5, [Tree(2, [Tree(2), Tree(4)]), Tree(9), Tree(7, [Tree(6), Tree(1), Tree(8)])])
    >>> prune(t)
    >>> print(t)
    5
      9
      7
        6
        1
    """
    def prune_level(t, d):
        if ____________________:
            t.branches = ____________________
        else:
            t.branches = ____________________
        for ____________________:
            ____________________
    prune_level(t, 0)

# Original skeleton
# def prune(t):
#     def prune_level(t, d):
#         if ____________________:
#             t.branches = ____________________
#         else:
#             t.branches = ____________________
#         for ____________________:
#             ____________________
#     prune_level(t, 0)

# Tree class as seen in lecture
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = f", {repr(self.branches)}"
        else:
            branch_str = ''
        return f"Tree({repr(self.label)}{branch_str}"

    def __str__(self):
        return "\n".join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append(f"  {line}")
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches



if __name__ == '__main__':
    import doctest

    # uncomment to test all funcs
    doctest.testmod()

    # run doctests for a specific function by replacing func_name with the name of the func you want to test
    # doctest.run_docstring_examples(func_name, globals(), verbose=True)