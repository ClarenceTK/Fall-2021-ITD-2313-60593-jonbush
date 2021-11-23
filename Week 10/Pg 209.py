import turtle
  
t = turtle.Turtle()
 
s = int(input("Enter the length of the side of square: "))
 
for _ in range(4):
  t.forward(s)
  t.left(90)