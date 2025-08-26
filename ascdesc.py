a = [2,5,1,3,7,5,9,7]
print("Input",*a)
n=len(a)
for i in range(0, n-1):
    for j in range(0,(n//2)):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    for j in range((n//2), n-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("Output",*a)

# import math
# a = [2,5,1,3,1,5,9,6,7]
# print("Input",*a)
# n=len(a)

# for i in range(math.floor(n/2)):
#     flag = False
#     for j in range(math.floor(n/2)-i-1):
#         if a[j+1]<a[j]:
#             a[j],a[j+1]=a[j+1],a[j] #swap
#             flag = True
#     if flag == False:
#         break
# print("Output",*a)                                          

# for i in range(n - math.floor(n/2)):
#     for j in range(math.floor(n/2),n-i-1):
#         if a[j+1]>a[j]:
#             a[j],a[j+1]=a[j+1],a[j] #swap
# print("Output",*a)