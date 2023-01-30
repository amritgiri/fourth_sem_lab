#include<iostream>

using namespace std;

class Node{
    public:
        int data;
        Node* next;
};

class Linkedlist{
    public:
        Node* head;
        void insertBeg();
        void insertMid();
        void insertEnd();
        void deleteBeg();
        void deleteMid();
        void deleteEnd();
        void show();
};

void Linkedlist::insertBeg(){
    Node* 
}

int main(){
    Linkedlist list;
    int choice;
    cout<<"Select: "<<endl;
    cout<<"1) Insert at beginning\n2) Insert at middle\n3) Insert at end\n4)Delete from beginning\n5) Delete from Middle\n6) Delete from End\n7) Show\n8)Exit"<<endl;
    cout<<"Enter your choice: ";
    cin>>choice;

    switch (choice)
    {
    case 1:
        list.insertBeg();
        break;
    case 2:
        list.insertMid();
        break;
    case 3:
        list.insertEnd();
        break;
    case 4:
        list.deleteBeg();
        break;
    case 5:
        list.deleteMid();
        break;
    case 6:
        list.deleteEnd();
        break;
    case 7:
        list.show();
        break;
    case 8:
        exit(0);

    default:
        cout<<"Invalid choice!!!"<<endl;
        break;
    }

    main();

    return 0;
}