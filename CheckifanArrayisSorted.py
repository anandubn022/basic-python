def checkSort(arr):
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
    

arr_1 = [90, 80, 100, 70, 40, 30]
arr_2 = [10, 20, 30, 40, 50]
print(checkSort(arr_1))
print(checkSort(arr_2))
