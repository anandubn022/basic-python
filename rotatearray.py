def rotatearray(arr, d):
    for i in range(d):
        first = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[len(arr)-1] = first

    return arr

arr = [1, 2, 3, 4, 5, 6]
d = 2
print(rotatearray(arr, d))
