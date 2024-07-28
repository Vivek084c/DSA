#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;

    // constructor for node class
    Node(int data){
        this->data = data;
        this->next = NULL;
    }
};

void insertAtHead(Node* &head, int data){
    // creating a new node 
    Node* temp  = new Node(data);
    temp -> next = head;
    head = temp;
};

void insertAtTail(Node* &tail, int data){
    // creating a node
    Node* temp = new Node(data);
    tail->next = temp;
    tail = tail->next;
}

void isertAtPosition(Node* &tail,Node* &head, int position, int data){
    // insertion at head
    if (position == 1){
        insertAtHead(head, data);
        return;
    }

    int pos = 1;
    Node* temp = head;
    while (pos < position-1){
        temp = temp->next;
        pos++;
    }

    if (temp->next == NULL){
        insertAtTail(tail, data);
        return;
    }

    // creating a new node
    Node* newNode = new Node(data);
    newNode->next = temp->next;
    temp->next = newNode;
}

void print(Node* &head){
    Node* cur = head;
    while (cur != NULL){
        cout<<cur->data<<" ";
        cur = cur -> next;
    }
};

int main(){
    // to create an abject of above node class
    Node* node1 = new Node(15);
    cout<<"the data in node1 is "<< node1->data<<endl;
    cout<<"the next address in node1 is "<<node1->next<<endl;

    // pointing head to node1
    Node* head  = node1;
    Node* tail = node1;

    // inserting at head
    // insertAtHead(head, 12);
    // insertAtHead(head, 13);
    // insertAtHead(head, 14);

    // inserting at tail
    insertAtTail(tail, 16);
    insertAtTail(tail, 17);
    print(head);

    isertAtPosition(tail, head, 4, 33);
    cout<<endl;
    print(head);

    cout<<endl;
    cout<<"head "<<head->data<<endl;
    cout<<"tail "<<tail->data<<endl;

    return 0;
}