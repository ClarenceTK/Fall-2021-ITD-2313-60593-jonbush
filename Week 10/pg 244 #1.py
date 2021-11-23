from turtle import *
def drawCircle (turtle, x,y, radius):
    circumference = 2 * 3.14 * (radius/120)
    turtle.up()
    turtle.goto(x,y)
    turtle.goto(0,radius)
    turtle.down()
    for i in range(0,120):
        turtle.forward(circumference)
        turtle.right(3)


def main():
    turtle=Turtle()
    drawCircle(turtle,50,75,100)
    turtle.getscreen()._root.mainloop()

if __name__ == '__main__':
    main()