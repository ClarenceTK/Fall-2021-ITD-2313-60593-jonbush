import turtle
import random


def cCurve(t, x1, y1, x2, y2, level):
    def drawLine(x1, y1, x2, y2):
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)

    if level == 0:
        t.pencolor(random.random(), random.random(), random.random())
        drawLine(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) / 2
        ym = (x2 + y1 + y2 - x1) / 2
        cCurve(t, x1, y1, xm, ym, level - 1)
        cCurve(t, xm, ym, x2, y2, level - 1)

def main():
    level = int(input("Enter the level (0 or greater): "))
    t = turtle.Turtle()
    t.pensize(5)
    t.speed(0)
    random.seed()
    cCurve(t, 50, -100, 50, 100, level)
    turtle.done()
main()
