# translation with translation vector tx=40 and ty= -20

from graphics import *
import time

win = GraphWin("Translation",900,900)

def main():
    print("Enter the coordinates: \n")
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    x3 = int(input("x3 = "))
    y3 = int(input("y3 = "))

    tx = int(input("Translation vector tx = "))
    ty = int(input("Translation vector ty = "))

    line(x1,y1,x2,y2,"red")
    line(x1,y1,x3,y3,"red")
    line(x2,y2,x3,y3,"red")

    translation(x1,y1,x2,y2,x3,y3,tx,ty)

    
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

def translation(x1,y1,x2,y2,x3,y3,tx,ty):
    x1=x1+tx
    y1=y1+ty
    x2=x2+tx
    y2=y2+ty
    x3=x3+tx
    y3=y3+ty

    line(x1,y1,x2,y2,"blue")
    line(x1,y1,x3,y3,"blue")
    line(x2,y2,x3,y3,"blue")



def put_pixel(x,y,color="red"):
    global win
    p = Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.005)

main()