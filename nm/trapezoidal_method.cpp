#include<iostream>
#include<cmath>

#define f(x) exp(x)

using namespace std;

int main(){
    double a,b,h,s,n;

    cout<<"Enter the value of a, b and number of interval respectively = ";
    cin>>a>>b>>n;
    cout<<fixed;
    h = (b-a)/n;
    s = f(a)+f(b);

    for(int i = 1; i<n; i++){
        s += 2*f(a+i*h);
    }
    cout<<"Value of intergal is = "<<(h/2)*s;

    return 0;
}