#include<iostream>
#include<stdlib.h>
#include<iomanip>

#define MAX 100

using namespace std;

int main(){

    long double ax[MAX+1], ay[MAX+1], nr, dr, x, y=0;

    int i,j,n;


    cout<<"Enter the value of n: ";
    cin>>n;
    cout<<"Enter the set of value: "<<endl;
    for(i=0;i<=n;i++){
        cout<<"ax["<<i<<"] = ";
        cin>>ax[i];
        cout<<"ay["<<i<<"] = ";
        cin>>ay[i];
    }
    cout<<"Enter the value of x for which value of y is wanted: ";
    cin>>x;

    for(i=0;i<=n;i++){
        nr=dr=1;
        for(j=0;j<=n;j++){
            if(j!=i){
                nr *= x-ax[j];
                dr *= ax[i]-ax[j];
            }
        }
        y += (nr/dr)*ay[i];
    }

    cout<<"\nWhen x= "<<x<<"\ty = "<<y<<endl;


    return 0;
}