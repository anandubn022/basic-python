age = int(input())
gender = input()

if gender == 'm' or gender == 'M' or gender == 'male' or gender == 'Male' or gender == 'MALE':
    if age>60:
        print("Senior Citizen")
    else:
        print("not Senior Citizen")
else:
    if age>58:
        print("Senior Citizen")
    else:
        print("not Senior Citizen")