# Count Elements ≥ X

# Problem Statement

# You are given an integer X and a sequence of space-separated integers representing an array. The size of the array is not provided explicitly.

# Your task is to determine how many elements in the array are greater than or equal to X.

# Input

# The first line contains a single integer X.

# The second line contains space-separated integers representing the array.

# Output

# Print a single integer — the count of elements greater than or equal to X.

# Example

# Input

# 5 1 5 7 3 9 5

# Output

# 4 

inp = list(map(int, input().split()))
x = inp[0]
arr = inp[1:]
count = 0
for i in arr:
    if i>=x:
        count = count+1
print(count)