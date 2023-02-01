#include<iostream>
#include<math.h>

using namespace std;

#define f(x,y) (x-y)/(x+y)

int main(){
    float x0,y0,h,m1,m2,m3,m4,y,xn;

    cout<<"Enter the value of x0, y0, h and xn = ";
    cin>>x0>>y0>>h>>xn;
    cout<<fixed;

    while(1){
        if(x0 == xn){
            break;
        }
        m1 = f(x0,y0);
        m2 = f((x0+h/2),(y0+(m1*h)/2));
        m3 = f((x0+h/2), (y0+(m2*h)/2));
        m4 = f((x0+h), (y0+(m3*h)));
        // cout<<m1<<"\t"<<m2<<"\t"<<m3<<"\t"<<m4<<endl;
        y = y0+((h/6)*(m1+2*(m2+m3)+m4));
        x0 += h;
        y0 = y;
        cout<<"When x = "<<x0<<"\t y = "<<y<<endl;
    }

    return 0;
}