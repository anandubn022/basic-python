# You are given three integers c, y and z representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n.

x = int(input("x : "))
y = int(input("y : "))
z = int(input("z : "))
n = int(input("n : "))

# result = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k != n:
#                 result.append([i, j, k])

result = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]                

print(result)
