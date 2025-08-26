# n=int(input("Enter n : "))
# a=0
# b=1
# result=0
# for i in range(n):
#     c = a+b
#     result=result+a
#     print(a)
#     a=b
#     b=c
# print("Sum", result)

def fibo(a, b, n):
    if(n == 0):
        return
    c=a+b
    print(a)
    a=b
    b=c
    n=n-1
    fibo(a, b, n)

n = int(input("n : "))
a=0
b=1
fibo (a, b, n)