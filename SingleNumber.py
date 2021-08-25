'''
Given a non-empty array of integers nums,
every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime
complexity and use only constant extra space.

'''

def singleNumber(nums):
    newList = []
    for i in nums:
        if i in newList:
            newList.remove(i)
        else:
            newList.append(i)
    return newList.pop()

print(singleNumber([4,1,2,1,2]))
