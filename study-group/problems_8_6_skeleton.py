"""
CS61A Study Group Pset #12

8/6/2020

SEE BOTTOM FOR DOCTEST INSTRUCTIONS
"""



"""
INTERPRETERS
25 min

Modify scheme so that it keeps track of the number of times each procedure 
is called inside the evaluator You will also add the primitive `call-count` 
that takes a procedure as its argument and returns the number of times the 
procedure has been called since the evaluator was started. This feature 
should work for both primitive and compound procedures.

For example:

scm> (define (foo x))
        (* 2 (+ 1 (* 2 x))))
foo
scm> (call-count foo)
0
scm> (call-count *)
0
scm> (foo 2)
10
scm> (call-count foo)
1
scm> (foo 10)
42
scm> (call-count foo)
2
scm> (call-count *)
4
scm> (call-count (lambda (x) x))
0

Your job is to modify the interpreter to make this work. We have provided 
several possibly relevant functions on the following pages. (You might not 
need all the lines!)
"""
"""
Write call_count below:

____________________
____________________
____________________
____________________
____________________

"""
"""
Other functions for (possible) alterations:
"""
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list)
    in environment ENV."""
    check_procedure(procedure)
    ____________________
    ____________________
    ____________________
    ____________________
    if isinstance(procedure, BuiltInProcedure):
        return procedure.apply(args, env)
    else:
        new_env = procedure.make_call_frame(args, env)
        return eval_all(procedure.body, new_env)


def create_global_frame():
    """Initialize and return a single-frame environment with built-in names."""
    env = Frame(None)
    ____________________
    env.define('apply', BuiltinProcedure(scheme_apply))
    env.define('map', BuiltinProcedure(scheme_map))
    ...
    return env

# Original skeleton
# """
# Write call_count below:
#
# ____________________
# ____________________
# ____________________
# ____________________
# ____________________
#
# """
# """
# Other functions for (possible) alterations:
# """
# def scheme_apply(procedure, args, env):
#     """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list)
#     in environment ENV."""
#     check_procedure(procedure)
#     ____________________
#     ____________________
#     ____________________
#     ____________________
#     if isinstance(procedure, BuiltInProcedure):
#         return procedure.apply(args, env)
#     else:
#         new_env = procedure.make_call_frame(args, env)
#         return eval_all(procedure.body, new_env)
#
#
# def create_global_frame():
#     """Initialize and return a single-frame environment with built-in names."""
#     env = Frame(None)
#     ____________________
#     env.define('apply', BuiltinProcedure(scheme_apply))
#     env.define('map', BuiltinProcedure(scheme_map))
#     ...
#     return env



"""
DATA ABSTRACTION
15 min

Roy and Charles are getting lunch before their sections. They each 
want to buy a main item, a snack, and a soft drink while staying within 
their budget.

We represent the various lunch items with the Food class and its subclasses. 
There’s a sale on snacks right now, so all snacks cost 40% less than their 
listed price. Berkeley charges a 5% tax on soft drinks, so those cost more 
than their base cost. Fill in the cost method for the Snack and SoftDrink 
classes.

For full credit, you must not hard-code the snack discount or the soda tax, 
in case they change in the future.
"""
class Food:
    def __init__(self, name, base_cost):
        self.name = name
        self.base_cost = base_cost

    def cost(self):
        return self.base_cost


class Main(Food):
    type = "main"


class Snack(Food):
    type = "snack"
    discount = 0.4
    def cost(self):
        """
        >>> chips = Snack("chips", 1)
        >>> chips.cost()
        0.6
        """
        return ____________________


class SoftDrink(Food):
    type = "softdrink"
    sugar_tax = 0.05
    def cost(self):
        """
        >>> cola = SoftDrink("cola", 2)
        >>> cola.cost()
        2.1
        """
        return ____________________

# Original skeleton
# class Food:
#     def __init__(self, name, base_cost):
#         self.name = name
#         self.base_cost = base_cost
#
#     def cost(self):
#         return self.base_cost
#
#
# class Main(Food):
#     type = "main"
#
#
# class Snack(Food):
#     type = "snack"
#     discount = 0.4
#     def cost(self):
#         """
#         >>> chips = Snack("chips", 1)
#         >>> chips.cost()
#         0.6
#         """
#         return ____________________
#
#
# class SoftDrink(Food):
#     type = "softdrink"
#     sugar_tax = 0.05
#     def cost(self):
#         """
#         >>> cola = SoftDrink("cola", 2)
#         >>> cola.cost()
#         2.1
#         """
#         return ____________________



