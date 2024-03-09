class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
        
class SLL:
    def __init__(self,start=None):
        self.start=start
    
    def isEmpty(self):
        return self.start==None
    
    def insertAtstart(self,data):
        n=Node(data,self.start)
        self.start=n
        
    def insertAtlast(self,data):
        n=Node(data)
        if not self.isEmpty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
    def inserAfter(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def printList(self):
        temp=self.start
        while temp is not None:
            print(temp.item, end='  ')
            temp=temp.next
            
    def deleteAtStart(self):
        if self.start is not None:
            self.start=self.start.next
        
    def deleteAtLast(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    
    def deleteItem(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return SLLiterable(self.start)
            
#to make the ssl class iterable we make a new class
class SLLiterable:
    def __init__(self,  start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
        
ll=SLL()
ll.insertAtstart(10)
ll.insertAtstart(9)
ll.inserAfter(ll.search(10),11)
ll.insertAtlast(12)
ll.printList()
print()
ll.deleteItem(10)
print()
ll.printList()
print()

for k in ll:
    print(k)