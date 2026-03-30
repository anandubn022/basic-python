string = "aababbababcddffgkgkzwnvtqou"
output_list = []
output_string = ""

for i in string:
    j = 0
    for k in string:
        if i == k:
            j = j+1
    if j<2:
            output_list.append(i)
            output_string = output_string+i

print(output_list)
[print(l, end=" ") for l in output_string]