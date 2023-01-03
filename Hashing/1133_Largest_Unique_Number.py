# https://leetcode.com/problems/largest-unique-number/description/
# Given an integer array nums, return the largest integer that only occurs once.
# If no integer occurs once, return -1.

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        unique = []
        for i in range(len(nums)):
            if nums.count(nums[i]) < 2:
                unique.append(nums[i])
        if len(unique) == 0:
            return -1
        else:
            return max(unique)