def partition(min_idx, max_idx, arr):
    ind = min_idx - 1
    pivot = arr[max_idx]
    for current in range(min_idx, max_idx):
        if arr[current] <= pivot:
            ind = ind + 1
            arr[current], arr[ind] = arr[ind], arr[current]
    arr[max_idx], arr[ind + 1] = arr[ind + 1], arr[max_idx]
    return ind + 1


def quickSort(min_idx, max_idx, arr):
    if min_idx < max_idx:  # We check the length of the array.
        # In quick sort the pivot's points sorted index is found
        pivot_idx = partition(min_idx, max_idx, arr)
        # Now, we consider the left and right indexes of pivot point and pass them as separate arguments
        quickSort(min_idx, pivot_idx - 1, arr)
        quickSort(pivot_idx + 1, max_idx, arr)


# Here is the array of values to be sorted
arr = [8, 7, 6, 5, 4, 3, 2, 1, 1, 0, 8, 5]
min_idx = 0
max_idx = len(arr) - 1
quickSort(min_idx, max_idx, arr)  # We are passing the indexes of the array an array as a parameter to sort
for i in range(len(arr)):
    print(arr[i])
