"""
CS61A Study Group Pset #07

7/30/2020

SEE BOTTOM FOR DOCTEST INSTRUCTIONS
"""



"""
OOP

Implement CreditCard, a class whose methods are described below.
"""
class CreditCard:
    """A CreditCard.

    >>> c = CreditCard(50)
    >>> c.purchase(5)      # 45 remaining
    45
    >>> c.purchase(30)     # now only 15 remaining
    15
    >>> c.purchase(30)
    'declined'
    >>> c.pay_bill()       # current balance is 35
    35
    >>> c.purchase(30)     # 20 remaining
    20
    >>> [CreditCard(10), CreditCard(20, 5)]
    [CreditCard(10, 0), CreditCard(20, 5)]

    >>> d = CreditCard(100)
    >>> d.purchase(10)
    90
    >>> d.purchase(60)
    30
    >>> d.purchase(60)
    'declined'
    >>> d.pay_bill()
    70
    >>> d.purchase(60)
    40
    """

    def __init__(self, maximum, balance=0):
        """A CreditCard is constructed from a maximum and an optional balance,
        which defaults to 0. The maximum represents the greatest value that
        balance is allowed to take after a purchase.
        """
        assert balance <= maximum
        self.maximum = maximum
        self.balance = balance

    def purchase(self, price):
        """When the CreditCard is used to make a purchase, the purchase price
        is added to the balance unless the purchase is declined. A purchase is
        declined if the result of adding the price to the current balance would
        exceed the maximum. If the purchase is not declined, return the highest
        price of the next purchase that would not be declined.
        """
        assert price > 0
        if ______:
            return 'declined'
        ______
        return ______

    def pay_bill(self):
        """Reduce the balance to 0 and return the value of the balance before
        it was reset to 0.
        """
        ______
        ______
        return ______

    def __repr__(self):
        return 'CreditCard(' + repr(self.maximum) + ', ' + repr(self.balance) + ')'


# Original skeleton
# class CreditCard:
#     """A CreditCard.
#
#     >>> c = CreditCard(50)
#     >>> c.purchase(5)      # 45 remaining
#     45
#     >>> c.purchase(30)     # now only 15 remaining
#     15
#     >>> c.purchase(30)
#     'declined'
#     >>> c.pay_bill()       # current balance is 35
#     35
#     >>> c.purchase(30)     # 20 remaining
#     20
#     >>> [CreditCard(10), CreditCard(20, 5)]
#     [CreditCard(10, 0), CreditCard(20, 5)]
#
#     >>> d = CreditCard(100)
#     >>> d.purchase(10)
#     90
#     >>> d.purchase(60)
#     30
#     >>> d.purchase(60)
#     'declined'
#     >>> d.pay_bill()
#     70
#     >>> d.purchase(60)
#     40
#     """
#
#     def __init__(self, maximum, balance=0):
#         """A CreditCard is constructed from a maximum and an optional balance,
#         which defaults to 0. The maximum represents the greatest value that
#         balance is allowed to take after a purchase.
#         """
#         assert balance <= maximum
#         self.maximum = maximum
#         self.balance = balance
#
#     def purchase(self, price):
#         """When the CreditCard is used to make a purchase, the purchase price
#         is added to the balance unless the purchase is declined. A purchase is
#         declined if the result of adding the price to the current balance would
#         exceed the maximum. If the purchase is not declined, return the highest
#         price of the next purchase that would not be declined.
#         """
#         assert price > 0
#         if ______:
#             return 'declined'
#         ______
#         return ______
#
#     def pay_bill(self):
#         """Reduce the balance to 0 and return the value of the balance before
#         it was reset to 0.
#         """
#         ______
#         ______
#         return ______
#
#     def __repr__(self):
#         return 'CreditCard(' + repr(self.maximum) + ', ' + repr(self.balance) + ')'


