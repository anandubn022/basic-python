movies = {
    "Avengers": {"seats": 5, "price": 150},
    "Inception": {"seats": 3, "price": 200},
    "Interstellar": {"seats": 4, "price": 180}
}

while True:
    print("\n Welcome to the Movie Ticket Booking System")
    print("1. View Movies")
    print("2. Book Tickets")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Movies:")
        for movie, info in movies.items():
            print(f"{movie} - ₹{info['price']} - {info['seats']} seats left")
    
    elif choice == "2":
        movie_name = input("Enter movie name to book: ")
        if movie_name in movies:
            available = movies[movie_name]["seats"]
            print(f"{available} seats available for {movie_name}")
            if available > 0:
                num = int(input("How many tickets do you want? "))
                if 0 < num <= available:
                    total = num * movies[movie_name]["price"]
                    print(f"Total cost: ₹{total}")
                    confirm = input("Confirm booking (yes/no)? ").lower()
                    if confirm == "yes":
                        movies[movie_name]["seats"] -= num
                        print("✅ Booking confirmed!")
                    else:
                        print("❌ Booking cancelled.")
                else:
                    print("❗ Invalid number of tickets.")
            else:
                print("❌ No seats available!")
        else:
            print("❌ Movie not found!")
    
    elif choice == "3":
        print("Thank you for using the Movie Ticket Booking System!")
        break
    
    else:
        print("Invalid choice. Try again.")
