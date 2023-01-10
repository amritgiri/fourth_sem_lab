#include<stdio.h>
#include<stdlib.h>

#define SIZE 4


void push();
void pop();
void show();

int top = -1;
int stack[SIZE];

int main(){
    int a;
    printf("\n1. Push operation\n2. Pop operation\n3. Show stack\n4. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &a);

    while(1){
        switch(a){
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                show();
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid selection\n\n");
                main();
        }

        main();
    }
    return 0;
}

void push(){
    if(top == SIZE-1){
        printf("Underflow!!\n");
        main();
    }

    else{
        printf("Enter a number to push: ");
        scanf("%d", &stack[top+1]);
        top += 1;
        main();
    }
}

void pop(){
    if(top == -1){
        printf("Underflow!!\n");
        main();
    }
    else{
        int x = stack[top];
        stack[top]=0;
        printf("Popped element from stack: %d", x);
        top -= 1;
        main();
    }

}


void show(){
    if(top == -1){
        printf("Underflow!!\n");
        main();
    }

    else{
        printf("Element present in stack are:\n");
        for(int i=0; i<SIZE; i++){
            printf("%d\t", stack[i]);

        }
        printf("\n");
        main();
    }
}