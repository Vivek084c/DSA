#creating a class heap 
class Heap:
    def __init__(self, size = 0 ):
        self.heap = [0]*100
        self.size = size
    
    def insert(self, value):
        # time o(log n)
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

    def deleteHeap(self):
        # time comp o(log n)
        if self.size==0:
            print("Nothing to delete")
            return  
        
        #taking the last elenemnt and storing as the head
        self.heap[1] = self.heap[self.size]
        self.size -= 1

        #taking root node to its correct positon
        currentIndex = 1
        while (currentIndex<self.size):
            leftIndex = 2*currentIndex
            rightIndex = 2*currentIndex + 1
            
            if leftIndex<=self.size and self.heap[currentIndex]<self.heap[leftIndex]:
                #swaping the values
                self.heap[leftIndex], self.heap[currentIndex] = self.heap[currentIndex], self.heap[leftIndex]
                currentIndex  = leftIndex
            elif rightIndex<self.size and self.heap[currentIndex]<self.heap[rightIndex]:
                self.heap[rightIndex], self.heap[currentIndex] = self.heap[currentIndex], self.heap[rightIndex]
                currentIndex = rightIndex
            else:
                return


def heapify(arr, n, i):
    # tc o(log n)
    largest = i
    leftIndex = 2 * i + 1  # Left child index (0-based)
    rightIndex = 2 * i + 2  # Right child index (0-based)

    # Check if the left child exists and is greater than the current largest
    if leftIndex < n and arr[leftIndex] > arr[largest]:
        largest = leftIndex

    # Check if the right child exists and is greater than the current largest
    if rightIndex < n and arr[rightIndex] > arr[largest]:
        largest = rightIndex

    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)
    

newHeap = Heap()
newHeap.insert(50)
newHeap.insert(55)
newHeap.insert(53)
newHeap.insert(52)
newHeap.insert(54)

print("Heap before deletion")
newHeap.print_heap()
newHeap.deleteHeap()
print("heap after deletion")
newHeap.print_heap()


arr = [-1, 54, 53, 55, 52, 50]

#heapifying the values from n/2 to 0
n=5
for i in range(n//2,0,-1):
    # rc o(n) ***********************
    heapify(arr, n, i)

print("the array values are: ")
for i in arr:
    print(i, sep=" ")
print("vivek was here")


