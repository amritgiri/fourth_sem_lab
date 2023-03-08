from graphics import *
import time
win=GraphWin("Bresenham line algo",1000,1000)
def main():
    offsetx=500
    offsety=500

    while True:
        x1 = offsetx+int(input("x1: "))
        y1 = offsety-int(input("y1: "))
        x2 = offsetx+int(input("x2: "))
        y2 = offsety-int(input("y2: "))

        linedraw(offsetx,0,offsetx,1000,"black",0)
        linedraw(0,offsety,1000,offsety,"black",0)

        linedraw(x1,y1,x2,y2,"blue")

        choice = input("Enter 'y' to continue: ")
        if choice == 'y' or choice == 'Y':
            global win
            win = GraphWin("Bresenham line algo",1000,1000)
            continue
        else:
            break
    # win.getMouse()
    win.close()

def abs(n):
    if(n>0):
        return n
    else:
        return (-1)*n

def linedraw(x1,y1,x2,y2,color="red",t=.005):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    xin=1
    yin=1
    x=x1
    y=y1
    # pk=(2*dy)-dx
    if x2<x1:
        xin = -1
    if y2<y1:
        yin=-1
    if (dx)>(dy):
        pk=2*dy-dx
        for i in range(dx):
            if(pk>0):
                x+=xin
                y+=yin
                pk+=2*dy-2*dx
            else:
                x+=xin
                pk+=2*dy
            put_pixel(x,y,color,t)
    elif (dy)>(dx):
        pk=2*dx-dy
        for i in range(dy):
            if pk>0:
                x+=xin
                y+=yin
                pk+=(2*dx)-(2*dy)
            else:
                y+=yin
                pk+=2*dx
            put_pixel(x,y,color,t)


def put_pixel(x,y,color="red",t=.005):
    global win
    p= Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(t)

main()