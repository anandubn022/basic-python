d ={
    "even":0, "odd":0
}

l = [1,2,3,4,5,6,7,8,9]

for i in l:
    if i%2 == 0:
        d.update({"even" : d["even"] + 1})
    else:
        d.update({"odd" : d["odd"] + 1})
print(d)