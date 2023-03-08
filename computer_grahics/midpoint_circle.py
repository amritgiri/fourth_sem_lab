from graphics import *
import time
win = GraphWin("Circle midpoint line", 900, 900)

def main():

    x = int(input("Enter center x of circle: "))
    y = int(input("Enter center y of circle: "))
    r = int(input("Enter the radius of the circle: "))


    # circle(450,450,75)    
    for i in range(r):
        circle(x+i,y+i,i)

    win.getMouse()
    win.close()
def circle(x1,y1,r):
    x=r
    y=0
    d=0

    while(x>=y):

        put_pixel(x1+x,y1+y,"red")
        put_pixel(x1+y,y1+x,"red")
        put_pixel(x1-y,y1+x,"blue")
        put_pixel(x1-x,y1+y,"blue")
        put_pixel(x1-x,y1-y,"yellow")
        put_pixel(x1-y,y1-x,"yellow")
        put_pixel(x1+y,y1-x,"black")
        put_pixel(x1+x,y1-y,"black")
        
        if(d<=0):
            y+=1
            d=d+2*y+1
        if(d>0):
            x=x-1
            d=d-2*x+1

def put_pixel(x,y,color="red"):
    global win
    p= Point(x,y)
    p.setFill(color)
    p.draw(win)
    time.sleep(.005)

main()