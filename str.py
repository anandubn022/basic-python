a=input("Enter string a : ")
b=input("Enter string b : ")
# c = "".join(char for char in a if char not in b)
c=""
for i in a:
    if i not in b:
        c=c+i
print(c)