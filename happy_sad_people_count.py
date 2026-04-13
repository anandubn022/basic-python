# Population State Transition

# Problem Statement

# There are N people, and initially all of them are in the Happy state.

# Each person changes state independently in each operation according to the following rules:

# If a person is Happy:

# 70% chance → becomes Sad

# 30% chance → remains Happy

# If a person is Sad:

# 50% chance → becomes Happy

# 50% chance → remains Sad

# Exactly 4 operations are performed.

# Your task is to compute the expected number of people in:

# Happy state

# Sad state

# after all 4 operations.

# If N < 0, print "Error!".

# Input

# A single integer N.

# Output

# Print two integers separated by space:

# Expected number of Happy people

# Expected number of Sad people

# The values should be rounded to the nearest integer

# Example

# Input

# 1000

# Output

# 418 582 

n = int(input())
if n<0:
    print("Error!")
else:
    state = [1.0, 0.0]
    for k in range(4):
        happy = state[0]*0.3 + state[1]*0.5
        sad = state[0]*0.7 + state[1]*0.5
        state = [happy, sad]
    print(round(state[0]*n), round(state[1]*n))


