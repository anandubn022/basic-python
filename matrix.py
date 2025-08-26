# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j], end=" ")
#     print()

row = int(input("Enter row : "))
col = int(input("Enter col : "))
matrix = []
for i in range(row):
    row_mat = []
    for j in range(col):
        row_mat.append(int(input(f"Enter [{i+1},{j+1}] : ")))
    matrix.append(row_mat)
print("Matrix is")
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()