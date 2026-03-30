def largestindex(l):
    d = {"max":0, "count":0}
    for i in range(len(l)):
        if l[i]>l[d["count"]]:
            d["max"] = l[i]
            d["count"] = i
    return d

l = [int(x) for x in input()]   #input like 12341
result = largestindex(l)
print(f"Largest Number : {result["max"]}")
print(f"Index : {result["count"]}")