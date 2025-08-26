def isArmstrong(num):
    su = 0
    order = len(str(num))
    tmp = num
    while tmp!=0:
        digit = tmp%10
        su+=digit**order
        tmp //= 10
    return su == num

n = int(input("lower limit : "))
m = int(input("upper limit : "))

for i in range(n, m+1):
    if isArmstrong(i):
        print(i, end=" ")
print()