f = ['f', 'g', 'h']
for x in f:
    print(x)
for x in "July":
    print(x)
for x in f:
    if x=='g':
        break
    print(x)

empty_list = [1, 2, 3, 4, 5, 6]
print(empty_list[2:5])
print(empty_list[:4])
print(empty_list[3:])
print(empty_list[1:5:2])