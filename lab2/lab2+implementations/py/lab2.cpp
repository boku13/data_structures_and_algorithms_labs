#include <bits/stdc++.h>
#include <fstream>
#include <string>

using namespace std;


class StudentRecord{
private:
    string studentName;
    string rollNumber;

public:
    string get_studentName() {
        return studentName;
    }
    void set_studentName(string Name) {
        studentName = Name;
    }
    string get_rollNumber() {
        return rollNumber;
    }
    void set_rollNumber(string rollnum) {
        rollNumber = rollnum;
    }
};

class Node{
	private:
		Node* next;
		StudentRecord* element;
	public:

	    Node* get_next() {
	        return next; 
	    }
	    StudentRecord* get_element() {
	        return element; 
	    }

	    Node* set_next(Node* value){
	    	next = value;
	    }
	    StudentRecord* set_element(StudentRecord* student){
	    	element = student;
	    }

};

class Entity {
private:
    string name;
    Node* iterator;

public:
    string get_name() {
        return name;
    }
    void set_name(string Name) {
        name = Name;
    }
    Node* get_iterator() {
        return iterator;
    }
    void set_iterator(Node* iter) {
        iterator = iter;
    }
};

vector<StudentRecord> students;
vector<Entity> EntityArray;

class LinkedList : public Entity {
    // Implement LinkedList members here
    Node* head, tail;

    Linkedlist() { 
        head = NULL;
        tail = NULL;
    }

    void insertnode(StudentRecord* student, Node* value){
        Node* newNode = new Node();
        newNode->next = head;
        head = newNode;
    }
};


int main(){

    // Node* head;
    // head = new Node();

    ifstream file 


    LinkedList Hostels;
    Hostels.set_name(Hostels)
    LinkedList Departments;
    LinkedList Courses;
    LinkedList Clubs;
    
    
    for(int i=0; i<4; i++){
        EntityArray.push_back()
    }

    



    
    for(auto i: v){

        Node* next;
        next = new Node();
        
        
        head->next = next;
    }
}