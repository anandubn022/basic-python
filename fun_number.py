def isprime(n):
    if n<2:
        return False
    for i in range (2, n//2 + 1):
        if n%i == 0:
            return False
    return True

def fun_calc(lower, upper):
    count = 0
    for i in range(lower, upper):
        tmp = i
        sum = 0
        sqr_sum = 0
        while tmp!=0:
            digit = tmp%10
            tmp = tmp//10
            sum += digit
            sqr_sum += digit**2
        if isprime(sum) and isprime(sqr_sum):
            count+=1
    return count

lower = int(input("Enter lower limit : "))
upper = int(input("Enter upper limit : "))
print("No of fun numbers :", fun_calc(lower, upper+1))