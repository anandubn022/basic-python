# n = int(input("dec "))
# n = bin(n)[2:]
# print("bin", n)

# n = n.replace('0', 'tmp')   
# # Temporarily mark all 0s
# n = n.replace('1', '0')     
# #Flip 1s to 0s
# n = n.replace('tmp', '1')   
# #Change temp-marked 0s to 1s

# print("1's", n)
# n=int(n,2)
# print("dec", n)

n = int(input("dec "))
x = bin(n)[2:]
print("bin",x)

l = n.bit_length()         
# Get the number of bits required to represent 'n' in binary (excluding leading zeros)
mask = (1 << l)            
# Create a number with a single 1 followed by 'l' zeros (i.e., 2^l)
mask = mask - 1                  
# Subtract 1 to get a bitmask of all 1s in 'bit_llen' positions (e.g., 0b111 for 3 bits)

n = n^mask 
# ^ = XOR 
x = bin(n)[2:]
print("bin",x)
print("1's",n)