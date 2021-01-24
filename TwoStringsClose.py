'''
https://leetcode.com/problems/determine-if-two-strings-are-close/
The two words could be close if they:
1. have same length
2. contain same characters
3. have same amount of characters that are of same count
'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        num11=Counter(word1)
        num2=Counter(word2)
        if num1.keys()!=num2.keys():
            return False
        if Counter(num1.values())!=Counter(num2.values()):
            return False
        return True



