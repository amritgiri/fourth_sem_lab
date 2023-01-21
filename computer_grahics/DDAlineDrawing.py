from graphics import *
import time
win=GraphWin("A STRAIGHT LINE USING DDA LINE DRAWING ALGORITHM",900,900)
def main():
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    
    line(x1,y1,x2,y2)

    win.getMouse()
    win.close()

def abs(n):
    if(n>0):
        return n
    else:
        return n*(-1)

def line(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if(abs(dx)>abs(dy)):
        steps=abs(dx)
    else:
        steps=abs(dy)
    (xin)= dx/(steps)
    (yin)= dy/(steps)
    (x)= x1
    (y)=y1
    for i in range(steps+1):
        put_pixel(x,y,"red")
        x=x+xin
        y=y+yin

def put_pixel(x,y,color="red"):
    global win
    p= Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.005)

main()