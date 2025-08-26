def factor(n):
    fact = []
    for i in range(1,n):
        if n%i==0:
            # i is a factor of n
            fact.append(i)
    return fact
def perfect(n):
    fact = factor(n)
    s = 0
    for i in fact:
        s += i
    return s == n
n = int(input("n : "))
x = perfect(n)
print("perfect number" if x else "not perfect number")