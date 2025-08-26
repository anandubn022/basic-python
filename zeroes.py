m, n = map (int, input("Enter m: and n: ").split())
width = len(str(n))
for i in range (m, n+1):
    # print(f"{i:0{width}d}", end=" ")
    print(str(i).zfill(width), end=' ')
print()
