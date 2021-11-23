import math
TOLERANCE = 0.000001
def newton(x, estimate =1):
   """
   Returns the square root of x."
   """
   difference = abs(x - estimate ** 2)
   if difference <= TOLERANCE:
     return estimate
   else :
      return newton(x, (estimate + x / estimate) / 2)
def main():
   ""
   "Allows the user to obtain square roots."
   ""
   while True:
      x = input("Enter a positive number or enter/return to quit: ")
      if x == "":
         break
      x = float(x)
      print("The program's estimate is", newton(x, 1))
      print("Python's estimate is ", math.sqrt(x))

if __name__ == "__main__":
   main()