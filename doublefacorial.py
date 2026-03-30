def doublefactorial(num):
    if num>1:
        return num*doublefactorial(num-2)
    else:
        return 1

num = int(input("enter a number : "))
if num>-1:
    print(f"Double factorial : {doublefactorial(num)}")