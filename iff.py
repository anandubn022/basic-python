a = 2000
b = 2000
c = 50

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
elif a==b and b>c:
    print(a, b)
elif b==c and c>a:
    print(b, c)
elif a==c and c>b:
    print(a, c)
else:
    print("equal")