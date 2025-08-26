def isPrime(n):
    if n<2:
        return False
    for i in range (2, n//2 + 1):
        if n%i == 0:
            return False
    return True

r1 = int ( input( "lower limit : "))
r2 = int ( input( "upper limit : "))
for i in range (r1, r2):
    b = isPrime(i)
    if b == True:
        print (i, end=" ")
print()