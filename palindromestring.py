s = "Abc 012..##  10cbA"
o = []
for i in s:
    if ('A' <= i <= 'Z') or ('a' <= i <= 'z') or ('0' <= i <= '9'):
        o.append(i)
if o == (o[::-1]):
    print(True)
else:   print(False)
        