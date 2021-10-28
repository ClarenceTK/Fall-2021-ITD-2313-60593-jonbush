# import required library

import math

def prediction():

    sp = int(input("Enter the initial number of organism: "))

    g = float(input("Enter the rate of growth [a real number > 0]: "))

    while(g<1):

        print ("Invalid.. growth rate.")

        g = float(input("Enter the rate of growth [a real number > 0]: "))

    r = int(input("Enter the number of hours to achieve the rate of growth: "))

    t = int(input("Enter the total hours of growth: "))


    tp=sp

    hours = 1

    while (hours < t):

        tp *= g

        hours += r

    print("The total population is " + str(int(tp)))


prediction()