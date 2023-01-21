# rotation about y-axis by 45 degree in cc-direction

from graphics import *
import time
import math

win = GraphWin("Scaling",900,900)

def main():
    print("Enter the coordinates: \n")
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    x3 = int(input("x3 = "))
    y3 = int(input("y3 = "))

    t = int(input("Angle for rotation = "))
    a = int(math.radians(t))

    xr = int((x1+x2+x3)/3)
    yr = int((y1+y2+y3)/3)

    print(xr,yr)

    line(x1,y1,x2,y2,"red")
    line(x1,y1,x3,y3,"red")
    line(x2,y2,x3,y3,"red")

    rotation(x1,y1,x2,y2,x3,y3,a,xr,yr)

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


def rotation(x1,y1,x2,y2,x3,y3,a,xr,yr):
    xa=int((x1*math.cos(a))-(y1*math.sin(a))+((yr*math.sin(a))-(xr*math.cos(a))+xr))
    ya=int((x1*math.sin(a))+(y1*math.cos(a))+((-xr*math.sin(a))-(yr*math.cos(a))+yr))
    xb=int((x2**math.cos(a))-(y2*math.sin(a))+((yr*math.sin(a))-(xr*math.cos(a))+xr))
    yb=int((x2*math.sin(a))+(y2*math.cos(a))+((-xr*math.sin(a))-(yr*math.cos(a))+yr))
    xc=int((x3**math.cos(a))-(y3*math.sin(a))+((yr*math.sin(a))-(xr*math.cos(a))+xr))
    yc=int((x3*math.sin(a))+(y3*math.cos(a))+((-xr*math.sin(a))-(yr*math.cos(a))+yr))

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