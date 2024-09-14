#creating a class heap 
class Heap:
    def __init__(self, size = 0 ):
        self.heap = [0]*100
        self.size = size
    
    def insert(self, value):
        self.size+=1
        insertingIndex = self.size
        #appending at the index of insertingIndex
        self.heap[insertingIndex] = value

        #appending the value to right position 
        while (insertingIndex>1):
            parentIndex = insertingIndex//2
            if self.heap[parentIndex]<self.heap[insertingIndex]:
                #swap them 
                self.heap[parentIndex], self.heap[insertingIndex] = self.heap[insertingIndex], self.heap[parentIndex]
                #update the insertingIndex
                insertingIndex = parentIndex
            else:
                return
            
    def print_heap(self):
        for i in range(1,self.size+1):
            print(self.heap[i],sep=" ")

newHeap = Heap()
newHeap.insert(50)
newHeap.insert(55)
newHeap.insert(53)
newHeap.insert(52)
newHeap.insert(54)

newHeap.print_heap()


