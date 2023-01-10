#include<iomanip>
#include<iostream>
#include<stdlib.h>

#define SIZE 5

using namespace std;

void enqueue();
void dequeue();
void show();

int front=-1,rare=-1;
int cir_queue[SIZE];

int main(){
    int choice;

    cout<<"select among the following: "<<endl;
    cout<<"1. Enqueue"<<endl<<"2. Dequeue\n3. Show\n4. Exit"<<endl;
    cout<<"Enter your choice: ";
    cin>>choice;

    switch(choice){
        case 1:
            enqueue();
            break;
        case 2:
            dequeue();
            break;
        case 3:
            show();
            break;
        case 4:
            exit(0);
        default:
            cout<<"Invalid choice!!!"<<endl;
            main();
    }

    return 0;
}


void enqueue(){
    if((front==0&&rare==SIZE-1)||(front==rare+1)){
        cout<<"\nQueue is full \n"<<endl;
        main();
    }
    if(front==-1){
        front =0;
        rare = 0;
    }
    else{
        if(rare == SIZE-1){
            rare = 0;
        }
        else{
            rare += 1;
        }
    }
    cout<<"\nEnter value to enqueue: ";
    cin>>cir_queue[rare];
    cout<<"\n\n";
    main();
}

void dequeue(){
    if(front == -1){
        cout<<"\nQueue is empty\n"<<endl;
        main();
    }
    cout<<"Element deleted from queue is: "<<cir_queue[front]<<endl<<endl;

    if(front == rare){
        front = rare = -1;
    }
    else{
        if(front == SIZE-1){
            front=0;
        }
        else{
            front+=1;
        }
    }
    main();
}

void show(){
    if(front == -1){
        cout<<"\nQueue is empty\n"<<endl;
        main();
    }
    cout<<"\nElements in the queue are: \n";
    if(front <= rare){
        for(int i = front; i<=rare; i++){
            cout<<cir_queue[i]<<"\t";
        }
    }
    else{
        for(int i = front; i<=SIZE-1; i++){
            cout<<cir_queue[i]<<"\t";
        }
        front=0;
        for(int i = front; i<=rare; i++){
            cout<<cir_queue[i]<<"\t";
        }
    }
    cout<<"\n\n";
    main();
}