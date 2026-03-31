n = int(input("Enter the range of the array : "))
l1 = [int(input()) for _ in range(n)]
count = 0
l2 = []

for i in range(n):
    for j in l1[i:n]:
        s = 0
        for k in l1[i: j+1]:
            s = s|k
        if s not in l2:
            count = count+1
            l2.append(s)

print(count)