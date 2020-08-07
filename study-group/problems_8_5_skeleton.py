"""
CS61A Study Group Pset #11

8/5/2020

SEE BOTTOM FOR DOCTEST INSTRUCTIONS
USE scheme.cs61a.org FOR SCHEME TESTING
"""



"""
SCHEME PART 1
25 min (all parts)

Implement repeater, which takes in a list of positive numbers and 
returns a list where every number in the original list except for 
the first number appears a number of times equivalent to the 
previous number.
"""
"""
;;; TESTS ARE BELOW THE SKELETON
;;; Copy your finished code into scheme.cs61a.org to run tests

; BEGIN PROBLEM
(define (repeater nums)
    (define (repeat nums n)
        (cond (____________________ ____________________) 
            ((= n 0) (repeater ) 
            (else ____________________)))
    (repeat ____________________ ____________________))
; END PROBLEM

;;; Tests
(repeater nil)
; expect ()
(repeater '(1 2 3))
; expect (2 3 3)
(repeater '(4 1 2 5))
; expect (1 1 1 1 2 5 5)
"""
# Original skeleton
# """
# ;;; TESTS ARE BELOW THE SKELETON
# ;;; Copy your finished code into scheme.cs61a.org to run tests
#
# ; BEGIN PROBLEM
# (define (repeater nums)
#     (define (repeat nums n)
#         (cond (____________________ ____________________)
#             ((= n 0) ____________________)
#             (else ____________________)))
#     (repeat ____________________ ____________________))
# ; END PROBLEM
#
# ;;; Tests
# (repeater nil)
# ; expect ()
# (repeater '(1 2 3))
# ; expect (2 3 3)
# (repeater '(4 1 2 5))
# ; expect (1 1 1 1 2 5 5)
# """
"""
SCHEME PART 2

Implement zip-tail, which is a tail recursive procedure that takes 
in two lists a and b and returns a single list containing two-element 
lists of co-indexed elements from a and b. If one list is shorter 
than the other, the zipped list’s length is that of the shorter list. 
Your solution should be tail recursive.

Hint: Use the built-in append procedure, which you can assume is tail 
recursive, to concatenate two lists together. For example:
    scm> (append '(1 2 3) '(4 5 6))
    (1 2 3 4 5 6)
"""
"""
;;; TESTS ARE BELOW THE SKELETON
;;; Copy your finished code into scheme.cs61a.org to run tests

; BEGIN PROBLEM
(define (zip-tail a b)
    (define (zipper a b result)
        (if (or (null? a) (null? b))
            result 
            (zipper (cdr a) (cdr b) (append result (cons a b)))))
    (zipper a b nil)
)
; END PROBLEM

;;; Tests
(zip-tail '(1 2 3) '(4 5 6))
;expect ((1 4) (2 5) (3 6))
(zip-tail '(c 6 a) '(s 1 ! hello world)) 
;expect ((c s) (6 1) (a !))
"""
# Original skeleton
# """
# ;;; TESTS ARE BELOW THE SKELETON
# ;;; Copy your finished code into scheme.cs61a.org to run tests
#
# ; BEGIN PROBLEM
# (define (zip-tail a b)
#     (define (zipper ____________________)
#         (if ____________________
#             ____________________
#             ____________________))
#     ____________________)
# ; END PROBLEM
#
# ;;; Tests
# (zip-tail '(1 2 3) '(4 5 6))
# ;expect ((1 4) (2 5) (3 6))
# (zip-tail '(c 6 a) '(s 1 ! hello world))
# ;expect ((c s) (6 1) (a !))
# """



