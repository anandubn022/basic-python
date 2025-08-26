t = int(input("Enter number of inputs: "))
number = map(int, input().split())
i = 0
while i < t:
    number[i] = int(number[i])
    i = i + 1

number.sort()
print("Runner-up score is:", number[-2])
