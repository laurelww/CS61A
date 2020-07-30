"""
Linked Lists

"""

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


def add(s, v):
    """
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    # curr_node = s
    # smaller_than = None
    # larger_than = None
    #
    # while curr_node:
    #
    #     if curr_node.first < v:
    #         smaller_than = curr_node
    #     elif curr_node.first > v:
    #         larger_than = v
    #     elif curr_node.first == v:
    #         return s
    #
    #     curr_node = curr_node.rest
    #
    # if smaller_than is not None:
    #     smaller_than = Link(smaller_than.first, [v, smaller_than.rest])
    # elif larger_than is not None:
    #     larger_than = Link(v, [larger_than])
    #
    # return s
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        return add(s.rest, v)
    return s


"""
Tree Class

"""


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


def fib_tree(n):
    """A Fibonacci tree."""
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])


def leaves(t):
    """Return a list of leaf labels in Tree T."""
    assert isinstance(t, Tree)
    if t.is_leaf():
        return [t.label]
    return sum([leaves(b) for b in t.branches], [])

def height(t):
    """Return the number of transitions in the longest path in T."""
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])


"""
Pruning trees
"""

def prune(t, n):
    """Prune al sub-trees whose label is n."""
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)

"""
When I got into this class I had no clue
about ED or what would python do,
then we were learning recursion by week 2
guess that's what I get from summer school

John DeNero
Kavi Chae and Ryan are the student teachers
not even gonna lie I love these python features
even if recursion makes me change my major...

John DeNero
Students on piazza giving helpful feedback
I be in that office hour learning SQL
I should probably be grinding for my final...



When I got into this class
I did not expect
To not have a clue


"""