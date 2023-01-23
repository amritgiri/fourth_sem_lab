#include<iostream>
#include<iomanip>

#define SIZE 5

using namespace std;

void BegInsert();
void RanInsert();
void EndInsert();
void BegDelete();
void RanDelete();
void EndDelete();
void show();

int list[SIZE];
int index=0,front=0,rare=0,temp;

int main(){
    int choice;

    cout<<"Choice from the following: "<<endl;
    cout<<"1) Beginning Insertion\n2) Insertion at End\n3) Random Insertion\n4) Delete from Beginning\n5) Delete from Middle\n6) Delete from End\n7) Show\n8) Exit"<<endl;
    cout<<"Enter your Choice = ";
    cin>>choice;

    switch (choice)
    {
    case 1:
        BegInsert();
        break;
    case 2:
        EndInsert();
        break;
    case 3:
        RanInsert();
        break;
    case 4:
        BegDelete();
        break;
    case 5:
        RanDelete();
        break;
    case 6:
        EndDelete();
        break;
    case 7:
        show();
        break;
    case 8:
        exit(0);
    default:
        cout<<"Invalid Selection"<<endl<<endl;
        break;
    }

    main();

    return 0;
}

void BegInsert(){
    int check = 0;//check for empty
    for(int i=0; i<SIZE; i++){
        if(list[i]==0){
            check=1;
            index = i;
            break;
        }
        else{
            check=0;
        }
    }
    if(check!=1){
        cout<<"List is full"<<endl<<endl;
    }
    else if(list[0]==0){
        cout<<"Enter the element to insert in the beginning: ";
        cin>>list[0];
        front = 0;
        rare+=1;
    }
    else{
        for(int i = index; i>front; i--){
            list[i]=list[i-1];
        }       

        cout<<"Enter the element to insert in the beginning: ";
        cin>>list[0];

        rare+=1;
    }
    cout<<endl<<endl;
}

void RanInsert(){
    int check = 0;//check for empty
    for(int i=0; i<SIZE; i++){
        if(list[i]==0){
            check=1;
            index = i;
            break;
        }
        else{
            check=0;
        }
    }

    if(check!=1){
        cout<<"List is full";
    }
    else{
        cout<<"Index that are free are: "<<endl;
        for(int i = 0;i<SIZE;i++){
            if(list[i]==0){
                cout<<i<<"\t";
            }
        }
        cout<<endl;
        cout<<"Enter the index to insert new element: ";
        if(index<SIZE){
            cin>>index;
            cout<<"Enter the element to insert: ";
            cin>>list[index];
        }else{
            cout<<"invalid";
        }
    }
    cout<<endl<<endl;
}

void EndInsert(){
    if(rare == SIZE){
        cout<<"list is full"<<endl<<endl;
    }
    else{
        cout<<"Enter the element to insert at the end: ";
        cin>>list[rare];
        rare+=1;
    }
    cout<<endl<<endl;
}

void BegDelete(){
    if(rare==front){
        cout<<"No element to delete"<<endl<<endl;
    }
    else{
        temp = list[front];
        list[front]=0;
        front+=1;
        cout<<"Deleted element from the list: "<<temp;
    }
    cout<<endl<<endl;
}

void RanDelete(){

}

void EndDelete(){
    if(front==rare){
        cout<<"No element to delete"<<endl<<endl;
    }
    else{
        temp = list[rare-1];
        list[rare-1] = 0;
        rare-=1;
        cout<<"Deleted element from end: "<<temp;
    }
    cout<<endl<<endl;
}

void show(){
    if(rare==front){
        cout<<"List is empty"<<endl<<endl;
    }
    else{
        cout<<"The list contains:\n";
        for(int i=0; i<SIZE; i++){
            cout<<list[i]<<"\t";
        }
        cout<<endl<<endl;
    }
}