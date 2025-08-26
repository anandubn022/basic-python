a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a+b > c and b+c>a and a+c >b:
    print("Valid Triangle")
else:
    print("Invalid Triangle")