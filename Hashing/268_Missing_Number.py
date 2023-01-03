# https://leetcode.com/problems/missing-number/description/
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        stor = set(nums)
        for i in range(0, len(nums) + 1):
            if not i in stor:
                return i