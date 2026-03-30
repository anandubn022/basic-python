def largstindex(l):
    max = 0
    for i in range(len(l)):
        if l[max]<l[i]:
            max = i
    return max
l = list(map(int, input().split(",")))
print(l)
print(largstindex(l))