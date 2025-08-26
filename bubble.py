import math
a = [2,5,1,3,1,5,9,6,7]
print("Input",*a)
n=len(a)

for i in range(n):
    flag = False
    for j in range(n-i-1):
        if a[j+1]<a[j]:
            a[j],a[j+1]=a[j+1],a[j] #swap
            flag = True
    if flag == False:
        break
print("Output",*a)