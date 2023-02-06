#include<iostream>
#include<cmath>

// #define f(x) (1/(1+x*x))

using namespace std;

float f(float x){
    return (1/(1+x*x));
}

int main(){
    double a,b,h,s,n;

    cout<<"Enter the value of a, b and number of interval 'n' respectively = ";
    cin>>a>>b>>n;
    cout<<fixed;

    h = (b-a)/n;
    cout<<h<<endl;
    s = f(a)+f(b);

    for(int i = 1; i<n; i++){
        cout<<"f = "<<f(a+i*h)<<endl;
        s += 2*f(a+i*h);
    }

    cout<<"Value of intergal is = "<<(h/2)*s;

    return 0;
}