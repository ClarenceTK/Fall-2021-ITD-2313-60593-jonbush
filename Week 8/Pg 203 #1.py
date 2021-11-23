def newton(num):
        temp = 0.000001
        estimate = 1.0
        while True:
                estimate = (estimate + num / estimate) / 2
                difference = abs(num - estimate ** 2)
                if difference <= temp:
                   break
        return estimate

def main():
        while True:
                try:
                    num = int(input("Enter a positive number or enter/return to quit: "))

                    print("newton = %0.15f" % newton(num))
                except:
                    return

main()1