"""
LISTS

This question involves plucking the leaves off a tree one by one.

Definitions:

1) A "number tree" is a Tree whose labels are _unique_ positive integers.
   No repeated labels appear in a number tree.

2) A "plucking order" for a number tree t is a sequence of unique positive
   integers that are all labels of t.

3) A plucking order is "valid" if both of these conditions are true:
   (a) the plucking order contains all labels of t, and
   (b) in the plucking order, the label for each node of t appears after
       the labels of all its descendant nodes. Thus, leaves appear first.

Note: redwood, pine, and cyprus are all kinds of trees.


Implement order, which takes a number tree called redwood. It returns
a valid plucking order as a list of numbers. If there is more than one valid
plucking order for redwood, your order function can return any one of them.

IMPORTANT: You do not need to return EVERY valid plucking order; just one.
"""
def order(redwood):
    """Return a list containing a valid plucking order for the labels of t.

    >>> order(Tree(1, [Tree(2, [Tree(3, [Tree(4)])])]))               # The only valid plucking order.
    [4, 3, 2, 1]
    >>> order(Tree(1, [Tree(2), Tree(3)])) in [[2, 3, 1], [3, 2, 1]]  # There are 2 valid orders.
    True
    >>> o = order(Tree(1, [Tree(2, [Tree(3)]), Tree(4, [Tree(5)])]))  # There are many valid orders,
    >>> o.index(5) < o.index(4)                                       # but all have 5 before 4,
    True
    >>> o.index(3) < o.index(2)                                       # and 3 before 2,
    True
    >>> o[4:]                                                         # and 1 at the end.
    [1]

    >>> order(Tree(7, [Tree(4, [Tree(6)]), Tree(5)])) in [[6, 5, 4, 7], [5, 6, 4, 7], [6, 4, 5, 7]]
    True
    """
    plucking_order = []
    for b in ______:
        ______
    return plucking_order + [redwood.label]


# Original skeleton
# def order(redwood):
#     """Return a list containing a valid plucking order for the labels of t.
#
#     >>> order(Tree(1, [Tree(2, [Tree(3, [Tree(4)])])]))               # The only valid plucking order.
#     [4, 3, 2, 1]
#     >>> order(Tree(1, [Tree(2), Tree(3)])) in [[2, 3, 1], [3, 2, 1]]  # There are 2 valid orders.
#     True
#     >>> o = order(Tree(1, [Tree(2, [Tree(3)]), Tree(4, [Tree(5)])]))  # There are many valid orders,
#     >>> o.index(5) < o.index(4)                                       # but all have 5 before 4,
#     True
#     >>> o.index(3) < o.index(2)                                       # and 3 before 2,
#     True
#     >>> o[4:]                                                         # and 1 at the end.
#     [1]
#
#     >>> order(Tree(7, [Tree(4, [Tree(6)]), Tree(5)])) in [[6, 5, 4, 7], [5, 6, 4, 7], [6, 4, 5, 7]]
#     True
#     """
#     plucking_order = []
#     for b in ______:
#         ______
#     return plucking_order + [redwood.label]


# Tree class
class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches




"""
CONTROL

Implement compose, which takes a positive integer n. It returns a function that, 
when called repeatedly on n one-argument functions f1, f2, . . . , fn, returns a 
one-argument function of x that returns f1 (f2 (. . . fn (x) . . . )). 
"""
def compose(n):
    """Return a function that, when called n times repeatedly
    on unary functions f1, f2, ..., fn, returns a function g(x)
    equivalent to f1(f2( ... fn(x) ... )).
    >>> add1 = lambda y: y + 1
    >>> compose(3)(abs)(add1)(add1)(-4) # abs(add1(add1(-4)))
    2
    >>> compose(3)(add1)(add1)(abs)(-4) # add1(add1(abs(-4)))
    6
    >>> compose(1)(abs)(-4)
    4
    """
    assert n > 0
    if n == 1:
        return ____________________
    def call(f):
        def on(g):
            return ____________________(____________________)
        return on
    return call

# Original skeleton
# def compose(n):
#     """Return a function that, when called n times repeatedly
#     on unary functions f1, f2, ..., fn, returns a function g(x)
#     equivalent to f1(f2( ... fn(x) ... )).
#     >>> add1 = lambda y: y + 1
#     >>> compose(3)(abs)(add1)(add1)(-4) # abs(add1(add1(-4)))
#     2
#     >>> compose(3)(add1)(add1)(abs)(-4) # add1(add1(abs(-4)))
#     6
#     >>> compose(1)(abs)(-4)
#     4
#     """
#     assert n > 0
#     if n == 1:
#         return ____________________
#     def call(f):
#         def on(g):
#             return ____________________(____________________)
#         return on
#     return call



"""
LAMBDAS

Complete the final expression below with only integers and names so it evaluates to 2020.
"""
from operator import add
c = lambda f: lambda x: lambda y: f(x, y)
twice = lambda z: 2 * z

compose(___________)(twice)(___________(___________)(10))(___________(pow)(10))(___________)


# Original skeleton
# from operator import add
# c = lambda f: lambda x: lambda y: f(x, y)
# twice = lambda z: 2 * z
#
# compose(___________)(twice)(___________(___________)(10))(___________(pow)(10))(___________)