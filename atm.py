balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Your balance is ₹{balance}")

    elif choice == "2":
        amt = float(input("Enter amount to deposit: "))
        balance += amt
        print(f"Deposited ₹{amt}")

    elif choice == "3":
        amt = float(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance -= amt
            print(f"Withdrawn ₹{amt}")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice!")
