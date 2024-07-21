#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;

    // constructor
    Node (int data){
        this ->data = data;
        this ->next = NULL;
    }
};

void inser_at_head(Node* &head, int data){
        // creating a new node
        Node* temp = new Node(data);

        // making the temp pointer point at head
        temp -> next = head;
        head = temp;
}

//traversing a linked list
void print_list(Node* &head){
    Node* temp = head;
    while (temp != NULL){
        cout<<temp->data<<" ";
        temp = temp ->next;
    }
    cout<<endl;
}


int main(){

// creating a new node
Node* node1 = new Node(10);
// cout<<node1->data<<endl;
// cout<<node1->next<<endl;

// head pointer
Node* head=node1;

//inserting at head
inser_at_head(head, 12);

print_list(head);

inser_at_head(head, 15);

print_list(head);

return 0;
}
