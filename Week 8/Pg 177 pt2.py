def summation(lower, upper, margin):
    """Returns the sum of the numbers from lower through upper,and outputs a trace of the arguments and return values on each call"""
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + summation(lower + 1, upper, margin + 4)
        print(blanks, result)
    return result