def automorphic(n):
    s = n*n
    if str(s).endswith(str(n)):
        return True
    else:
        return False
n = int(input("n : "))
x = automorphic(n)
print("automorphic number" if x else "not automorphic number")