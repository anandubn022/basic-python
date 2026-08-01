a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]

# for i in range(len(a)-1, -1, -1):
#     for j in range(len(b)):
#         if a[i] > b[j]:
#             temp = a[i]
#             a[i] = b[j]
#             b[j] = temp

i = len(a) - 1
j = 0
while i>= 0 and j<len(b):
    if a[i] > b[j]:
        a[i] , b[j] = b[j] , a[i]
        i = i -1
        j = j +1
    else: break

a.sort()
b.sort()
print(a)
print(b)