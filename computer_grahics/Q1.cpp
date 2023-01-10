#include<iostream>
#include<graphics.h>
#include<cmath>
#include<dos.h>
#define Round(p) (p+0.5)

using namespace std;

int main(){
    float x,y,x1,y1,x2,y2,dx,dy,step;
    float xinc, yinc;

    initwindow(400,400, "DDA Alogrithm");

    cout<<"Enter the value of x1 and y1: "<<endl;
    cin>>x1>>y1;
    cout<<"Enter the value of x2 and y2: "<<endl;
    cin>>x2>>y2;

    x=x1;
    y=y1;

    dx=x2-x1;
    dy=y2-y1;

    if(abs(dx)>abs(dy)){
        step = abs(dx);
    }
    else{
        step = abs(dy);
    }

    xinc = dx/(float)step;
    yinc = dy/(float)step;
    putpixel(Round(x), Round(y), 5);

    int i = 1;

    while(i<=step){
        x = x+xinc;
        y = y+yinc;

        i+=1;

        delay(100);

        putpixel(Round(x), Round(y), 5);

    }

    closegraph();

    return 0;
}