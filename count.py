a = ['A', 'E', 'I', 'O', 'U']
s = input("Enter the string : ")
s = s.upper()
v = 0
w = 0
c = 0
spl = 0
num = 0
for i in s:
    if i in a:
        v+=1
    elif i == " ":
        w+=1
    elif i.isalpha() == True:
        c+=1
    elif i.isdigit() == True:
        num += 1
    else:
        spl += 1
print("Vowels :", v)
print("Consanants :", c)
print("White Spaces :", w)
print("Special Characters :", spl)