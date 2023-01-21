from graphics import *
import time
win=GraphWin("A STRAIGHT LINE USING DDA LINE DRAWING ALGORITHM",900,900)
def main():
    x1 = int(input("Enter coordinate x1: "))
    y1 = int(input("Enter coordinate y1: "))
    x2 = int(input("Enter coordinate x2: "))
    y2 = int(input("Enter coordinate y2:  "))
    linedraw(x1,y1,x2,y2)
    win.getMouse()
    win.close()

def linedraw(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    x=x1
    y=y1
    p=2*(dy-dx)
    while(x<x2):
        if(p>=0):
            put_pixel(x,y,"red")
            y=y+1
            p=p+2*dy-2*dx
        else:
            put_pixel(x,y,"red")
            p=p+2*(dy)
        x=x+1


def put_pixel(x,y,color="red"):
    global win
    p= Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.05)

main()