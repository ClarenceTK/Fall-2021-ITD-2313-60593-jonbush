while True:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        break
else:
    print("Error: grade must be between 100 and 0")
print(number)