l = [1, 3, 5, 3, 7, 9, 3]
s = int(input("Enter s :"))
d = {
    "count":0
}
for i in l:
    if i == s:
        d["count"]+=1
print(d)