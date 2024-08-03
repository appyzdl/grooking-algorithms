def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total


def sum2(arr):
    if len(arr) == 1:
        return arr[0]
    return arr.pop()+sum2(arr)


def freq(arr):
    if len(arr) == 1:
        return 1
    arr.pop()
    return 1+freq(arr)

# base case: if arr[mid]==target, binarysearch(arr, mid-1) or binarysearch(arr, mid+1)


print("Normla:", sum([1, 2, 3, 4, 5]))
print("Recursive", sum2([1, 2, 3, 4, 5]))
print("Freq", freq([1, 2, 3, 4, 5]))
