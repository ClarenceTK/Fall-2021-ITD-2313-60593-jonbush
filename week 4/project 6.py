import math

n=int(input("Enter number of iterations: "))

ct=1

flag=1

s=0

for i in range(n):

    s=s+4/ct*flag

flag=0-flag

ct=ct+2

print("Approximated pi is")

print("%.15f"%s)

print("Math pi is")

print("%.15f"%math.pi)