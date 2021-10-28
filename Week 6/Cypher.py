string = input("Enter a message: ")
n = int(input("Enter the distance value: "))
print()
output = ""
for i in string:
    output += chr(ord(i)+n)
print(output)