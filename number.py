from sympy import RealNumber, Rational, Integer, Abs

def exact(real_num):
    """Returns a rational representation of the floating point number.
    """
    return Rational(str(real_num)) # cast to string to preserve precision
    

def approx(rational_num):
    """Returns an approximation of the rational number.
    """
    return rational_num.evalf()


def abs(real_num):
    """Returns the absolute value of the number
    """
    return Abs(real_num)


def round_num(real_num, digits=0):
    """Rounds the number to the specified number of digits. Will 
    round to the nearest integer by default.
    """ 
    number = real_num.evalf()
    rounded_num = round(number, digits)
    if digits == 0:
        return Integer(int(rounded_num))
    else:
        return RealNumber(rounded_num)




if __name__ =="__main__":
    from sympy import RealNumber
    print(exact(RealNumber(3/2))) # 3/2
    print(approx(Rational(3,2))) # 1.5
    print(abs(RealNumber(2)), abs(RealNumber(-1.1))) # 2.0 1.1
    print(round_num(RealNumber(1.1)), round_num(RealNumber(1.5)), round_num(RealNumber(1.8)), round_num(RealNumber(-1.5))) # 1 2 2 -2
