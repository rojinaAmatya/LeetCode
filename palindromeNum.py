'''

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as
forward. For example, 121 is palindrome while 123 is not.

 

'''


def isPalindrome(x):
    y = (str(x)[::-1])
    return str(x) == y

print(isPalindrome("121"))
