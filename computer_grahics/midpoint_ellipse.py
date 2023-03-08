from graphics import *
import time

win = GraphWin("midpoint ellipse Algorithm", 1000,1000)

def main():
    while True:
        xc = int(input("Enter the value of x coordinate: "))
        yc = int(input("Enter the value of y coordinate: "))
        rx = int(input("Enter the value of x-radius: "))
        ry = int(input("Enter the value of y-radius: "))
        h = int(input("Enter the height for cylider: "))

        for i in range(h):
            ellipse(xc,yc-i,rx,ry)

        choice = input("Enter 'y' to continue: ")
        if choice == 'y' or choice == 'Y':
            global win
            win = GraphWin("midpoint ellipse algo",1000,1000)
            continue
        else:
            break
    # win.getMouse()
    win.close()

def ellipse(xc,yc,rx,ry):
    p1 = ry*ry-rx*rx*ry+(rx*rx)/4
    
    x = 0
    y=ry
    while 2*x*ry*ry <= 2*y*rx*rx:
        if p1<=0:
            x+=1
            p1 = p1 + 2*ry*ry*x + ry*ry
        else:
            x+=1
            y-=1
            p1 = p1 + 2*ry*ry*x +ry*ry - 2*rx*rx*y
        put_pixel(xc+x,yc+y,"red")
        put_pixel(xc+x,yc-y,"blue")
        put_pixel(xc-x,yc+y,"green")
        put_pixel(xc-x,yc-y,"yellow")

    p2 = ry*ry*pow((x+1/2),2)+pow(rx,2)*pow((y-1),2)-rx*rx*ry*ry
    while y!=0:
        if(p2>0):
            y-=1
            p2 = p2 + rx*rx - 2*rx*rx*y
        else:
            x+=1
            y-=1
            p2 = p2+rx*rx - 2*rx*rx*y + 2*ry*ry*x

        put_pixel(xc+x,yc+y,"red")
        put_pixel(xc+x,yc-y,"blue")
        put_pixel(xc-x,yc+y,"green")
        put_pixel(xc-x,yc-y,"yellow")

def put_pixel(x,y,color):
    global win
    p = Point(x,y)
    p.setFill(color)
    p.draw(win)
    # time.sleep(0.0000001)


main()