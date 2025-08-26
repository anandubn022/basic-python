user1 = 0
user2 = 0
stop = 0
while(stop == 0):
    choose1 = int(input("Enter 1 Rock 2 Paper 3 Scissors "))
    choose2 = int(input("Enter 1 Rock 2 Paper 3 Scissors "))
    if (choose1 == 1 and choose2 == 2) or (choose1 == 3 and choose2 == 1) or (choose1 == 2 and choose2 == 3):
        user2+=1
    elif (choose1 == 2 and choose2 == 1) or (choose1 == 3 and choose2 == 2) or (choose1 == 1 and choose2 == 3):
        user1+=1
    elif choose2 == choose1:
        print("Tie")
    else:
        print("Invalid Input")
    stop = int(input("Enter 0 to continue "))

print("User 1 score", user1)
print("User 2 score", user2)
if user2>user1:
    print("User 2 wins")
elif user1>user2:
    print("User 1 wins")
else:
    print("Tie")