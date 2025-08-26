m=int(input("Enter the no of rows:"))
n=int(input("Enter the no of cols:"))
print(f"Enter {m*n} elements:")
iplist=list(map(int,input().split()))

mat=[]
for k in range(m):
    start=k*n
    end=start+n
    row=iplist[start:end]
    mat.append(row)

index=-1
count=0
for i in range(m):
    rowcount=0
    for j in range(n):
        if mat[i][j]==1:
            rowcount+=1
    if rowcount>count:
        count=rowcount
        index=i
print(index+1)