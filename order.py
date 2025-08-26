# n = int(input("Enter the size of the array : "))
# arr_matrix = []
# for i in range(n):
#     tmp = int(input(f"Enter element at {i} index : "))
#     arr_matrix.append(tmp)
# print("Array is ", *arr_matrix)
# arr_matrix.sort()
# even = []
# odd = []
# for i in arr_matrix:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(arr_matrix)
# print(even)
# print(odd)
# print ("sum ", (even[len(even)-2]+odd[len(odd)-2]))

rows = int(input("Enter the no of rows "))
cols = int(input("Enter the no of cols "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter element at [{i},{j}]"))
        row.append(val)
    matrix.append(row)
flat_list = []
for row in matrix:
    flat_list.extend(row)
even_matrix = []
odd_matrix = []
for index in range(len(flat_list)):
    if flat_list[index] % 2 == 0:
        even_matrix.append(flat_list[index])
    else:
        odd_matrix.append(flat_list[index])
even_matrix.sort()
odd_matrix.sort()
print("Even Matrix ", *even_matrix)
print("Odd matrix " , *odd_matrix)
second_largest_even = even_matrix[-2]
second_largest_odd = odd_matrix[-2]
result = second_largest_even+second_largest_odd
print ("Sum ", result)