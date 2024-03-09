// linked list is a linear data structure made of collection on nodes, node is a combination of , why we need linked list.?
//  for array we cant chagnge the lenght of elemnent,  linked list advantafe: dynamic data structure, can shrink and grow as needed on runtime
// deletion is easy in linked list as compare to array

#include<iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;

    //constructor
    Node(int data){
        this -> data=data;
        this -> next=NULL;
        cout<<"hellow wordl"<<endl;
    }
};

void InsertAtHead(Node* &head, int data){
    // creating a new node
    Node* temp=new Node(data);
    temp ->next=head;
    head=temp;

}

//method to traverse a linked list
void printLL(node* &head){
    Node* temp=head;
    while (temp !=NULL){
        cout<<temp->data<< endl;
        temp=temp->next;
    }
    cout<<

}


int main(){
    Node* node1=new Node(4);
    cout<<node1 -> data <<endl;
    cout<<node1 -> next <<endl;
    return 0;
}