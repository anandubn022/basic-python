# n=6
# arrt = [6,0,1,8,0,2]
# final = []
# i=0
# while i<=n-1:
#     if arrt[i] !=0:
#         final.append(arrt[i])
#     i+=1
# i=0
# while i<=n-1:
#     if arrt[i] ==0:
#         final.append(arrt[i])
#     i+=1
# for i in final:
#     print(i, end=" ")
# print()

n = int (input ("Enter n : "))
arr = list(map(int, input("Enter elements comma separated : ").split(",")))
count = 0
for i in arr:
    if i == 0:
        arr.remove(i)
        count += 1
for i in range(count):
    arr.append(0)
print(arr)