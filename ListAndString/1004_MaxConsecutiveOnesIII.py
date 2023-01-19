class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # set l and r two pointers
        # move when there are k+1's 0, move left point until only k's 0
        #  each step max current len with new len

        l = r = maxnum = count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            maxnum = max(maxnum, r - l + 1)
        return maxnum
