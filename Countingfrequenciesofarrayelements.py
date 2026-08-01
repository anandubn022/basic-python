arr = [10, 20, 10, 5, 20]
arr.sort()
count = {}
for i in arr:
    count[i] = count.get(i, 0) + 1

output = []
for i in count:
    output.append([i, count[i]])

print(output)
