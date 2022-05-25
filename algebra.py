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

def zeros(function, var=symbols("x")):
    """Finds the set of all numbers x (real or complex) such that (x, 0) is an
    element of the function f.

    Example: if f(x) = x**3 - x**2 + x - 1,  then return [1, -I, I]
    """
    return solve(function, var)

def solve_eq(lhs, rhs, var=symbols("x")):
    """Finds the (possibly parameterized) set of all numbers x (real or complex) such
    that the given equation is true.

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