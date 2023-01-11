class Solution:
    # I -> array of nums, target
    # o -> [] has two elements, first is the left-most index, second is the right-most index
    # c: O(log n) -> it reminds to use binary search method
    # e: if length of nums is 0 and it requires to find a target in this empty nums[-1, -1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #  edge case
        if len(nums) == 0:
            return [-1, -1]

        l = 0
        r = len(nums) - 1
        res = []
        #  left-most method:
        #  insead of l <=r:

        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        c = r if nums[r] == target else -1
        res.append(c)

        # right -most
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2 + 1
            if nums[m] <= target:
                l = m
            else:
                r = m - 1
        d = l if nums[l] == target else -1
        res.append(d)
        return res

        # if not nums:
        #     return [-1, -1]

        # def bisect_left(nums, target):
        #     l, r = 0, len(nums) - 1
        #     while l < r:
        #         m = (l + r) // 2
        #         if nums[m] < target:
        #             l = m + 1
        #         else:
        #             r = m
        #     return l if nums[l] == target else -1

        # def bisect_right(nums, target):
        #     l, r = 0, len(nums) - 1
        #     while l < r:
        #         m = (l + r) // 2 + 1
        #         if nums[m] > target:
        #             r = m - 1
        #         else:
        #             l = m
        #     return l if nums[l] == target else -1

        # return [bisect_left(nums, target), bisect_right(nums, target)]