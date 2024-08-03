def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less)+[pivot]+quicksort(greater)


print(quicksort([10, 4, 2, 3]))

# traditional way


def partition(arr, low, high):
    mid = (low+high)//2
    pivot = arr[mid]
    i = low-1

    # move pivot to end
    arr[mid], arr[high] = arr[high], arr[mid]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Move pivot to its final position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quicksort2(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort2(arr, low, pi-1)
        quicksort2(arr, pi+1, high)


arr = [10, 4, 7, 12, 0]
quicksort2(arr, 0, len(arr)-1)
print(arr)
