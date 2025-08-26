t = {
    "br":"F", "m":"M", "year":1964
}
print(t)
print(len(t))
print(t["m"])
print(type(t))
print(t.keys())
print(t.values())
t["car"] = "volvo"
t["year"] = 2025
print(t)
print(t.items())
d = t.items()
print(d)
if "m" in t:
    print("m is found")
t.update({"year": 2020})
t.pop("m")
print(t)
del t