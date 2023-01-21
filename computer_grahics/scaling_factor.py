# scaling with scaling factor sx=2 and sy =2
from graphics import *
import time

win = GraphWin("Scaling",900,900)

def main():
    print("Enter the coordinates: \n")
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    x3 = int(input("x3 = "))
    y3 = int(input("y3 = "))

    sx = int(input("Scaling factor sx = "))
    sy = int(input("Scaling factor sy = "))

    xr = int((x1+x2+x3)/3)
    yr = int((y1+y2+y3)/3)

    print(xr,yr)

    line(x1,y1,x2,y2,"red")
    line(x1,y1,x3,y3,"red")
    line(x2,y2,x3,y3,"red")

    scaling(x1,y1,x2,y2,x3,y3,sx,sy,xr,yr)

    win.getMouse()
    win.close()

def abs(n):
    if(n>0):
        return n
    else:
        return n*(-1)

def line(x1,y1,x2,y2,color):
    dx = x2-x1
    dy = y2-y1

    if(abs(dx)>abs(dy)):
        steps=abs(dx)
    else:
        steps=abs(dy)
    xin=dx/steps
    yin=dy/steps

    x=x1
    y=y1

    for i in range(steps+1):
        put_pixel(x,y,color)
        x=x+xin
        y=y+yin


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

def put_pixel(x,y,color="red"):
    global win
    p = Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.005)

main()