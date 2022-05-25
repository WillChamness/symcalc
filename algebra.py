from sympy import factor, expand, symbols, Eq, solve

def factor_expression(expression, var=symbols("x")):
    return factor(expression, var)

def expand_expression(expression, var=symbols("x")):
    return expand(expression, var)

def zeros(expression, var=symbols("x")):
    return solve(expression, var)

def solve_eq(lhs, rhs, var=symbols("x")):
    return solve(Eq(lhs, rhs), var)


if __name__ == "__main__":
    x = symbols("x")
    y = symbols("y")
    print(factor_expression(x**2 - 3*x + 2, x))
    print(expand_expression((x-2)*(x-1), x))
    print(zeros(x + y, x))
    print(solve_eq(2*x**3, 1/2, x))