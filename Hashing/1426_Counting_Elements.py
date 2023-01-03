# https://leetcode.com/problems/counting-elements/description/
# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
# If there are duplicates in arr, count them separately.

class Solution:
    def findDifference(self, arr: List[int]) -> List[List[int]]:
        new_set = set(arr)
        count = 0
        for item in arr:
            if item+1 in new_set:
                count += 1
        return count