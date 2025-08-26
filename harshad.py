def harshad(n):
    s = 0
    tmp = n
    while tmp != 0:
        rem = tmp%10
        s += rem
        tmp //= 10
    if n%s == 0:
        return True
    return False
n = int(input("n : "))
x = harshad(n)
print("harshad number" if x else "not harshad number")