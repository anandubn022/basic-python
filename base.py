n = '23GF'
# n = int(n, 17)
# print("Decimal", n)
d ={
    '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16
}
decimal = 0
power = 0
for i in reversed(n):
    decimal = decimal + ( (d[i]) * (17**power) )
    power+=1
print("Decimal", decimal)