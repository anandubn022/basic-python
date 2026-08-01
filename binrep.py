# Given an integer n, the task is to print the binary representation of the number. 

# Note: The given number will be maximum of 32 bits, so append 0's to the left if the result string is smaller than 30 length.

def binrep(n):
    b_str = bin(n)[2:]
    b_str = 32*'0' + b_str
    b_str = b_str[-32:]
    return b_str

n = 5
print(binrep(n))