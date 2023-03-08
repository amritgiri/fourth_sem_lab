from graphics import *
import time
import math

win = GraphWin("Shear", 1000,1000)

def main():
    offsetx = 500
    offsety = 500


    print("Enter the coordinates accordingly: \n")
    x1 = offsetx+int(input("X1 = "))
    y1 = offsety-int(input("Y1 = "))
    x2 = offsetx+int(input("X2 = "))
    y2 = offsety-int(input("Y2 = "))
    x3 = offsetx+int(input("X3 = "))
    y3 = offsety-int(input("Y3 = "))
    x4 = offsetx+int(input("X4 = "))
    y4 = offsety-int(input("Y4 = "))

    while True:
        line(offsetx,0,offsetx,1000,"black",0)
        line(0,offsety,1000,offsety,"black",0)

        line(x1,y1,x2,y2,"red")
        line(x2,y2,x3,y3,"red")
        line(x3,y3,x4,y4,"red")
        line(x4,y4,x1,y1,"red")

        choice = int(input("For x-directional shear enter '1'\nFor y-directional shear enter '2'\n Enter your choice = "))

        if choice==1:
            shx = int(input("Enter the value of Shx = "))
            yref = offsety-int(input("Enter the value of Yref = "))
            xshear(x1,y1,x2,y2,x3,y3,x4,y4,shx,yref)
        else:
            shy = int(input("Enter the value of Shy = "))
            xref = offsetx+int(input("Enter the value of Xref = "))
            ysear(x1,y1,x2,y2,x3,y3,x4,y4,shy,xref)

        x = input("Wanna continue?\n [Y] for yes else press any key = ")

        if x == 'Y' or x == 'y':
            global win
            win = GraphWin("shear",1000,1000)
            continue
        else:
            break

    # win.getMouse()
    win.close()

def abs(n):
    if n>0:
        return n
    else:
        return (-1)*n

def line(x1,y1,x2,y2,color,t=0.002):
    dx = x2-x1
    dy = y2-y1

    if abs(dx)>abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    xin = dx/steps
    yin = dy/steps

    x = x1
    y = y1

    for i in range(steps+1):
        put_pixel(x,y,color,t)
        x = x+xin
        y = y+yin

def xshear(x1,y1,x2,y2,x3,y3,x4,y4,shx,yref):
    x1 = x1-(shx*(y1-yref))
    # y1 = y1
    x2 = x2-(shx*(y2-yref))
    # y2 = y2
    x3 = x3-(shx*(y3-yref))
    # y3 = y3
    x4 = x4-(shx*(y4-yref))
    # y4 = y4
    print("coordinate after shear\n x = ",x1,x2,x3,x4,"\nand y = ",y1,y2,y3,y4)
    line(x1,y1,x2,y2,"blue")
    line(x2,y2,x3,y3,"blue")
    line(x3,y3,x4,y4,"blue")
    line(x4,y4,x1,y1,"blue")

def ysear(x1,y1,x2,y2,x3,y3,x4,y4,shy,xref):
    # x1 = x1
    y1 = y1-(shy*(x1-xref))
    # x2 = x2
    y2 = y2-(shy*(x2-xref))
    # x3 = x3
    y3 = y3-(shy*(x3-xref))
    # x4 = x4
    y4 = y4-(shy*(x4-xref))
    print("coordinates after shear\n x = ",x1,x2,x3,x4,"\nand y = ",y1,y2,y3,y4)
    line(x1,y1,x2,y2,"blue")
    line(x2,y2,x3,y3,"blue")
    line(x3,y3,x4,y4,"blue")
    line(x4,y4,x1,y1,"blue")

def put_pixel(x,y,color="red",t=.002):
    global win
    p = Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(t)

main()