"""
NONLOCAL PART 1
25 min

An (n)-repeater for a single-argument function f takes a single 
argument x, calls f(x) n times, then returns an (n + 1)-repeater for f.

Implement repeater, which takes a single-argument function f and a positive 
integer n. It returns an (n)-repeater for f. Also implement the helper function 
repeat.
"""
def repeater(f, n):
    """Return an (n)-repeater for f.
    >>> r = repeater(print, 2)
    >>> s = r('CS')
    CS
    CS
    >>> t = s('CS')
    CS
    CS
    CS
    """
    def g(x):
        ____________________
        return ____________________
    return ____________________

def repeat(f, x, n):
    """Call f(x) n times.
    >>> repeat(print, 'Hello', 3)
    Hello
    Hello
    Hello
    """
    if ____________________:
        ____________________
        ____________________

# Original skeleton
# def repeater(f, n):
#     """Return an (n)-repeater for f.
#     >>> r = repeater(print, 2)
#     >>> s = r('CS')
#     CS
#     CS
#     >>> t = s('CS')
#     CS
#     CS
#     CS
#     """
#     def g(x):
#         ____________________
#         return ____________________
#     return ____________________
#
# def repeat(f, x, n):
#     """Call f(x) n times.
#     >>> repeat(print, 'Hello', 3)
#     Hello
#     Hello
#     Hello
#     """
#     if ____________________:
#         ____________________
#         ____________________

"""
NONLOCAL PART 2

Implement compound, which takes a single-argument function f and returns 
a single-argument function g. When g is called for the nth time, it returns 
the result of calling f repeatedly n times. That is, the first call g(x) 
returns f(x), the second call g(y) returns f(f(y)), and the third call g(z) 
returns f(f(f(z))). Do not call repeat or repeater in your implementation.
"""
def compound(f):
    """Return a function that, when called the nth time, applies f repeatedly n times.
    >>> double = lambda y: 2 * y
    >>> doubler = compound(double)
    >>> doubler(3) # 1st call to doubler; double 3 one time
    6
    >>> doubler(5) # 2nd call to doubler; double 5 two times
    20
    >>> doubler(7) # 3rd call to doubler; double 7 three times
    56
    """
    h = ____________________

    def g(x):
        ____________________
        h = ____________________
        return h(x)
    return g

# Original skeleton
# def compound(f):
#     """Return a function that, when called the nth time, applies f repeatedly n times.
#     >>> double = lambda y: 2 * y
#     >>> doubler = compound(double)
#     >>> doubler(3) # 1st call to doubler; double 3 one time
#     6
#     >>> doubler(5) # 2nd call to doubler; double 5 two times
#     20
#     >>> doubler(7) # 3rd call to doubler; double 7 three times
#     56
#     """
#     h = ____________________
#
#     def g(x):
#         ____________________
#         h = ____________________
#         return h(x)
#     return g

"""
NONLOCAL PART 3

Write the values bound to b and c that result from executing the code 
below, assuming compound is implemented correctly.

(Don't use the interpreter for this!)

increment = lambda x: x + 1
h = compound(compound(increment)) 
a, b, c = h(3), h(3), h(3)

Your answers here:
b: ____________________
c: ____________________
"""
# Original skeleton
# Your answers here:
# b: ____________________
# c: ____________________


"""
STREAMS
15 min

Implement the cycle procedure, which takes a non-empty Scheme list of 
values. It returns an infinite stream that repeats those values in order, 
indefinitely. For example, (cycle ’(6 1 a)) evaluates to the infinite stream 
containing the values 6 1 a 6 1 a 6 1 a 6 1...
"""
"""
;;; NO DOCTESTS INCLUDED -- See solutions afterwards.
;;; Copy your finished code into scheme.cs61a.org to test your function

; BEGIN PROBLEM
(define (cycle s) 
    (define (with t)
        (if (null? t)
            ____________________
            (cons-stream ____________________ ____________________))))
    ____________________)
; END PROBLEM
"""
# Original skeleton
# """
# ;;; NO DOCTESTS INCLUDED -- See solutions afterwards.
# ;;; Copy your finished code into scheme.cs61a.org to test your function
#
# ; BEGIN PROBLEM
# (define (cycle s)
#     (define (with t)
#         (if (null? t)
#             ____________________
#             (cons-stream ____________________ ____________________))))
#     ____________________)
# ; END PROBLEM
# """



if __name__ == '__main__':
    import doctest

    # uncomment to test all funcs
    # doctest.testmod()

    # run doctests for a specific function by replacing func_name with the name of the func you want to test
    # to run degrees, use name Network.degrees
    doctest.run_docstring_examples(func_name, globals(), verbose=True)