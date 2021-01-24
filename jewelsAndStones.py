'''

You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a
type of stone you have. You want to know how many of the stones you have are
also jewels.

Letters are case sensitive, so "a" is considered a different type of stone
from "A".


Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

'''

def newJewelsInStones(jewels, stones):
    tot = 0
    for i in jewels:
        for j in stones:
            if i ==j:
                tot +=1
    return tot


print(newJewelsInStones("aA", "aAAbbbb"))
