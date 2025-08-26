def fact(n):
    if n < 0:
        print("Not defined")
        exit()
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
def strong(n):
    tmp = n
    s = 0
    while tmp!= 0:
        rem = tmp%10
        s += fact(rem)
        tmp = tmp//10
    return s==n
n = int(input("Enter a number ; "))
x = strong(n)
print("strong number" if x else "not strong number")