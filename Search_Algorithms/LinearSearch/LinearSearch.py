arr = [3, 6, 8, 9, 11, 14, 16]

def linearSearch(arr,element):
    for i in range(len(arr)):
        if arr[i] == element:
            msg = "Element found in array at position "+ str(i+1)
            break
        else:
            msg = "Element not found in the array"
    return msg

result = linearSearch(arr,12)
print(result)