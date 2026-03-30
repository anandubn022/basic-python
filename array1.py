n = int(input("array size : "))
l = []
[l.append(int(input())) for _ in range(n)]
print(l)

sum = 0
for i in l:
    sum = sum + i
print(f"Sum : {sum}")

print(f"Average : {sum/n}")

l.sort(reverse=True)
print(f"Biggest : {l[0]}")
print(f"3rd Biggest : {l[2]}")
print(f"Smallest : {l[n-1]}")