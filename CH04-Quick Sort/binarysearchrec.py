def binarysearch(arr, target):
    low = 0
    high = len(arr)-1
    return helper(arr, low, high, target)


def helper(arr, low, high, target):
    if low > high:
        return -1

    mid = (low+high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return helper(arr, mid+1, high, target)
    elif arr[mid] > target:
        return helper(arr, low, mid-1, target)


print(binarysearch([1, 2, 3, 4], 3))
print(binarysearch([1, 2, 3, 4], 5))
