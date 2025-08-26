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