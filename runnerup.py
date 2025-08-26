n = int(input("n : "))
A = list(set(list(map(int, input("A : ").split()))))\
# set removes dupes
# sort doesnt remove dupes
print(A)
print("runner up :",A[-2])