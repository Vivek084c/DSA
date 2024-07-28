#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
};

int main(){
    // to create an abject of above node class
    Node* node1 = new Node();
    cout<<"the data in node1 is "<< node1->data<<endl;
    cout<<"the next address in node1 is "<<node1->next<<endl;

    return 0;
}