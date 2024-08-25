# time - O(n^2) , Omega(n^2)
# space - O(1) , 
# use when array size is small

def selection_sort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1,len(arr)-1):
            if (arr[minIndex]>arr[j]):
                minIndex = j
        # swaping the i and minIndex data
        arr[minIndex], arr[i] = arr[i], arr[minIndex]

arr = [1,2,5,7,3,8,2,10,15,12]
selection_sort(arr)
print(arr)

        
    