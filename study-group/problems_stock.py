"""
LISTS - Fall 2016 Final: Q4(a)

A flat list is a list containing integers and None that describes a
binary tree of integers. The root is element 0. The left branch of
element i is element 2∗i+1 and the right is 2∗i+2. The None value is
used to indicate an empty tree, such as an empty left branch when the
corresponding right branch is not empty. None values at the end of a
flat list can be omitted. Four examples of trees and the flat lists
that describe them appear below.

  3                 |  3                    |   3         [3, 1]    |
 / \  --> [3, 1, 4] |   \  --> [3, None, 4] |  /   -->      OR      |
1   4               |    4                  | 1        [3, 1, None] |

     6
    / \          [6, 3, 8, 1, None, 7]
   3   8  -->              OR
  /   /        [6, 3, 8, 1, None, 7, None]
 1   7


Implement grow, which takes a flat list s of integer node values (which
may also contain None, as described above) and an index i that is 0 by
default. When i is 0, grow returns a BTree instance described by s. The
BTree class appears in the left column of page 2 of the midterm 2 study guide.
"""