"""
LINKED LISTS
15 min

Implement slice_reverse which takes a linked list s and mutatively reverses 
the elements on the interval, [i, j) (including i but excluding j). Assume s 
is zero-indexed, 0 < i < j, and that s has at least j elements.

You must use mutation; solutions which call the Link constructor will not 
receive credit. The Link class reference is provided below.
"""
def slice_reverse(s, i, j):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> slice_reverse(s, 1, 2)
    >>> s
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> slice_reverse(s, 2, 4)
    >>> s
    Link(1, Link(2, Link(4, Link(3, Link(5)))))
    """
    start = s
    for _ in range(i):
        start = s.rest
    reverse = Link.empty
    current = start
    for _ in range(j - i):
        start = start.rest
        current.rest = start.rest
        reverse = Link(current.first, reverse)
        current = current.rest
    # ____________________
    # ____________________
    # ____________________

# Original skeleton
# def slice_reverse(s, i, j):
#     """
#     >>> s = Link(1, Link(2, Link(3)))
#     >>> slice_reverse(s, 1, 2)
#     >>> s
#     Link(1, Link(2, Link(3)))
#     >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
#     >>> slice_reverse(s, 2, 4)
#     >>> s
#     Link(1, Link(2, Link(4, Link(3, Link(5)))))
#     """
#     start = ____________________
#     for ____________________:
#         start = ____________________
#     reverse = Link.empty
#     current = ____________________
#     for ____________________:
#         ____________________
#         current.rest = ____________________
#         reverse = ____________________
#         current = ____________________
#     ____________________
#     ____________________
#     ____________________

# Link class
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
HOF
15 min

Write a function, make_guess, which takes in a number that we want 
someone to try to guess, and returns a guessing function.

A guessing function is a one-argument function which takes in a number. 
If the number passed in is the number we wanted to guess, it will return 
the number of incorrect guesses made prior to the correct guess. 
Otherwise, it returns another guessing function, which keeps track of the
fact that we’ve made an incorrect guess.

Solutions which use lists, object mutation, nonlocal, or global will 
receive no credit.
"""
def make_guess(n):
    """
    >>> guesser = make_guess(10)
    >>> guess1 = guesser(6)
    >>> guess2 = guess1(7)
    >>> guess3 = guess2(8)
    >>> guess3(10)
    3
    >>> guess2(10)
    2
    >>> a = make_guess(5)(1)(2)(3)(4)(5)
    >>> a
    4
    """
    def update_guess(num_incorrect):
        def new_guess(x):
            if x == n:
                return num_incorrect
            else:
                return update_guess(num_incorrect + 1)
        return new_guess
    return update_guess(0)

# Original skeleton
# def make_guess(n):
#     """
#     >>> guesser = make_guess(10)
#     >>> guess1 = guesser(6)
#     >>> guess2 = guess1(7)
#     >>> guess3 = guess2(8)
#     >>> guess3(10)
#     3
#     >>> guess2(10)
#     2
#     >>> a = make_guess(5)(1)(2)(3)(4)(5)
#     >>> a
#     4
#     """
#     def update_guess(num_incorrect):
#         def new_guess(x):
#             if ____________________:
#                 ____________________
#             else:
#                 ____________________
#         ____________________
#     return ____________________



"""
RECURSION
15 min

Implement *-to-mul, which takes any expression e. It returns an expression 
like e, but with all calls to * replaced with calls to mul. Note that * 
takes an arbitrary number of arguments, while mul always takes exactly one 
argument: a list of numbers. You should account for this difference.
"""
"""
;;; TESTS ARE BELOW THE SKELETON
;;; Copy your finished code into scheme.cs61a.org to run tests

; BEGIN PROBLEM
(define (*-to-mul e)
    (if (not (list? e)) e
        (let ((op (car e)) (rest (*-to-mul (cdr e))))
            (if (equal? op '*)
                (list mul rest)
                (cons op rest)))))
; END PROBLEM
                            
;;; Tests
;; Convert all calls to * to calls to mul in expression e. 
(eval (*-to-mul '(* 1 (+ 2 3) (+ 4 5 (* 6 1)))))
; expect 75
"""
# Original skeleton
# """
# ;;; TESTS ARE BELOW THE SKELETON
# ;;; Copy your finished code into scheme.cs61a.org to run tests
#
# ; BEGIN PROBLEM
# (define (*-to-mul e)
#     (if (not (list? e))
#          e
#         (let ((op ____________________ ) (rest ____________________ ))
#             (if (equal? op '*)
#                 (list ____________________ )
#                 (cons op rest)))))
# ; END PROBLEM
#
# ;;; Tests
# ;; Convert all calls to * to calls to mul in expression e.
# (eval (*-to-mul '(* 1 (+ 2 3) (+ 4 5 (* 6 1)))))
# ; expect 75
# """



