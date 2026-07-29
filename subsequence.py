n = int(input())
arr = []
for i in range(n): arr.append(int(input()))

length = 0

for i in range(n):
    curr_length = 0
    for j in range(i, n-1):
        if (arr[j] & arr[j+1]) * 2 < (arr[j] | arr[j+1]):
            curr_length = curr_length + 1

    if curr_length > length: length = curr_length

print(length)