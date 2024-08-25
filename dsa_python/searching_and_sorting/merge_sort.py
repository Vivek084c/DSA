# time - O(n log n)
# space - O(n)

def merge(arr, start, mid, end):
    # creating two arrays: one from start to mid and the other from mid+1 to end
    len1 = mid - start + 1
    len2 = end - mid

    # creating two arrays with the above lengths
    first = [0] * len1
    second = [0] * len2

    # copying values to the first array
    k = start
    for i in range(len1):
        first[i] = arr[k]
        k += 1

    # copying values to the second array
    k = mid + 1
    for i in range(len2):
        second[i] = arr[k]
        k += 1

    # merge two sorted arrays
    index1 = 0
    index2 = 0
    k = start

    # copying values from first and second to main arr in ascending order
    while index1 < len1 and index2 < len2:
        if first[index1] <= second[index2]:  # Ensure stability
            arr[k] = first[index1]
            k += 1
            index1 += 1
        else:
            arr[k] = second[index2]
            k += 1
            index2 += 1

    # copying the leftover elements
    while index1 < len1:
        arr[k] = first[index1]
        k += 1
        index1 += 1

    while index2 < len2:
        arr[k] = second[index2]
        k += 1
        index2 += 1


def merge_sort(arr, start, end):
    # base case
    if start >= end:
        return

    mid = start + (end - start) // 2

    # sorting the left part
    merge_sort(arr, start, mid)

    # sorting the right part
    merge_sort(arr, mid + 1, end)

    # merging the two sorted arrays
    merge(arr, start, mid, end)


arr = [1,2,5,7,3,8,2,10,15,12]
merge_sort(arr, 0, len(arr)-1)
print(arr)

