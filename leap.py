def leap(y):
    if (y%4 == 0 and y%100 != 0) or y%400 == 0:
        return True
    else:
        return False
i = int(input("year : "))
r = leap(i)
print("leap year" if r else "not leap year")