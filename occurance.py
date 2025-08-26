number = input("Enter a number ")
digit = input("Enter the digit to count ")

count_dict= {}

for d in number:
    if d in count_dict:
        count_dict[d] += 1
    else:
        count_dict[d] = 1
print(count_dict)
print(f"The digit {digit} occurs {count_dict.get(digit, 0)} time(s).")