# class node:
#     def __init__(self,value, left=None ,right=None):
#         self.value = value
#         self.left = left
#         self.right = right
    
# #revursive funtion to build the tree
# def buildNode():
#     print("Enter the data")
#     data = int(input())

#     if data==-1:
#         return
#     root = node(data)

#     print("enter data for left of ",data)
#     root.left = buildNode()
#     print("Enter data for rigth of ",data)
#     root.right = buildNode()
#     return root


# #level order traversal
# def levelOrderTraversal(root):
#     q = []
#     q.append(root)
#     q.append(None)

#     while (len(q)!=0):
#         temp = q[-1]
#         q.pop()

#         if (temp == None):
#             print()
#             if (len(q)!=0):
#                 q.append(None)
#         else:
#             print(temp.data)
#             if temp.left:
#                 q.append(temp.left)
            
#             if temp.right:
#                 q.append(temp.right)



class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Recursive function to build the tree
def buildNode():
    print("Enter the data:")
    data = int(input())
    
    if data == -1:
        return None

    root = Node(data)

    print(f"Enter left child of {data}:")
    root.left = buildNode()

    print(f"Enter right child of {data}:")
    root.right = buildNode()

    return root

# Level-order traversal (BFS)
def levelOrderTraversal(root):
    if not root:
        return

    q = []
    q.append(root)
    q.append(None)  # Using `None` as a level separator

    while len(q) > 0:
        temp = q.pop(0)  # Dequeue the front of the queue

        if temp is None:
            print()  # New line for a new level
            if len(q) > 0:
                q.append(None)  # Append `None` to mark the end of the next level
        else:
            print(temp.value, end=" ")  # Print current node value
            if temp.left:
                q.append(temp.left)  # Enqueue left child
            if temp.right:
                q.append(temp.right)  # Enqueue right child

def inOrder(root):
    if root==None:
        return 
    inOrder(root.left)
    print(root.value, sep=" ")
    inOrder(root.right)
    
def preOrder(root):
    if root == None:
        return 
    
    print(root.value, sep=" ")
    preOrder(root.left)
    preOrder(root.right)



# # Example usage
# root = buildNode()
# levelOrderTraversal(root)

# newNode = node(10)

# creating a tree
root = buildNode()
# 1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1

#traversal
levelOrderTraversal(root)

print("inorder traversal")
inOrder(root)

print("psot order")
preOrder(root)

