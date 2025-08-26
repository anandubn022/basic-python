pswd = input("Enter the password ")
n = len(pswd)

lower = False
upper = False
digit = False

# Check for character types
for c in pswd:
    if 'a' <= c <= 'z':
        lower = True
    elif 'A' <= c <= 'Z':
        upper = True
    elif '0' <= c <= '9':
        digit = True

# Count missing types
missing = 0
if not lower:
    missing += 1
if not upper:
    missing += 1
if not digit:
    missing += 1

# Count sequences of 3+ repeating characters
i = 2
replace = 0
while i < n:
    if pswd[i] == pswd[i - 1] == pswd[i - 2]:
        replace += 1
        i += 2  # Skip next character to avoid overlapping replacements
    else:
        i += 1

# Decide how many changes are needed
if n < 6:
    print("Changes needed:", max(missing, replace, 6 - n))
elif n <= 20:
    print("Changes needed:", max(missing, replace))
else:
    print("Length > 20 — consider trimming the password")