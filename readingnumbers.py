inp = input("Enter the numbers ").split()
numbers = []
for i in inp:
    try:
        out = int(i)
        numbers.append(out)
    except:
        print(f"Invalid number {i}")
print(f"Numbers are {numbers}")