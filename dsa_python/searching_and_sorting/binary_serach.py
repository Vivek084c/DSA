# time complexity - O(log n)

def binary_serach(arr, start, elenment):
    end = len(arr) - 1
    mid = start + (end- start)//2

    while (start<=mid):
        if (arr[mid] == elenment):
            return mid
        elif (arr[mid]>elenment):
            end = mid - 1
        else:
            start = mid + 1 
        mid = start + (end - start)//2
    return -1

arr = [1,2,5,6,7,8,9,10,11,12]
elenment = 7
print(binary_serach(arr,0,8))