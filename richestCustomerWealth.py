def maximumWealth(accounts):
    tot = 0
    ans = 0
    for i in accounts:
        for j in i:
            tot += j
        ans = max(ans,tot)
        tot= 0
    return ans
print(maximumWealth([[1,2,3],[3,2,1]]))
