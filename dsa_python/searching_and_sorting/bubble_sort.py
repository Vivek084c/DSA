# time  - O(n^2), Omega(n)
# space - O(1)

def bubble_sort(arr):
    for i in range(1,len(arr)):
        swap = False
        for j in range(len(arr)-i):
            if (arr[j]>arr[j+1]):
                # swaping the lenments
                swap = True
                arr[j], arr[j+1]  = arr[j+1] , arr[j]
        if (swap == False):
            # the array is sorted
            break
arr = [1,2,5,7,3,8,2,10,15,12]
bubble_sort(arr)
print(arr)
