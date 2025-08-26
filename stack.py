stack = []
top = -1
max_size = 0

def push():
    global top
    if top == max_size - 1:
        print("\nOverflow")
    else:
        item = int(input("\nEnter the item to be added: "))
        top += 1
        stack.append(item)
        print(f"Value of item pushed: {item}")

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        print(f"Value to be popped from the stack: {stack[top]}")
        stack.pop()
        top -= 1

def display():
    if top == -1:
        print("Stack is Underflow")
    else:
        print("Stack contents:")
        for i in range(top, -1, -1):
            print(stack[i])

def main():
    global max_size
    max_size = int(input("Enter the size of the stack: "))
    choice = 0
    while choice < 4:
        print("\nEnter 1 for Push")
        print("Enter 2 for Pop")
        print("Enter 3 for Display")
        print("Enter 4 to Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            push()
        elif choice == 2:
            pop()
        elif choice == 3:
            display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
