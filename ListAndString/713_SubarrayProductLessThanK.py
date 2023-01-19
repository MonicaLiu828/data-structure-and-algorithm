class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # give two pointer, multiple(1) and countsubarr(0)
        # move right and count the multiple
        # if multiple < k, countsubarr has newest right's method: r -l +1
        # if multiple >=k, move left and check again
        # finalcount then = each countsubarr's sum
        if k <= 1:
            return 0
        l = r = count = 0
        multiple = 1
        while r < len(nums):
            multiple = multiple * nums[r]
            while multiple >= k and l < len(nums):
                multiple = multiple / nums[l]
                l += 1
            count = count + r - l + 1
            r += 1
        return count
