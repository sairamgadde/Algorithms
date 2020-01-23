arr = [3, 6, 8, 9, 11, 14, 16]


def binarySearch(arr, start, end, element):
    if start < end:
        mid = (start + end) // 2
        if arr[mid] == element:
            print("Element found at position " + str(mid + 1))
        elif arr[mid] > element:
            binarySearch(arr, start, mid, element)
        elif arr[mid] < element:
            binarySearch(arr, mid + 1, end, element)
    else:
        print("Element not found in the given array")


binarySearch(arr, 0, len(arr) - 1, 12)
