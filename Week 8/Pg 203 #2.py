import math
tolerance=0.00001
estimate=1.0
x = float(input("Enter a positive number: "))
def newton(num,estimate):
    estimate=(estimate+num/estimate)/2
    difference =abs(num-estimate**2)
    if difference<= tolerance:
        return estimate
    else:

        return newton(num,estimate)

print("The program's estimate: ",newton(x, estimate))

print("Python's estimate: ",math.sqrt(x))