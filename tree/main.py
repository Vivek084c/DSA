class node:
    def __init__(self,value, left=None ,right=None):
        self.value = value
        self.left = left
        self.right = right
    
#revursive funtion to build the tree
def buildNode():
    print("Enter the data")
    data = int(input())

    if data==-1:
        return
    root = node(data)

    print("enter data for left of ",data)
    root.left = buildNode()
    print("Enter data for rigth of ",data)
    root.right = buildNode()
    return root


#level order traversal
# void levelOrderTraversal(node* root) {
# queue<node*> q;
# q- push (root);
# q- push (NULL*;
# while(!q empty)) {
# node* temp = q. front);
# q- pop();
# if(temp == NULL) {
# //purana level
# complete traverse ho chuka hai
# cout
# < endl;
# if(!q-empty)) {
# //queue still has some child ndoes
# q - push (NULL) ;
# ｝
# ｝
# elset
# cout « temp →> data «< " ";
# if (temp ->left) {
# q- push (temp -> left);
# if(temp
# →>right) {
# q. push ( temp right);
# ｝
# }
# ｝
newNode = node(10)

# creating a tree
buildNode()

