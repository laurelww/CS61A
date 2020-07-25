"""
CS61A Study Group Pset #04

7/25/2020

SEE BOTTOM FOR DOCTEST INSTRUCTIONS
"""


"""
DATA ABSTRACTION

Given the following class definitions, check whether each 
line of code results in an error (ERROR), data abstraction 
violation (DAV), or is otherwise correct (OK).

I will give out the solutions on Monday!

Example:
>>> print("EE/CS 2024 server best server")
OK

>>> "s" + 3
ERROR
"""

"""
>>> t = Tree(3, [Tree(1), Tree(2)])
'YOUR ANSWER HERE'
    
>>> L = [tree(1)]
'YOUR ANSWER HERE'
    
>>> L.append(tree(2))
'YOUR ANSWER HERE'
    
>>> s = tree(3, L)
'YOUR ANSWER HERE'
    
>>> s
'YOUR ANSWER HERE'
    
>>> print(s)
'YOUR ANSWER HERE'
    
>>> t
'YOUR ANSWER HERE'
    
>>> t.label
'YOUR ANSWER HERE'
    
>>> print(t)
'YOUR ANSWER HERE'
    
>>> label(s)
'YOUR ANSWER HERE'
    
>>> t.label = 4
'YOUR ANSWER HERE'
    
>>> label(s) = 4
'YOUR ANSWER HERE'
    
>>> s[0] = 5
'YOUR ANSWER HERE'
    
>>> print_tree_adt([5])
'YOUR ANSWER HERE'
    
>>> print_tree_adt(s)
'YOUR ANSWER HERE'
    
>>> t.branches[0].label = s
'YOUR ANSWER HERE'
    
>>> print_tree_adt(t.branches[0])
'YOUR ANSWER HERE'
    
>>> print_tree_adt(t.branches[0].label)
'YOUR ANSWER HERE'
    
>>> t
'YOUR ANSWER HERE'
    
>>> print(t)
'YOUR ANSWER HERE'
"""


# Tree ADT
def tree(label, branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def print_tree_adt(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree_adt(b, indent + 1)

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k=0):
        ind = []
        for b in self.branches:
            for line in b.indented(k + 1):
                ind.append('  ' + line)
            return [str(self.label)] + ind



"""
NONLOCAL

A runt node is a node in a tree whose label is smaller than all of the 
labels of its siblings. A sibling is another node that shares the same 
parent. A node with no siblings is a runt node.

Implement runts, which takes a Tree instance t in which every label is 
different and returns a list of the labels of all runt nodes in t, in 
any order. Also implement apply_to_nodes, which returns nothing and is 
part of the implementation. Do not mutate any tree. The Tree class given 
below.
"""

def runts(t):
    """Return a list in any order of the labels of all runt nodes in t.
    >>> sorted(runts(Tree(9, [Tree(3), Tree(4, [Tree(5, [Tree(6)]), Tree(7)]), Tree(2)])))
    [2, 5, 6, 9]
    """
    result = []
    def g(node):
        if ____________________:
            result.append(____________________)
    apply_to_nodes(____________________)
    return ____________________

def apply_to_nodes(f, t):
    """Apply a function f to each node in a Tree instance t."""
    ____________________
    for b in t.branches:
        ____________________


# Original skeleton
# def runts(t):
#     """Return a list in any order of the labels of all runt nodes in t.
#     >>> sorted(runts(Tree(9, [Tree(3), Tree(4, [Tree(5, [Tree(6)]), Tree(7)]), Tree(2)])))
#     [2, 5, 6, 9]
#     """
#     result = []
#     def g(node):
#         if ____________________:
#             result.append(____________________)
#     apply_to_nodes(____________________)
#     return ____________________
#
# def apply_to_nodes(f, t):
#     """Apply a function f to each node in a Tree instance t."""
#     ____________________
#     for b in t.branches:
#         ____________________

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
    # doctest.testmod()

    # run doctests for a specific function by replacing func_name with the name of the func you want to test
    doctest.run_docstring_examples(func_name, globals(), verbose=True)