from sympy.parsing.sympy_parser import parse_expr
from sympy import *
from sympy.parsing.sympy_parser import standard_transformations,\
implicit_multiplication_application
from sympy import degree
# node of a doubly linked list
from sympy import sympify
from sympy import Symbol
class node:
    def __init__(self, up=None, down=None, right=None, left=None, exp=None, CV=None):
        self.up = up
        self.down = down 
        self.right = right
        self.left = left
        self.exp = exp
        self.CV = CV    
transformations = (standard_transformations +
    (implicit_multiplication_application,))
P = "3 + x^2 + xyz(xy + y − z) + z^3(1 − 3x)"
P = P.replace('^','**')
P = P.replace('−','-')
regular_expression = parse_expr(P, transformations=transformations)
regular_expression = expand(regular_expression).args
for r in regular_expression:
    print(degree(r,gen = Symbol('z')))
    print(r.coeff(Symbol('z')**3))
print("regular expression",regular_expression)