from sympy import Rational
def exact(num):
    """Returns a rational representation of the number.
    """
    return Rational(str(num))
    

def approx(num):
    """Returns an approximation of the number.
    """
    return num.evalf()



if __name__ =="__main__":
    from sympy import RealNumber
    print(exact(RealNumber(3/2)))
    print(approx(Rational(3,2)))