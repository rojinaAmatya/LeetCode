'''

Given a non-empty array of decimal digits representing a
non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit
is at the head of the list, and each element in the array
contains a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.
'''

def plusOne(digits):
    digits  = digits[::-1]
    carryover, i = 1, 0
    while carryover:
        if i < len(digits):
            if digits[i]==9:
                carryover = 1
                digits[i]=0
            else:
                digits[i]+=1
                carryover = 0
        else:
            digits.append(1)
            carryover = 0
        i += 1
    return digits[::-1]

print(plusOne([9,9,9]))
