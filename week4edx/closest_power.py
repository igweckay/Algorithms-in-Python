def closest_power(base, num):
    '''base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.'''
    x = 1
    if num == 1:
        return 0
    else:
        while (base**x) <=num:
            x+=1

        if abs(base**(x-1)-num) <= abs(base**(x)-num):
            return (x-1)
        else:
            return (x)


closest_power(15, 8.0)