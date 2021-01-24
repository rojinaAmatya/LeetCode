'''

Given an array nums.
We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

'''

class Solution:
    def runningSum(self, nums):
        sum = 0
        newList =[]
        for i in nums:
            sum = i + sum
            newList.append(sum)
        return newList
            

        
#go through the list of integers
#define new integers and initialize it to 0
#create a new list to append the sum of numbers
#return the list
