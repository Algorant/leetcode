'''
Given a string s, return the longest palindromic substring in s.
'''

def longestPalindrome(s):
    result = ""
    n = len(s)

    def helper(i, j):
        while i >= 0 and j < n and s[i] == s[j]:
            i, j = i-1, j+1
        return s[i+1:j]

    for k in range(n):
        result = max(helper(k, k), helper(k,k+1), result, key=len)

    return result
