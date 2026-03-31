n = int(input("enter the range : "))
print("enter the array", end="\n")
l = [int(input()) for _ in range(n)]
k = int(input("no of shifts : "))
temp = 0

while(k>0):
    
    temp = l[n-1]
    for i in range(n-1, 0, -1):
        l[i] = l[i-1]
    l[0] = temp

    k = k-1

print(f"after shift {l}")