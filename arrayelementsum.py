n = int(input("Enter array size : "))
l = []
[l.append(int(input())) for _ in range(n)]

sum_no_dupes = sum(set(l))

#sum_unique = sum(x for x in l if count(x)==1)
sum_unique = 0
for i in l:
    count = 0
    for j in l:
        if i == j:
            count = count + 1
    if count == 1:
        sum_unique = sum_unique + i

print(f"Sum Unique {sum_unique}")
print(f"Sum no duplicates {sum_no_dupes}")