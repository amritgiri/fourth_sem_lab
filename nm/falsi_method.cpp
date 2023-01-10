#include<iostream>
#include<iomanip>
#include<math.h>

#define f(x) cos(x)-x*exp(x)

using namespace std;

void regula(float *x, float x0, float x1, float fx0, float fx1, int *itr){
    *x = x0 - ((x1-x0)/(fx1-fx0))*fx0;
    ++(*itr);
    cout<<"Iteration- "<<*itr<<"X = "<<*x<<endl;
}

int main(){
    int itr=0, maxitr;
    float x0,x1,x2,x3,aerr;
    cout<<"Enter the value of: "<<endl<<"x0 = ";
    cin>>x0;
    cout<<"x1 = ";
    cin>>x1;
    cout<<"Allowed error = ";
    cin>>aerr;
    cout<<"max itr = ";
    cin>>maxitr;

    regula(&x2,x0,x1,f(x0),f(x1),&itr);

    do{
        if(f(x0) * f(x2) < 0){
            x1 = x2;
        }
        else{
            x0=x2;
        }
        regula(&x3,x0,x1,f(x0),f(x1),&itr);

        if(fabs(x3-x2) < aerr ){
            cout<<endl<<"After "<<itr<<" iterations, root = "<<x3<<endl<<endl;
            return 0;
        }

        x2=x3;
        
    }while(itr<maxitr);

    cout<<"Solution does not coverage iteration not sufficient"<<endl;

    return 1;
}