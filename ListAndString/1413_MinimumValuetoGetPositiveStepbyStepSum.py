class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        min = float('inf')
        for item in prefix:
            if item < min:
                min = item
        if min >= 0:
            return 1
        else:
            return abs(min) + 1

#         time: o(n)
#         space:O（n）