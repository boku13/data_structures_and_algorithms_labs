#include <bits/stdc++.h>

using namespace std;

#define SIZE 1000
// stack has the following properties:
// push
// pop
// isempty
// size


class Stack{

public:
	int arr[SIZE]={0};
	int top;

    Stack(){
        top = -1;
    }
	void push(int a){

		arr[++top]=a;
		return;
	}

	void pop(){
		arr[top--]=0;
		return;
	}

	int getTop(){
		return arr[top];
	}

	bool isEmpty(){
		if(top>0){
			return true;
		}
		else{
			return false;
		}
	}

};


int main(){
    int index;
    Stack s1;
    
    while(index!=6){

	cout<<"This is my implementation of stack."<<endl;

	cout<<"Choose the stack operation you want to perform from the following:"<<endl;
	
	cout<<"1. Create a new stack"<<endl;
	cout<<"2. Display the stack"<<endl;
	cout<<"3. Push an element"<<endl;
	cout<<"4. Pop an element"<<endl;
	cout<<"5. Check the top element"<<endl;

	cout<<"Enter the corresponding index of the operation you want to perform: ";

	
	cin>>index;

	switch(index){

	case 1: 
		cout<<"bleh"<<endl;
		break;

	case 3:
		int element;
		if(s1.top < SIZE){
				cout<<"Enter the element you want to push: ";
				cin>>element;
				s1.push(element);
			}
		else{
			cout<<"Stack is full"<<endl;
		}
		break;

	case 4:
		if(s1.top >= 0){
		    s1.pop();
		}
		else{
		    cout<<"stack empty"<<endl;
		}
		break;

	case 5:
		cout<<"Top of the stack is: "<<s1.getTop()<<endl;
		break;

	default:
		cout<<"Enter a valid indice!"<<endl;
	}
	
    }
    

	return 0;
}