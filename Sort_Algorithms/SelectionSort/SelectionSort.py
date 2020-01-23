arr = [8, 9, 7, 6, 5, 4, 3, 2, 1]

for i in range(len(arr)):
    # Initially the first element of list is considered as the minimum element
    min_idx = i
    for j in range(i+1,len(arr)):
        # Finds the min element in the list and swaps it with the minimum element position
        if arr[min_idx] >= arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)
