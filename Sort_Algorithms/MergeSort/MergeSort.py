arr = [8, 7, 6, 5, 4, 3, 2, 1, 5, 7, 9, -1, -8]

def mergeSort(arr):
    if len(arr) > 1:
        center = len(arr) // 2
        left_arr = arr[:center]
        right_arr = arr[center:]
        mergeSort(left_arr)
        mergeSort(right_arr)

        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            elif right_arr[j] <= left_arr[i]:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


mergeSort(arr)
print(*arr)
