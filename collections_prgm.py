carlist = ["ford", "toyota", "mazda", "kia", "hyundai", "mahindra"]
print(carlist)
print("carlist[2] : " + carlist[2])
print("cartlist[1:4] : " + format(carlist[1:3]))
carlist[1] = "road"
carlist.append("orange")
carlist.remove("ford")
print("new carlist : " + format(carlist))
thisset = {"apple", "orrange", "berry"}
print(thisset)
for i in thisset:
    print(i)
print("afajf" in thisset)
print("apple" in thisset)
print("len : " +format(len(thisset)))
x = thisset.pop()   #removes random item from set
print(x) 
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 0}
print(set1.union(set2))