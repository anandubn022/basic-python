n=int(input("Enter the number of numbers : "))
a=[]
for i in range(n):
    k = int(input("Enter number : "))
    a.append(k)
r=[]
x=int(input("No of spikes : "))
for i in a:
    c=bin(i)[2:]
    if(len(c)<=x):
        f='0'
    else:
        f=c[:-x]
    g=int(f,2)
    r.append(g)
print(r)
