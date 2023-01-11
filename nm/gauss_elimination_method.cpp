#include<iostream>
#include<iomanip>
#include<stdlib.h>
#include<math.h>

#define N 3

using namespace std;

int main(){
    long double a[N][N+1], x[N], t, s;
    int i,j,k;

    cout<<"Enter the elements of the augmented matirx rowwise: "<<endl;

    for(i=0;i<N;i++){
        for(j=0;j<N+1;j++){
            cout<<"a["<<i<<"]["<<j<<"]";
            cin>>a[i][j];
        }
    }
    cout<<endl;

    // converting into upper triangular matrix

    for(j=0;j<N-1;j++){
        for(i=j+1;i<N;i++){
            t=a[i][j]/a[j][j];
            for(k=0;k<N+1;k++){
                a[i][k] -= a[j][k]*t;
            }
        }
    }

    cout<<endl<<"Upper triangular matrix is: "<<endl;

    for(i=0;i<N;i++){
        for(j=0;j<N+1;j++){
            cout<<a[i][j];
        }
        cout<<endl;
    }

    //back substitution 

    for(i=N-1;i>=0;i--){
        s=0;
        for(j=i+1; j<N; j++){
            s+=a[i][j]*x[j];
        }
        x[i] = (a[i][N]-s)/a[i][j];
    }

    // printing the result
    cout<<"The Solution is: "<<endl;

    for(i=0;i<N;i++){
        cout<<"x["<<i+1<<"] = "<<x[i]<<endl;
    }

    return 0;
}
