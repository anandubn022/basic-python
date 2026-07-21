# Khaled has an array A of N elements. It is guaranteed that N is even. He wants to choose at most N/2 elements from
# array A. It is not necessary to choose consecutive elements. Khaled is interested in XOR of all the elements he chooses.
# Here, XOR denotes the bitwise XOR operation.
# For example:
# If then Khaled can choose the subset to achieve XOR 4 XOR
# Khaled wants to maximize the XOR of all the elements he chooses. Your task is to help Khaled to find the max XOR of a
# subset that he can achieve by choosing at most N/2 elements?
# Input format:
# The first line contairs an integer, N, denoting the number of elements in A.
# Each line i of the N subsequent lines (where contains an integer describing Ai.
# Constraints
# Sample Input 1
# 2
# 1
# 2
# Sample Output 1
# 2
# Explanation:
# N=2, Khaled can choose the subset[21. The xor of the elemene in the subset is 2. And the number of elements in
# the subset is 1 which is less than N/2.
# Sample Input 2
# 4
# 1
# 2
# 4
# 7
# Sample Output 2
# 7
# Explanation:
# N=4, Khaled can choose the subset [71. The xor of the elements in the subset is 7, and the number of
# elements in the subset is 1 which is less than N/2.

from itertools import combinations

def find_max(arr, n):
    let_max = max(arr)

    for size in range(2, n//2 + 1):
        for subset in combinations(arr, size):
            z = 0
            for x in subset:
                z ^= x
            let_max = max(let_max, z)

    return let_max

n = int(input())
arr = []
for i in range (n):
    arr.append(int(input()))
if n<3:
    print(max(arr))
else:
    print(find_max(arr, n))