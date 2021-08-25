
def romantoInt(s):
    hash = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    n = len(s)
    i = n-1
    output = 0

    while i >= 0:
        if i <  n-1 and hash[s[i]] < hash[s[i+1]]:
            output -= hash[s[i]]
        else:
            output +=hash[s[i]]
        i -=1
    return output
        


print(romantoInt("IV"))

