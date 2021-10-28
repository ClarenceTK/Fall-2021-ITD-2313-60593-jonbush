theSum = 0.0
n = 0

while True:

    data = input("Enter a number or press Enter to quit: ")

    if data == '':
        break
    number = float(data)
    theSum += number
    n += 1
print()

print("The sum is", theSum)

if n > 0:
    average = theSum / n

    print('The average is', average)

else:
    print('Average : undefined (as the number of terms eneterd are 0)')