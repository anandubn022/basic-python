students = {}

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks

    elif choice == "2":
        print("\nStudent List:")
        for name, marks in students.items():
            print(f"{name}: {marks}")

    elif choice == "3":
        break

    else:
        print("Invalid choice!")
