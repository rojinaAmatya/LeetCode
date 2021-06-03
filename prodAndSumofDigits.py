'''
Given an integer number n, return the difference
between the product of its digits and the sum of its digits.
'''

def subtractProductAndSum(n):
    prod =1
    sum1 = 0
    while (n!=0):
        digit = (n%10)
        n = n//10
        prod *= digit
        sum1 += digit
    return (prod - sum1)

print(subtractProductAndSum(234))
