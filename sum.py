n = int(input("Enter a number : "))
s = 0
while n!=0:
    tep = n%10
    s += tep
    n = n//10
print("sum" , s)