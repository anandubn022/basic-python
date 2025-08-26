def fact(n):
    if n < 0:
        print("Not defined")
        exit()
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
n = int (input("n : "))
f = fact(n)
print("f :", f)