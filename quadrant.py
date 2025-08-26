x, y = map(int, input("Enter coordinates : ").split(","))
print("Output : ", end="")
if x>0 and y>0:
    print("Quadrant 1")
elif x<0 and y>0:
    print("Quadrant 2")
elif x>0 and y<0:
    print("Quadrant 4")
elif x<0 and y<0:
    print("Quadrant 3")
else:   print("Invalid Input")