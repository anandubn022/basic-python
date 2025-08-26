#read a flat list to convert to 2d list
m = int(input("Enter no of rows : "))
n = int(input("Enter no of cols : "))

print(f"Enter {m*n} element : ")
iplist = list(map(int, input ().split(" ")))

mat = []
for k in range(m):
    start = k*n
    end = start +n
    row = iplist[start:end]
    mat.append(row)
for i in mat:
    print(i)