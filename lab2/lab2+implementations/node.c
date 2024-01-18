#include <stdio.h>
#include <stdlib.h>

struct node{
	int data;
	struct node *link;
	//self referential structure in c programming
};

int main(){
	struct node *head = NULL;
	head = (struct node *)malloc(sizeof(struct node));
}