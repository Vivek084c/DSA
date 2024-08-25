# adaptable algorithm
# time - O(n^2), Omega(n)
# space - O(1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j] #shifting elenemnt to the right
            j -=1
        arr[j+1] = temp

arr = [1,2,5,7,3,8,2,10,15,12]
insertion_sort(arr)
print(arr)