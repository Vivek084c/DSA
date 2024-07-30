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

    // destructor 
    ~Node(){
        int value = this -> data;
        // memory free
        if (this->next != NULL){
            delete next;
            this->next = NULL;
        }
        cout<<"memory is free for node with data "<< value << endl;
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

//deleting the node
void deleteNode(int position, Node* &head){
    // deleteing the starting node
    if (position == 1){
        Node* temp = head;
        head = head->next;
        // free the memory
        delete temp;
    }
    else{
        // deleting other node
        Node* cur = head;
        Node* prev  = NULL;
        int  cnt = 1;
        while (cnt <= position){
            prev = cur;
            cur = cur->next;
            cnt ++;
        }
        prev->next = cur->next;
        cur -> next = NULL;
         
    }
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

deleteNode(2, head);

print_list(head);

return 0;
}
