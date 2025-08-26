arr = [4,3,7,2,6,1]
lowest = arr[0]
count = 0
for i in arr:
    if(i<lowest):
        count+=1
        lowest = i
print("count",count)