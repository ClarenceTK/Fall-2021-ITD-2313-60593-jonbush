def summation(lower, upper):
    """Returns the sum of the numbers from lower through upper."""
    if lower > upper:
        return 0
    else:
        return lower + summation (lower + 1, upper)