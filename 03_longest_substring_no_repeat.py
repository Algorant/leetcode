'''
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = {}
        result = 0
        start = 0
        # iterate through str
        # slice out unique strings, append to longest
        # if find a longer one, replace longest
        for i, j in enumerate(s):
            if j not in longest or longest[j] < start:
                result = max(result, i - start + 1)
            else:
                start = longest[j] + 1
            longest[j] = i
        return result
        
