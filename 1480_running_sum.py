"""
Given an array nums, we define a running sum of an array as:
runningSum[i] = sum(nums[0]..nums[i])

Return the running sum of nums.
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return ([sum(nums[0:i+1]) for i in range(0,len(nums))])
