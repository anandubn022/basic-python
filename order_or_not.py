def in_order(my_string):
    my_string = my_string.lower();
    for i in range(0, len(my_string)-1):
        if my_string[i] > my_string[i+1]:
            return False
        
    return True

str1 = input("enter a word ")
print("word in alphabet order" if in_order(str1) else "word not in alphabet order")