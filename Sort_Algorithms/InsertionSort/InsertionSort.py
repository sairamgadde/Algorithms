arr = [12, 11, 13, 5, 6]
sorted_arr = arr[:1]
unsorted_arr = arr[1:]


def insertionSort(element):
    for i in range(len(sorted_arr)):
        if element <= sorted_arr[i]:
            elem_pos = i
            break
        else:
            elem_pos = len(sorted_arr)
    sorted_arr.insert(elem_pos, element)
    print(sorted_arr)


for i in range(len(unsorted_arr)):
    insertionSort(unsorted_arr[i])
