times = int(input("enter the number of inputs: "))

count = 1
while count <= times:
    n = int(input("enter the number: "))
    
    f = 1
    num = 1
    while num <= n:
        f = f*num
        num = num + 1
    
    sum = 0
    strfact = str(f)
    i = 0
    while i < len(strfact):
        sum = sum + int(strfact[i])
        i = i + 1
    
    print("Sum is: ",sum)
    count = count + 1
