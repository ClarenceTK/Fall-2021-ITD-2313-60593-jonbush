def isSorted(lyst):
     if len(lyst) >= 0 and len(lyst) < 2:
          return True
     else:        
          for i in range(len(lyst)-1):
               if lyst[i] > lyst[i+1]:
                    return False
          return True

def main():
     lyst = []
     print(isSorted(lyst))
     lyst = [1]
     print(isSorted(lyst))   
     lyst = list(range(10))   
     print(isSorted(lyst))
     lyst[9] = 3   
     print(isSorted(lyst))

main()