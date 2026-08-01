S1 = "aacdb"
S2 = "gafd"
count = {}
for i in S1:
    if i not in count:
        count[i] = 1

for i in S2:
    if i in count:
        count[i] = 2

output = ""

for i in S1:
    if i in count and count[i] == 1:
        output = output + i

for i in S2:
    if i not in count:
        output = output + i

print(output)