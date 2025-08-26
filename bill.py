# Dictionary to store items
bill_items = {}

while True:
    print("\n--- Simple Billing System ---")
    print("1. Add Item")
    print("2. View Bill")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))

        # Add to dictionary
        if name in bill_items:
            bill_items[name]['qty'] += qty
        else:
            bill_items[name] = {'qty': qty, 'price': price}

    elif choice == "2":
        print("\n--- Bill Summary ---")
        total = 0
        for item, details in bill_items.items():
            item_total = details['qty'] * details['price']
            print(f"{item} - {details['qty']} x {details['price']} = ₹{item_total:.2f}")
            total += item_total
        print(f"Total Amount: ₹{total:.2f}")

    elif choice == "3":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")