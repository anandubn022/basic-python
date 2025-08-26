def reversefunc(n):
    revr = 0
    while n != 0:
        rem = n % 10        
        revr = (revr * 10) + rem
        n = n // 10
    return revr       

a = int(input("Enter a number "))
x=0
while(x == 0):
    rev = reversefunc(a)
    if a == rev:
        x=1
        print(a, "Palindrome")
    else:
        print(a, "Not Palindrome")
        a = a+rev