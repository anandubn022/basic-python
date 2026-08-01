prices = [7, 10, 1, 3, 6, 9, 2]
min_ = prices[0]
output = 0
for i in prices:
    min_ = min(i, min_)
    output = max (output, i - min_)
print(output)