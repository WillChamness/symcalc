from sympy import factor, expand, symbols, Eq, solve

def factor_expression(expression, var=symbols("x")):
    """Factors a polynomial expression.

    Example: 'x**2 - 3*x + 2' will return '(x-2)*(x-1)'
    """
    return factor(expression, var)

def expand_expression(expression, var=symbols("x")):
    """"Expands the product of polynomial expressions.
    
    Example: '(x+1)*(x**2+x+1)' will return 'x**3 + 2*x**2 + 2*x + 1'
    """
    return expand(expression, var)

def zeros(expression, var=symbols("x")):
    """Finds the (possibly parametarized) set of all numbers x (real or complex) such
    that for every value in that set, the expression evaluates to zero.

    Example: if given x**3 - x**2 + x - 1, then assume x**3 - x**2 + x - 1 == 0. Therefore return [1, -I, I]
    Example: if given x + y, then assume x + y == 0. Therefore return [-y]
    """
    return solve(function, var)

def solve_eq(lhs, rhs, var=symbols("x")):
    """Finds the (possibly parameterized) set of all numbers x (real or complex) such
    that the given equation is true.

    Example: if x**3 == 1, then return [1, -1/2 + I*sqrt(3)/2, -1/2 + I*sqrt(3)/2]
    Example: if y == x**2, then return [-sqrt(y), sqrt(y)]
    """
    return solve(Eq(lhs, rhs), var)
    


if __name__ == "__main__":
    x = symbols("x")
    y = symbols("y")
    print(factor_expression(x**2 - 3*x + 2, x))
    print(expand_expression((x-2)*(x-1), x))
    print(zeros(x + y, x))
    print(solve_eq(2*x**3, 1/2, x))