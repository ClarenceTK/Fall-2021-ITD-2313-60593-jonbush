def expo(base, exponent):
    product = 1
    for i in range(exponent):
        product *= base
    return product

def main():

    for exponent in range(5):
        print(exponent, expo(2,exponent))

main()