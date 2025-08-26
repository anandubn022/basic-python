n=10

order = int(input("No of candies needed: "))

if(order > n):
    print("Order invalid")
else:
    print(order, "candies sold")
    k=n-order
    if(k<=5):
        print("No of candies available", n)
    else:
        print("No of candies available", k)