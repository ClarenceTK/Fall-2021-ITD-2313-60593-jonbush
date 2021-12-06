class Student:
   def __init__(self, name):
       self.name = name

   def __eq__(self, stud2):
       if self.name == stud2.name:
           return True
       else:
           return False

   def __lt__(self, stud2):
       if self.name < stud2.name:
           return True
       else:
           return False

   def __ge__(self, stud2):
       if self.name >= stud2.name:
           return True
       else:
           return False


def main():
   s1 = Student("Retheesh")
   s2 = Student("Sampath")

   print("s1: " + s1.name)
   print("s2: " + s2.name)

   print("\nIs s1 = s2 ? ", end = ' ')
   print(s1.__eq__(s2))

   print("Is s1 = s1 ? ", end = ' ')
   print(s1.__eq__(s1))

   print("Is s1 < s2 ? ", end = ' ')
   print(s1.__lt__(s2))

   print("Is s2 < s1 ? ", end = ' ')
   print(s2.__lt__(s1))

   print("Is s1 >= s2 ? ", end = ' ')
   print(s1.__ge__(s2))

   print("Is s2 >= s1 ? ", end = ' ')
   print(s2.__ge__(s1))


main()