'''

Given the array nums, for each nums[i] find out how many numbers
in the array are smaller than it. That is, for each nums[i] you
have to count the number of valid j's such that j != i and
nums[j] < nums[i].

Return the answer in an array.

'''

def smallerNumbersThanCurrent(nums):
    sortedList = sorted(nums)
    myDict = {}
    result = []
    
    for i in range(len(sortedList)):
        if sortedList[i] not in myDict:
            myDict[sortedList[i]] = i
            
    for i in nums:
        result.append(myDict[i])
        
    return result

print(smallerNumbersThanCurrent([8,1,2,2,3]))
