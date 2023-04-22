class Solution:
    # def __init__(self):

    def canJump(self, nums: List[int]) -> bool:

        lastpos = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastpos:
                lastpos = i
        return lastpos == 0


