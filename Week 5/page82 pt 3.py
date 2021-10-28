from math import sqrt
number = int(input("Enter the numeric grade: "))
if number >= 0 and number <= 100:
    Square = number * number
else:
    Square = number * number
    print("Error: grade must be between 100 and 0", Square)