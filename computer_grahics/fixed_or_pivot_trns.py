from graphics import *
import time
import math

win = GraphWin("fixed or pivot transformation", 1000,1000)

def main():
    # offsetx = 300
    # offsety = 300


    print("Enter the coordinates accordingly: \n")
    x1 = int(input("X1 = "))
    y1 = int(input("Y1 = "))
    x2 = int(input("X2 = "))
    y2 = int(input("Y2 = "))
    x3 = int(input("X3 = "))
    y3 = int(input("Y3 = "))

    xr = int((x1+x2+x3)/3)
    yr = int((y1+y2+y3)/3)

    while True:
        # line(offsetx,0,offsetx,1000,"black",0)
        # line(0,offsety,1000,offsety,"black",0)

        line(x1,y1,x2,y2,"red")
        line(x2,y2,x3,y3,"red")
        line(x3,y3,x1,y1,"red")

        choice = int(input("1. scaling\n2. rotation\n Enter your choice = "))

        if choice == 1:
            sx = int(input("Scaling factor sx = "))
            sy = int(input("Scaling factor sy = "))

            scaling(x1,y1,x2,y2,x3,y3,sx,sy,xr,yr)

        elif choice==2:
            t = int(input("Angle for rotation = "))
            a = t*(3.14/180)
            rotation(x1,y1,x2,y2,x3,y3,a,xr,yr)

        else:
            print("Invalid!!!\n")

        x = input("Wanna continue?\n [Y] for yes else press any key = ")

        if x == 'Y' or x == 'y':
            global win
            win = GraphWin("fixed or pivot transformation",1000,1000)
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

def rotation(x1,y1,x2,y2,x3,y3,a,xr,yr):
    xa=abs(int((x1*math.cos(a))-(y1*math.sin(a))+((yr*math.sin(a))-(xr*math.cos(a))+xr)))
    ya=abs(int((x1*math.sin(a))+(y1*math.cos(a))+((-xr*math.sin(a))-(yr*math.cos(a))+yr)))
    xb=abs(int((x2**math.cos(a))-(y2*math.sin(a))+((yr*math.sin(a))-(xr*math.cos(a))+xr)))
    yb=abs(int((x2*math.sin(a))+(y2*math.cos(a))+((-xr*math.sin(a))-(yr*math.cos(a))+yr)))
    xc=abs(int((x3**math.cos(a))-(y3*math.sin(a))+((yr*math.sin(a))-(xr*math.cos(a))+xr)))
    yc=abs(int((x3*math.sin(a))+(y3*math.cos(a))+((-xr*math.sin(a))-(yr*math.cos(a))+yr)))

    line(xa,ya,xb,yb,"blue")
    line(xa,ya,xc,yc,"blue")
    line(xb,yb,xc,yc,"blue")

def scaling(x1,y1,x2,y2,x3,y3,sx,sy,xr,yr):
    xa=(x1*sx)+(xr*(1-sx))
    ya=(y1*sy)+(yr*(1-sy))
    xb=(x2*sx)+(xr*(1-sx))
    yb=(y2*sy)+(yr*(1-sy))
    xc=(x3*sx)+(xr*(1-sx))
    yc=(y3*sy)+(yr*(1-sy))

    line(xa,ya,xb,yb,"blue")
    line(xa,ya,xc,yc,"blue")
    line(xb,yb,xc,yc,"blue")


def put_pixel(x,y,color="red",t=.002):
    global win
    p = Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(t)

main()