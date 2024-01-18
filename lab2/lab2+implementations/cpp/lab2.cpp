#include <bits/stdc++.h>
#include <limits.h>

using namespace std;

#define SIZE 1000
// stack has the following properties:
// push
// pop
// peek
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

	int peek(){
	    if(top>=0){
		return arr[top];
	    }
	    else{
	    return -1;
	    }
	}
	
	int size(){
	    return top;
	}

	int isEmpty(){
		if(top>0){
			return 0;
		}
		else{
			return 1;
		}
	}

};


int main(){
    int t;
    Stack s1;
    
    cin>>t;
    
    for(int i = 0; i < t; i++){

// 	cout<<"This is my implementation of stack."<<endl;

// 	cout<<"Choose the stack operation you want to perform from the following:"<<endl;
	
// 	cout<<"1. Create a new stack"<<endl;
// 	cout<<"2. Display the stack"<<endl;
// 	cout<<"3. Push an element"<<endl;
// 	cout<<"4. Pop an element"<<endl;
// 	cout<<"5. Check the top element"<<endl;

// 	cout<<"Enter the corresponding index of the operation you want to perform: ";
    
    
    map<string, int> map;
    map["push"] = 1;
    map["pop"] = 2;
    map["peek"] = 3;
    map["size"] = 4;
    map["isempty"] = 5;
    
    string s;
    cin>>s;
    
	switch(map[s]){

	case 1: 
		int element;
		cin>>element;
		s1.push(element);
		break;
	
	case 2:
	    if(s1.top >= 0){
		    s1.pop();
		}
		else{
		    cout<<"stack is empty"<<endl;
		}
	    break;

	case 3:
		cout<<s1.peek()<<endl;
		break;

	case 4:
		cout<<s1.size()<<endl;
		break;

	case 5:
		cout<<s1.isEmpty()<<endl;
		break;

	default:
		cout<<"Enter a valid indice!"<<endl;
	}
	
    }
    

	return 0;
} 