import math
def calcMedian(c):
    l = len(c)
    h = l//2
    print(h)
    if l%2 == 0:
        return float((c[h-1]+c[h])/2)
    else:
        return float(c[h])
n1 = int(input("Enter n1 : "))
a=[]
for i in range(n1):
    tmp = int(input(f"Enter a[{i}] "))
    a.append(tmp)
print("a :",*a)
n2 = int(input("Enter n2 : "))
b=[]
for i in range(n2):
    tmp = int(input(f"Enter b[{i}] "))
    b.append(tmp)
print("b :",*b)
c = list(set(a+b))
c.sort()
print("c :",*c)
x = calcMedian(c)
print("median :", x)