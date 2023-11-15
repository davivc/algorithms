def findBiggest(arr):
    biggest = arr[0]
    biggest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
            biggest_index = i

    return biggest_index

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selectionSort(arr, small=True):
    sortedArr = []
    for i in range(len(arr)):
        if small:
            index = findSmallest(arr)
        else:
            index = findBiggest(arr)
        sortedArr.append(arr.pop(index))

    return sortedArr

print(selectionSort([5, 3, 6, 2, 10]))
print(selectionSort([5, 3, 6, 2, 10], False))