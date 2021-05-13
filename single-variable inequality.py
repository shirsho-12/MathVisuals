# Solves ALL single algebraic term ,i.e. x inequalities!

import sympy

x = sympy.Symbol('x')


# eqn = -x**2 + 4 < 0
def poly_inequality_solve(eqn):
    lhs = eqn.lhs
    p = sympy.Poly(lhs, x)
    relation_operator = eqn.rel_op
    return sympy.solve_poly_inequality(p, relation_operator)


# eqn = ((x + 1) / (x + 2)) > 0
def rational_inequality_solve(eqn):
    lhs = eqn.lhs
    numerator, denominator = lhs.as_numer_denom()
    numerator, denominator = sympy.Poly(numerator), sympy.Poly(denominator)
    relation_operator = eqn.rel_op
    return sympy.solve_rational_inequalities([[((numerator, denominator), relation_operator)]])


# eqn = sympy.sin(x) + 0.6 < 0
def trig_inequality_solve(eqn):
    return sympy.solve_univariate_inequality(eqn, x, relational=False)


def ineq_type(eqn):
    expr = sympy.sympify(eqn)
    # sympy.plot(expr)

    if expr.is_rational_function():
        ans = rational_inequality_solve(expr)
    elif expr.is_polynomial():
        ans = poly_inequality_solve(expr)
    else:
        ans = trig_inequality_solve(expr)

    print("Solution: ", end='')
    sympy.pprint(ans)
    

if __name__ == '__main__':
    while True:
        formula = str(input("Enter single-variable inequality: "))
        ineq_type(formula)

