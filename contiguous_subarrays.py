n = int(input("Enter the range : "))
l = []
[l.append(int(input())) for _ in range(n)]

print("contiguous arrays are") 
for i in range(n):
    for j in range(i, n):
        print(l[i:j+1])