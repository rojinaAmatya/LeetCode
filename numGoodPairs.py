'''

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
'''

def numIdenticalPairs(num):
    newDict ={}
    tot = 0
    for i in num:
        if not i in newDict:
            newDict[i]=0
        newDict[i]+= 1

    for i in newDict:
        num = newDict[i]
        tot += (num * (num-1)//2)
    return tot

print(numIdenticalPairs([1,2,3,1,1,3]))