"""
MACROS PART 1
25 min (all parts)

In Python, we can do arithmetic using infix notation, where the operator 
goes between two operands, e.g. 3 + 4. In Scheme, we have to use prefix 
notation for all call expressions, e.g. (+ 3 4).

Let’s add support for infix notation in Scheme!

First, write the helper function skip, which skips the first n items in a 
list, returning the rest. For full credit, your solution must be tail recursive. 
You may assume that n is non-negative.
"""
"""
;;; TESTS ARE BELOW THE SKELETON
;;; Copy your finished code into scheme.cs61a.org to run tests

; BEGIN PROBLEM
(define (skip n lst)
(if (or (= n 0) (null? lst))
lst
(skip (- n 1) (cdr lst))))
; END PROBLEM

;;; Tests
(skip 2 '(1 2 3 4))
; expect (3 4)
(skip 10 '(1 2 3 4))
; expect ()
"""
# Original skeleton
# """
# ;;; TESTS ARE BELOW THE SKELETON
# ;;; Copy your finished code into scheme.cs61a.org to run tests
#
# ; BEGIN PROBLEM
# (define (skip n lst)
# (if ____________________
# ____________________
# ____________________))
# ; END PROBLEM
#
# ;;; Tests
# (skip 2 '(1 2 3 4))
# ; expect (3 4)
# (skip 10 '(1 2 3 4))
# ; expect ()
# """
"""
MACROS PART 2

Now let’s write infix, which takes in a list containing some arithmetic 
in infix notation and evaluates it. You only need to support addition 
and multiplication, but you do need to take the order of operations and 
parentheses into account. You may use skip, as well as cadr and caddr.
"""
"""
;;; TESTS ARE BELOW THE SKELETON
;;; Copy your finished code into scheme.cs61a.org to run tests
;       If you use skip, include that in your code.

(define (cadr lst) (car (cdr lst)))
(define (caddr lst) (cadr (cdr lst)))

; BEGIN PROBLEM
(define (infix expr)
    (cond
        ((not (pair? expr)) expr) ; a single value
        ((or (equal? (car expr) '*) (equal? (car expr) '+)) (eval expr)) ; already in prefix form
        ((null? (cdr expr)) nil)
        (else
            (define left (infix (car expr))
            (define right (infix (caddr expr)))
            (define operator (cadr expr))
        (cond
            ((equal? operator '+) (+ left right))
            ((equal? operator '*) (infix (cons operator
                                                (cons left right))))))))
; END PROBLEM

;;; Tests
(infix '(5))
; expect 5
(infix '(2 * 3))
; expect 6
(infix '(2 + 3))
; expect 5
(infix '(2 * (3 + 6)))
; expect 18
(infix '(2 * 3 + 6))
; expect 12
(infix '(2 + 3 * 6))
; expect 20
"""
# Original skeleton
# """
# ;;; TESTS ARE BELOW THE SKELETON
# ;;; Copy your finished code into scheme.cs61a.org to run tests
# ;       If you use skip, include that in your code.
#
# (define (cadr lst) (car (cdr lst)))
# (define (caddr lst) (cadr (cdr lst)))
#
# ; BEGIN PROBLEM
# (define (infix expr)
#     (cond
#         ((not (pair? expr)) expr) ; a single value
#         ((or (equal? (car expr) '*) (equal? (car expr) '+)) (eval expr)) ; already in prefix form
#         ((null? (cdr expr)) ____________________)
#         (else
#             (define left (infix ____________________))
#             (define right (infix ____________________))
#             (define operator ____________________)
#         (cond
#             ((equal? operator '+) (+ left ____________________))
#             ((equal? operator '*) (infix (cons ____________________
#                                                 ____________________)))))))
# ; END PROBLEM
#
# ;;; Tests
# (infix '(5))
# ; expect 5
# (infix '(2 * 3))
# ; expect 6
# (infix '(2 + 3))
# ; expect 5
# (infix '(2 * (3 + 6)))
# ; expect 18
# (infix '(2 * 3 + 6))
# ; expect 12
# (infix '(2 + 3 * 6))
# ; expect 20
# """



if __name__ == '__main__':
    import doctest

    # uncomment to test all funcs
    # doctest.testmod()

    # run doctests for a specific function by replacing func_name with the name of the func you want to test
    doctest.run_docstring_examples(make_guess, globals(), verbose=True)