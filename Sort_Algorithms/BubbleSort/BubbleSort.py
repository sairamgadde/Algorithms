a = [4, 6, 2, 1, 3, 8, 0]
for n in range(len(a)-1):
    for i in range(len(a)-1):
        # In bubble sort for every iteration we find the highest element in the list and swap it
        if a[i] > a[i+1]:
            swap = a[i+1]
            a[i+1] = a[i]
            a[i] = swap
    # prints the list for each iteration
    print(a)
