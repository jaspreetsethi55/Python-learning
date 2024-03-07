#!/usr/bin/python3.4

'''
Let us consider polynomials in a single variable x with integer coefficients: for instance, 3x4 - 17x2 - 3x + 5. Each term of the polynomial can be represented as a pair of integers (coefficient,exponent). The polynomial itself is then a list of such pairs.

We have the following constraints to guarantee that each polynomial has a unique representation:

Terms are sorted in descending order of exponent
No term has a zero cofficient
No two terms have the same exponent
Exponents are always nonnegative
For example, the polynomial introduced earlier is represented as

[(3,4),(-17,2),(-3,1),(5,0)]
The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.

Write Python functions for the following operations:


addpoly(p1,p2)
multpoly(p1,p2)
that add and multiply two polynomials, respectively.

You may assume that the inputs to these functions follow the representation given above. Correspondingly, the outputs from these functions should also obey the same constraints.

Hint: You are not restricted to writing just the two functions asked for. You can write auxiliary functions to "clean up" polynomials – e.g., remove zero coefficient terms, combine like terms, sort by exponent etc. Build a library of functions that can be combined to achieve the desired format.

You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation, and then convert back.

Some examples:

>>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
[(2, 1),(3, 0)]
Explanation: (4x3 + 3) + (-4x3 + 2x) = 2x + 3

>>> addpoly([(2,1)],[(-2,1)])
[]
Explanation: 2x + (-2x) = 0

>>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
[(1, 3),(-1, 0)]
Explanation: (x - 1) * (x2 + x + 1) = x3 - 1

'''

res = {}

def analyze_expr(exp,pwr):
    if(pwr in res):
        res[pwr] = res[pwr] + exp

        if(res[pwr] == 0):
            del(res[pwr])

    else:
        res[pwr] = exp

    return 1

def add_poly(l1,l2):
    for (exp1,pwr1),(exp2,pwr2) in zip(l1,l2):
        analyze_expr(exp1,pwr1)
        analyze_expr(exp2,pwr2)

    return res

print([(4,0),(5,4)],[(-4,3),(4,4)])
print(add_poly([(4,0),(5,4)],[(-4,3),(4,4)]))
